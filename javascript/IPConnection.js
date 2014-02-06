var net = require('net');
var Device = require('./Device');

IPConnection.FUNCTION_ENUMERATE = 254;
IPConnection.FUNCTION_DISCONNECT_PROBE = 128;
IPConnection.CALLBACK_ENUMERATE = 253;
IPConnection.CALLBACK_CONNECTED = 0;
IPConnection.CALLBACK_DISCONNECTED = 1;
IPConnection.BROADCAST_UID = 0;
// enumeration_type parameter to the enumerate callback
IPConnection.ENUMERATION_TYPE_AVAILABLE = 0;
IPConnection.ENUMERATION_TYPE_CONNECTED = 1;
IPConnection.ENUMERATION_TYPE_DISCONNECTED = 2;
// connect_reason parameter to the connected callback
IPConnection.CONNECT_REASON_REQUEST = 0;
IPConnection.CONNECT_REASON_AUTO_RECONNECT = 1;
// disconnect_reason parameter to the disconnected callback
IPConnection.DISCONNECT_REASON_REQUEST = 0;
IPConnection.DISCONNECT_REASON_ERROR = 1;
IPConnection.DISCONNECT_REASON_SHUTDOWN = 2;
// returned by getConnectionState
IPConnection.CONNECTION_STATE_DISCONNECTED = 0;
IPConnection.CONNECTION_STATE_CONNECTED = 1;
IPConnection.CONNECTION_STATE_PENDING = 2; //auto-reconnect in process
IPConnection.DISCONNECT_PROBE_INTERVAL = 5000;
IPConnection.RETRY_CONNECTION_INTERVAL = 2000;
// error codes
IPConnection.ERROR_ALREADY_CONNECTED = 11;
IPConnection.ERROR_NOT_CONNECTED = 12;
IPConnection.ERROR_AUTO_RECONNECT_IN_PROGRESS = 13;
IPConnection.ERROR_CONNECT_FAILED = 13;
IPConnection.ERROR_INVALID_FUNCTION_ID = 21;
IPConnection.ERROR_TIMEOUT = 31;
IPConnection.ERROR_INVALID_PARAMETER = 41;
IPConnection.ERROR_FUNCTION_NOT_SUPPORTED = 42;

//the IPConnection class and constructor
function IPConnection() {
    // Creates an IP Connection object that can be used to enumerate the available
    // devices. It is also required for the constructor of Bricks and Bricklets.
    this.host = undefined;
    this.port = undefined;
    this.timeout = 2500;
    this.autoReconnect = true;
    this.autoReconnectPending = false;
    this.sequenceNumber = 0;
    this.authKey = undefined;
    this.devices = {};
    this.registeredCallbacks = {};
    this.socket = undefined;
    this.disconnectProbeIID = undefined;
    this.retryConnectionIID = undefined;
    this.isConnected = false;
    this.disconnectRequested = false;
    this.connectRequested = false;
    this.connectionPending = false;
    this.connectErrorCallback = undefined;
    this.disconnectErrorCallback = undefined;
    this.mergeBuffer = new Buffer(0);
    
    this.disconnectProbe = function() {
        if(this.socket !== undefined) {
            this.socket.write(this.createPacketHeader(undefined, 8, IPConnection.FUNCTION_DISCONNECT_PROBE));
        }
    };
    this.disconnect = function(disconnectErrorCallback) {
        this.disconnectErrorCallback = disconnectErrorCallback;
        //checking if already disconnected
        if(!this.isConnected || this.socket === undefined) {
            if (this.connectErrorCallback !== undefined) {
                this.disconnectErrorCallback(IPConnection.ALREADY_DISCONNECTED);
            }
            return;
        }
        this.disconnectRequested = true;
        this.connectRequested = false;
        //if retry pending clear the flag and stop it
        if(this.connectionPending) {
            clearInterval(this.retryConnectionIID);
            this.connectionPending = false;
        }
        this.socket.end();
        this.socket.destroy();
        if(this.socket !== undefined) {
            this.socket.write(this.createPacketHeader(undefined, 8, IPConnection.FUNCTION_DISCONNECT_PROBE));
        }
        return;
    };
    this.connect = function(HOST, PORT, connectErrorCallback) {
        this.connectErrorCallback = connectErrorCallback;
        //checking if already connected
        if(this.isConnected && this.socket !== undefined && this.host != undefined && this.port != undefined) {
            if (this.connectErrorCallback !== undefined) {
                this.connectErrorCallback(IPConnection.ERROR_ALREADY_CONNECTED);
            }
            return;
        }
        //checking if reconnect retry is in progress
        //if so then calling user error CB(if any) and simply returning
        if(this.connectionPending) {
        	if (this.connectErrorCallback !== undefined) {
        		this.connectErrorCallback(IPConnection.ERROR_AUTO_RECONNECT_IN_PROGRESS);
        	}
        	return;
        }
        clearInterval(this.retryConnectionIID);
        clearInterval(this.disconnectProbeIID);
        this.isConnected = false;
        this.connectRequested = true;
        this.disconnectRequested = false;
        this.host = HOST;
        this.port = PORT;
        this.socket = new net.Socket();
        this.socket.setNoDelay(true);
        this.socket.on('connect', this.handleConnect.bind(this));
        this.socket.on('data', this.handleIncomingData.bind(this));
        this.socket.on('error', this.handleConnectionError.bind(this));
        this.socket.on('close', this.handleConnectionClose.bind(this));
        this.socket.connect(this.port, this.host, null);
    };
    this.handleConnect = function() {
        if(this.connectRequested) {
            clearInterval(this.retryConnectionIID);
            clearInterval(this.disconnectProbeIID);
            this.isConnected = true;
            this.connectRequested = false;
            this.disconnectRequested = false;
            this.connectionPending = false;
            
            //check and call functions if registered for callback connected
            if(this.registeredCallbacks[IPConnection.CALLBACK_CONNECTED] !== undefined) {
                this.registeredCallbacks[IPConnection.CALLBACK_CONNECTED](IPConnection.CONNECT_REASON_REQUEST);
            }
            
            this.disconnectProbeIID = setInterval(this.disconnectProbe.bind(this),
                                                       IPConnection.DISCONNECT_PROBE_INTERVAL);
            return;
        }
        //if true then reconnected from auto reconnect try
        if(this.connectionPending) {
            clearInterval(this.disconnectProbeIID);
            clearInterval(this.retryConnectionIID);
            this.isConnected = true;
            this.connectRequested = false;
            this.disconnectRequested = false;
            this.connectionPending = false;
            
            //check and call functions if registered for callback connected
            if(this.registeredCallbacks[IPConnection.CALLBACK_CONNECTED] !== undefined) {
                this.registeredCallbacks[IPConnection.CALLBACK_CONNECTED](IPConnection.CONNECT_REASON_AUTO_RECONNECT);
            }
            
            this.disconnectProbeIID = setInterval(this.disconnectProbe.bind(this),
                                                       IPConnection.DISCONNECT_PROBE_INTERVAL);
        }
    };
    this.handleIncomingData = function(data) {
        if(data.length === 0) {
            return;
        }
        this.mergeBuffer = bufferConcat([this.mergeBuffer, data]);
        if(this.mergeBuffer.length < 8) {
            return;
        }
        if(this.mergeBuffer.length < this.mergeBuffer.readUInt8(4)) {
            return;
        }
        while(this.mergeBuffer.length >= 8) {
            var newPacket = new Buffer(this.mergeBuffer.readUInt8(4));
            this.mergeBuffer.copy(newPacket, 0, 0, this.mergeBuffer.readUInt8(4));
            this.handlePacket(newPacket);
            this.mergeBuffer = this.mergeBuffer.slice(this.mergeBuffer.readUInt8(4));
        }
    };
    this.handleConnectionError = function(error) {
        if(error['errno'] === 'ECONNRESET') {
            //check and call functions if registered for callback disconnected
            if(this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED] !== undefined) {
                this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED](IPConnection.DISCONNECT_REASON_SHUTDOWN);
            }
        }
    };
    this.handleConnectionClose = function() {
        if(this.disconnectRequested) {
            for(var i=0; i<this.devices.length; i++) {
            	clearTimeout(this.devices[i].expectedResponses.timeout);
                this.devices[i].expectedResponses = [];
            }
            this.isConnected = false;
            this.connectRequested = false;
            this.disconnectRequested = false;
            this.connectionPending = false;
            clearInterval(this.disconnectProbeIID);
            clearInterval(this.retryConnectionIID);
            if(this.socket !== undefined) {
                this.socket.end();
                this.socket.destroy();
                this.socket = undefined;
            }
            //check and call functions if registered for callback disconnected
            if(this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED] !== undefined) {
                this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED](IPConnection.DISCONNECT_REASON_REQUEST);
            }
            return;
        }
        //was connected, disconnected because of error and auto reconnect is enabled
        if(this.isConnected && this.autoReconnect && !this.disconnectRequested) {
            this.isConnected = false;
            this.connectRequested = false;
            this.disconnectRequested = false;
            this.connectionPending = true;
            clearInterval(this.disconnectProbeIID);
            clearInterval(this.retryConnectionIID);
            if(this.socket !== undefined) {
                this.socket.end();
                this.socket.destroy();
                this.socket = undefined;
            }
            //check and call functions if registered for callback disconnected
            if(this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED] !== undefined) {
                this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED](IPConnection.DISCONNECT_REASON_ERROR);
            }
            this.retryConnectionIID = setInterval(this.retryConnection.bind(this),
                                                       IPConnection.RETRY_CONNECTION_INTERVAL);
            return;
        }
        //same as before but auto reconnect is disabled
        if(this.isConnected && !this.autoReconnect && !this.disconnectRequested && 
            this.host != undefined && this.port != undefined) {
            this.isConnected = false;
            this.connectRequested = false;
            this.disconnectRequested = false;
            this.connectionPending = false;
            clearInterval(this.disconnectProbeIID);
            clearInterval(this.retryConnectionIID);
            if(this.socket !== undefined) {
                this.socket.end();
                this.socket.destroy();
                this.socket = undefined;
            }
            //check and call functions if registered for callback disconnected
            if(this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED] !== undefined) {
                this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED](IPConnection.DISCONNECT_REASON_ERROR);
                return;
            }
            return;
        }
        //were not connected. failed at new connection attempt
        if(!this.connectionPending) {
            //check and call functions if registered for callback disconnected
            if(this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED] !== undefined) {
                this.registeredCallbacks[IPConnection.CALLBACK_DISCONNECTED](IPConnection.DISCONNECT_REASON_ERROR);
                return;
            }
            if (this.connectErrorCallback !== undefined) {
                
                this.connectErrorCallback(IPConnection.ERROR_CONNECT_FAILED);
            }
        }
        return;
    };
    this.retryConnection = function() {
        this.socket = new net.Socket();
        this.socket.setNoDelay(true);
        this.socket.on('connect', this.handleConnect.bind(this));
        this.socket.on('data', this.handleIncomingData.bind(this));
        this.socket.on('error', this.handleConnectionError.bind(this));
        this.socket.on('close', this.handleConnectionClose.bind(this));
        this.socket.connect(this.port, this.host, null);
    };

    this.getUIDFromPacket = function(packetUID){
        return packetUID.readUInt32LE(0);
    };
    this.getLengthFromPacket = function(packetLen) {
        return packetLen.readUInt8(4);
        
    };
    this.getFunctionIDFromPacket = function(packetFID) {
        return packetFID.readUInt8(5);
    };
    this.getSequenceNumberFromPacket = function(packetSeq) {
        return (packetSeq.readUInt8(6) >>> 4) & 0x0F;
    };
    this.getRFromPacket = function(packetR) {
        return (packetR.readUInt8(6) >>> 3) & 0x01;
    };
    this.getAFromPacket = function(packetA) {
        return (packetA.readUInt8(6) >>> 2) & 0x01;
    };
    this.getOOFromPacket = function(packetOO) {
        return packetOO.readUInt8(6) & 0x03;
    };
    this.getEFromPacket = function(packetE) {
        //getting Error bits(E, 2bits)
        return (packetE.readUInt8(7) >>> 6) & 0x03;
    };
    this.getFutureUseFromPacket = function(packetFutureUse) {
        //getting Future Use(6bits)
        return (packetFutureUse.readUInt8(7) >>> 6) & 0x63;
    };
    this.getPayloadFromPacket = function(packetPayload) {
        var payloadReturn = new Buffer(packetPayload.length - 8);
        packetPayload.copy(payloadReturn, 0, 8, packetPayload.length);
        return new Buffer(payloadReturn);
    };
    function pack(data, format) {
        var formatArray = format.split(' ');
        if(formatArray.length <= 0) {
            return new Buffer(0);
        }
        var packedBuffer = new Buffer(0);
        for(var i=0; i<formatArray.length; i++){
            if(formatArray[i].split('').length === 1) {
                if(formatArray[i] === 's') {
                    var tmpPackedBuffer = new Buffer(1);
                    tmpPackedBuffer.fill(0x00);
                    tmpPackedBuffer.writeUInt8(data[i].charCodeAt(0), 0);
                    packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                    continue;
                }
                switch(formatArray[i]) {
                    case 'c':
                        var tmpPackedBuffer = new Buffer(1);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeUInt8(data[i].charCodeAt(0), 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'b':
                        var tmpPackedBuffer = new Buffer(1);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeInt8(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'B':
                        var tmpPackedBuffer = new Buffer(1);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeUInt8(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'h':
                        var tmpPackedBuffer = new Buffer(2);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeInt16LE(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'H':
                        var tmpPackedBuffer = new Buffer(2);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeUInt16LE(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'i':
                        var tmpPackedBuffer = new Buffer(4);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeInt32LE(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'I':
                        var tmpPackedBuffer = new Buffer(4);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeUInt32LE(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'q':
                        var tmpPackedBuffer = new Buffer(8);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeDoubleLE(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'Q':
                        var tmpPackedBuffer = new Buffer(8);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeDoubleLE(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'f':
                        var tmpPackedBuffer = new Buffer(4);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeFloatLE(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                    case 'd':
                        var tmpPackedBuffer = new Buffer(8);
                        tmpPackedBuffer.fill(0x00);
                        tmpPackedBuffer.writeDoubleLE(data[i], 0);
                        packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        continue;
                }
            }
            if(formatArray[i].split('').length > 1) {
                var singleFormatArray = formatArray[i].split('');
                for(var j=0; j<parseInt(formatArray[i].match(/\d/g).join('')); j++) {
                    if(singleFormatArray[0] === 's') {
                        if(!isNaN(data[i].charCodeAt(j))) {
                            var tmpPackedBuffer = new Buffer(1);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeUInt8(data[i].charCodeAt(j), 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        }
                        else {
                            var tmpPackedBuffer = new Buffer(1);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeUInt8(0x00, 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                        }
                        continue;
                    }
                    switch(singleFormatArray[0]) {
                        case 'c':
                            var tmpPackedBuffer = new Buffer(1);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeUInt8(data[i][j].charCodeAt(0), 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'b':
                            var tmpPackedBuffer = new Buffer(1);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeInt8(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'B':
                            var tmpPackedBuffer = new Buffer(1);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeUInt8(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'h':
                            var tmpPackedBuffer = new Buffer(2);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeInt16LE(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'H':
                            var tmpPackedBuffer = new Buffer(2);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeUInt16LE(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'i':
                            var tmpPackedBuffer = new Buffer(4);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeInt32LE(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'I':
                            var tmpPackedBuffer = new Buffer(4);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeUInt32LE(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'q':
                            var tmpPackedBuffer = new Buffer(8);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeDoubleLE(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'Q':
                            var tmpPackedBuffer = new Buffer(8);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeDoubleLE(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'f':
                            var tmpPackedBuffer = new Buffer(4);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeFloatLE(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                        case 'd':
                            var tmpPackedBuffer = new Buffer(8);
                            tmpPackedBuffer.fill(0x00);
                            tmpPackedBuffer.writeDoubleLE(data[i][j], 0);
                            packedBuffer = bufferConcat([packedBuffer,tmpPackedBuffer]);
                            continue;
                    }
                }
            }
        }
        return packedBuffer;
    }
    function unpack(unpackPayload, format) {
        var formatArray = format.split(' ');
        var returnArguments = [];
        var returnSubArray = [];
        var constructedString = '';
        var payloadReadOffset = 0;
        if(formatArray.length <= 0) {
            return returnArguments;
        }
        for(var i=0; i<formatArray.length; i++) {
            if(formatArray[i].split('').length === 1) {
                if(formatArray[i] === 's') {
                    constructedString += String.fromCharCode(unpackPayload.readUInt8(payloadReadOffset));
                    payloadReadOffset++;
                    returnArguments.push(constructedString);
                    constructedString = '';
                    continue;
                }
                switch(formatArray[i]) {
                    case 'c':
                        returnArguments.push(String.fromCharCode(unpackPayload.readUInt8(payloadReadOffset)));
                        payloadReadOffset++;
                        continue;
                    case 'b':
                        returnArguments.push(unpackPayload.readInt8(payloadReadOffset));
                        payloadReadOffset++;
                        continue;
                    case 'B':
                        returnArguments.push(unpackPayload.readUInt8(payloadReadOffset));
                        payloadReadOffset++;
                        continue;
                    case 'h':
                        returnArguments.push(unpackPayload.readInt16LE(payloadReadOffset));
                        payloadReadOffset = payloadReadOffset + 2;
                        continue;
                    case 'H':
                        returnArguments.push(unpackPayload.readUInt16LE(payloadReadOffset));
                        payloadReadOffset = payloadReadOffset + 2;
                        continue;
                    case 'i':
                        returnArguments.push(unpackPayload.readInt32LE(payloadReadOffset));
                        payloadReadOffset = payloadReadOffset + 4;
                        continue;
                    case 'I':
                        returnArguments.push(unpackPayload.readUInt32LE(payloadReadOffset));
                        payloadReadOffset = payloadReadOffset + 4;
                        continue;
                    case 'q':
                        returnArguments.push(unpackPayload.readDoubleLE(payloadReadOffset));
                        payloadReadOffset = payloadReadOffset + 8;
                        continue;
                    case 'Q':
                        returnArguments.push(unpackPayload.readDoubleLE(payloadReadOffset));
                        payloadReadOffset = payloadReadOffset + 8;
                        continue;
                    case 'f':
                        returnArguments.push(unpackPayload.readFloatLE(payloadReadOffset));
                        payloadReadOffset = payloadReadOffset + 4;
                        continue;
                    case 'd':
                        returnArguments.push(unpackPayload.readDoubleLE(payloadReadOffset));
                        payloadReadOffset = payloadReadOffset + 8;
                        continue;
                }
            }
            if(formatArray[i].split('').length > 1) {
                var singleFormatArray = formatArray[i].split('');
                if(singleFormatArray[0] === 's') {
                    constructedString = '';
                    for(var j=0; j<parseInt(formatArray[i].match(/\d/g).join('')); j++) {
                        constructedString += String.fromCharCode(unpackPayload.readUInt8(payloadReadOffset));
                        payloadReadOffset++;
                    }
                    returnArguments.push(constructedString);
                    constructedString = '';
                    continue;
                }
                returnSubArray = [];
                for(var k=0; k<parseInt(formatArray[i].match(/\d/g).join('')); k++) {
                    switch(singleFormatArray[0]) {
                        case 'c':
                            returnSubArray.push(String.fromCharCode(unpackPayload.readUInt8(payloadReadOffset)));
                            payloadReadOffset++;
                            continue;
                        case 'b':
                            returnSubArray.push(unpackPayload.readInt8(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'B':
                            returnSubArray.push(unpackPayload.readUInt8(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'h':
                            returnSubArray.push(unpackPayload.readInt16LE(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'H':
                            returnSubArray.push(unpackPayload.readIntU16LE(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'i':
                            returnSubArray.push(unpackPayload.readInt32LE(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'I':
                            returnSubArray.push(unpackPayload.readIntU32LE(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'q':
                            returnSubArray.push(unpackPayload.readDoubleLE(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'Q':
                            returnSubArray.push(unpackPayload.readDoubleLE(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'f':
                            returnSubArray.push(unpackPayload.readFloatLE(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                        case 'd':
                            returnSubArray.push(unpackPayload.readDoubleLE(payloadReadOffset));
                            payloadReadOffset++;
                            continue;
                    }
                }
                if(returnSubArray.length !== 0) {
                    returnArguments.push(returnSubArray);
                    returnSubArray = [];
                    continue;
                }
            }
        }
        return returnArguments;
     }
    
    this.sendRequest = function(sendRequestDevice, sendRequestFID, sendRequestData,
                                sendRequestPackFormat, sendRequestUnpackFormat,
                                sendRequestReturnCB, sendRequestErrorCB) {
    	if(this.getConnectionState() === IPConnection.CONNECTION_STATE_DISCONNECTED ||
    			this.getConnectionState() === IPConnection.CONNECTION_STATE_PENDING) {
    		if(sendRequestErrorCB !== undefined) {
    			sendRequestErrorCB(IPConnection.ERROR_NOT_CONNECTED);
    		}
    		return;
    	}
        //packet creation
        var sendRequestPayload = pack(sendRequestData, sendRequestPackFormat);
        var sendRequestHeader = this.createPacketHeader(sendRequestDevice,
                                                        8+sendRequestPayload.length,
                                                        sendRequestFID, sendRequestErrorCB);
        if (sendRequestHeader === undefined) {
            return;
        }
        var sendRequestPacket = bufferConcat([sendRequestHeader, sendRequestPayload]);
        var sendRequestSEQ = this.getSequenceNumberFromPacket(sendRequestHeader);
        //sending the created packet
        if(sendRequestDevice.getResponseExpected(sendRequestFID)) {
            //setting the requesting current device's current request            
            var sendRequestDeviceOID = sendRequestDevice.getDeviceOID();
            sendRequestDevice.expectedResponses.push({DeviceOID:sendRequestDeviceOID,
                FID:sendRequestFID,
                SEQ:sendRequestSEQ,
                unpackFormat:sendRequestUnpackFormat,
                timeout:setTimeout(this.sendRequestTimeout.bind
                        (this, sendRequestDevice, sendRequestDeviceOID, sendRequestErrorCB), this.timeout),
                returnCB:sendRequestReturnCB,
                errorCB:sendRequestErrorCB});
        }
        this.socket.write(sendRequestPacket);
    };
    this.sendRequestTimeout = function(timeoutDevice, timeoutDeviceOID, timeoutErrorCB) {
        for(var i=0; i<timeoutDevice.expectedResponses.length; ++i) {
            if(timeoutDevice.expectedResponses[i].DeviceOID === timeoutDeviceOID) {
                clearTimeout(timeoutDevice.expectedResponses[i].timeout);
                timeoutDevice.expectedResponses.splice(i, 1);
                if(timeoutErrorCB !== undefined){
                    timeoutErrorCB(IPConnection.ERROR_TIMEOUT);
                }
                return;
            }
        }
    };
    this.handleResponse = function(packetResponse) {
        var handleResponseDevice = this.devices[this.getUIDFromPacket(packetResponse)];
        var handleResponseFID = this.getFunctionIDFromPacket(packetResponse);
        var handleResponseSEQ = this.getSequenceNumberFromPacket(packetResponse);
        for(var i=0; i < handleResponseDevice.expectedResponses.length; i++) {
            if(this.devices[this.getUIDFromPacket(packetResponse)].expectedResponses[i].returnCB === undefined) {
                clearTimeout(handleResponseDevice.expectedResponses[i].timeout);
                handleResponseDevice.expectedResponses.splice(i, 1);
                return;
            }
            if(this.devices[this.getUIDFromPacket(packetResponse)].expectedResponses[i].unpackFormat === '') {
                clearTimeout(handleResponseDevice.expectedResponses[i].timeout);
                if(handleResponseDevice.expectedResponses[i].returnCB !== undefined) {
                	eval('handleResponseDevice.expectedResponses[i].returnCB();');
                }
                handleResponseDevice.expectedResponses.splice(i, 1);
                return;
            }
            if(handleResponseDevice.expectedResponses[i].FID === handleResponseFID &&
                    handleResponseDevice.expectedResponses[i].SEQ === handleResponseSEQ) {
            	if (this.getEFromPacket(packetResponse) === 1) {
                    clearTimeout(handleResponseDevice.expectedResponses[i].timeout);
            		if(this.devices[this.getUIDFromPacket(packetResponse)].expectedResponses[i].errorCB !== undefined) {
            			eval('handleResponseDevice.expectedResponses[i].errorCB(IPConnection.ERROR_INVALID_PARAMETER);');
            		}
            		handleResponseDevice.expectedResponses.splice(i, 1);
            		return;
            	}
            	if (this.getEFromPacket(packetResponse) === 2) {
                    clearTimeout(handleResponseDevice.expectedResponses[i].timeout);
            		if(this.devices[this.getUIDFromPacket(packetResponse)].expectedResponses[i].errorCB !== undefined) {
            			eval('handleResponseDevice.expectedResponses[i].errorCB(IPConnection.FUNCTION_NOT_SUPPORTED);');
            		}
            		handleResponseDevice.expectedResponses.splice(i, 1);
            		return;
            	}
                clearTimeout(handleResponseDevice.expectedResponses[i].timeout);
                if(handleResponseDevice.expectedResponses[i].returnCB !== undefined) {
                	var retArgs = unpack(this.getPayloadFromPacket(packetResponse),
                			handleResponseDevice.expectedResponses[i].unpackFormat);
                	var evalStr = 'handleResponseDevice.expectedResponses[i].returnCB(';
                	for(var j=0; j<retArgs.length;j++) {
                		eval('var retSingleArg'+j+'=retArgs['+j+'];');
                		if(j != retArgs.length-1) {
                			evalStr += 'retSingleArg'+j+',';
                		}
                		else {
                			evalStr += 'retSingleArg'+j+');';
                		}
                	}
                	eval(evalStr);
                }
                handleResponseDevice.expectedResponses.splice(i, 1);
                return;
            }
        }
    };
    this.handleCallback = function(packetCallback) {
        if(this.getFunctionIDFromPacket(packetCallback) === IPConnection.CALLBACK_ENUMERATE) {
            if(this.registeredCallbacks[IPConnection.CALLBACK_ENUMERATE] !== undefined) {
                var args = unpack(this.getPayloadFromPacket(packetCallback), 's8 s8 c B3 B3 H B');
                var evalCBString = 'this.registeredCallbacks[IPConnection.CALLBACK_ENUMERATE](';
                for(var i=0; i<args.length;i++) {
                    eval('var cbArg'+i+'=args['+i+'];');
                    if(i != args.length-1) {
                        evalCBString += 'cbArg'+i+',';
                    }
                    else {
                        evalCBString += 'cbArg'+i+');';
                    }
                }
                eval(evalCBString);
                return;
            }
        }
        if (this.devices[this.getUIDFromPacket(packetCallback)] === undefined) {
            return;
        }
        if (this.devices[this.getUIDFromPacket(packetCallback)].
            registeredCallbacks[this.getFunctionIDFromPacket(packetCallback)] === undefined ||
            this.devices[this.getUIDFromPacket(packetCallback)].
            callbackFormats[this.getFunctionIDFromPacket(packetCallback)] === undefined) {
            return;
        }
        var cbFunction = this.devices[this.getUIDFromPacket(packetCallback)].
                         registeredCallbacks[this.getFunctionIDFromPacket(packetCallback)];
        var cbUnpackString = this.devices[this.getUIDFromPacket(packetCallback)].
                             callbackFormats[this.getFunctionIDFromPacket(packetCallback)];
        if(cbFunction == undefined) {
            return;
        }
        if(cbUnpackString == undefined) {
            return;
        }
        if(cbUnpackString === '') {
            eval('this.devices[this.getUIDFromPacket(packetCallback)].\
                    registeredCallbacks[this.getFunctionIDFromPacket(packetCallback)]();');
            return;
        }
        var args = unpack(this.getPayloadFromPacket(packetCallback), cbUnpackString);
        var evalCBString = 'this.devices[this.getUIDFromPacket(packetCallback)].\
                            registeredCallbacks[this.getFunctionIDFromPacket(packetCallback)](';
        if(args.length <= 0) {
            eval(evalCBString+');');
            return;
        } 
        for(var i=0; i<args.length;i++) {
            eval('var cbArg'+i+'=args['+i+'];');
            if(i != args.length-1) {
                evalCBString += 'cbArg'+i+',';
            }
            else {
                evalCBString += 'cbArg'+i+');';
            }
        }
        eval(evalCBString);
        return;
    };
    this.handlePacket = function(packet) {
        if(this.getSequenceNumberFromPacket(packet) === 0) {
            this.handleCallback(packet);
        }
        if(this.getSequenceNumberFromPacket(packet) > 0) {
            this.handleResponse(packet);
        }
    };
    this.getConnectionState = function() {
        if(this.isConnected) {
            return IPConnection.CONNECTION_STATE_CONNECTED;
        }
        if(this.connectionPending) {
            return IPConnection.CONNECTION_STATE_PENDING;
        }
        return IPConnection.CONNECTION_STATE_DISCONNECTED;
    };
    this.setAutoReconnect = function(autoReconnectSet) {
        autoReconnect = autoReconnectSet;
    };
    this.getAutoReconnect = function() {
        return autoReconnect;
    };
    this.setTimeout = function(timeoutSet) {
        timeout = timeoutSet;
    };
    this.getTimeout = function() {
        return timeout;
    };
    this.enumerate = function() {
        this.socket.write(this.createPacketHeader(undefined, 8, IPConnection.FUNCTION_ENUMERATE));
    };
    this.on = function(FID, CBFunction) {
        this.registeredCallbacks[FID] = CBFunction;
    };
    this.getNextSequenceNumber = function() {
        if(this.sequenceNumber >= 15) {
            this.sequenceNumber = 0;
        }
        return ++this.sequenceNumber;
    };
    this.createPacketHeader = function(headerDevice, headerLength, headerFunctionID, headerErrorCB) {
        var UID = IPConnection.BROADCAST_UID;
        var len = headerLength;
        var FID = headerFunctionID;
        var seq = this.getNextSequenceNumber();
        var responseBits = 0;
        var authBits = 0;
        var EFutureUse = 0;
        var returnOnError = false;
        if(headerDevice !== undefined) {
            var responseExpected = headerDevice.getResponseExpected(headerFunctionID,
                    function(errorCode){returnOnError = true; if(headerErrorCB !== undefined) {headerErrorCB(errorCode);}});
            if(returnOnError) {
                returnOnError = false;
                
                return;
            }
            UID = headerDevice.uid;
            if(responseExpected) {
                responseBits = 1;
            }
            if(headerDevice.authKey !== undefined) {
                authBits = 1;
            }
        }
        else {
            if(this.authKey != undefined) {
                authBits = 1;
            }
        }
        var seqResponseAuthOOBits = seq << 4;
        if(responseBits) {
            seqResponseAuthOOBits |= (responseBits << 3);
        }
        if(authBits) {
            seqResponseAuthOOBits |= (authBits << 2);
        }
        var returnHeader = new Buffer(8);
        returnHeader.writeUInt32LE(UID, 0);
        returnHeader.writeUInt8(len, 4);
        returnHeader.writeUInt8(FID, 5);
        returnHeader.writeUInt8(seqResponseAuthOOBits, 6);
        returnHeader.writeUInt8(EFutureUse , 7);
        return returnHeader;
    };
    function bufferConcat(arrayOfBuffers) {
        var newBufferSize = 0;
        var targetStart = 0;
        for(var i = 0; i<arrayOfBuffers.length; i++) {
            newBufferSize += arrayOfBuffers[i].length;
        }
        var returnBufferConcat = new Buffer(newBufferSize);
        for(var j=0; j<arrayOfBuffers.length; j++) {
            arrayOfBuffers[j].copy(returnBufferConcat, targetStart);
            targetStart += arrayOfBuffers[j].length;
        }
        return returnBufferConcat;
    }
}

module.exports = IPConnection;