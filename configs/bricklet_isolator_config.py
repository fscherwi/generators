# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Isolator Bricklet communication config

from openhab_common import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 1],
    'category': 'Bricklet',
    'device_identifier': 2122,
    'name': 'Isolator',
    'display_name': 'Isolator',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Galvanically isolates any Bricklet from any Brick',
        'de': 'Trennt Verbindung zwischen Bricklets und Bricks galvanisch'
    },
    'released': True,
    'documented': True,
    'discontinued': False,
    'features': [
        'comcu_bricklet',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['packets'].append({
'type': 'function',
'name': 'Get Statistics',
'elements': [('Messages From Brick', 'uint32', 1, 'out'),
             ('Messages From Bricklet', 'uint32', 1, 'out'),
             ('Connected Bricklet Device Identifier', 'uint16', 1, 'out'),
             ('Connected Bricklet UID', 'string', 8, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns statistics for the Isolator Bricklet.
""",
'de':
"""
Gibt Statistken des Isolator Bricklets zurück.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set SPITFP Baudrate Config',
'elements': [('Enable Dynamic Baudrate', 'bool', 1, 'in'),
             ('Minimum Dynamic Baudrate', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
The SPITF protocol can be used with a dynamic baudrate. If the dynamic baudrate is
enabled, the Isolator Bricklet will try to adapt the baudrate for the communication
between Bricks and Bricklets according to the amount of data that is transferred.

The baudrate for communication config between
Brick and Isolator Bricklet can be set through the API of the Brick.

The baudrate will be increased exponentially if lots of data is send/received and
decreased linearly if little data is send/received.

This lowers the baudrate in applications where little data is transferred (e.g.
a weather station) and increases the robustness. If there is lots of data to transfer
(e.g. Thermal Imaging Bricklet) it automatically increases the baudrate as needed.

In cases where some data has to transferred as fast as possible every few seconds
(e.g. RS485 Bricklet with a high baudrate but small payload) you may want to turn
the dynamic baudrate off to get the highest possible performance.

The maximum value of the baudrate can be set per port with the function
:func:`Set SPITFP Baudrate`. If the dynamic baudrate is disabled, the baudrate
as set by :func:`Set SPITFP Baudrate` will be used statically.

The minimum dynamic baudrate has a value range of 400000 to 2000000 baud.

By default dynamic baudrate is enabled and the minimum dynamic baudrate is 400000.
""",
'de':
"""
Das SPITF-Protokoll kann mit einer dynamischen Baudrate genutzt werden. Wenn die dynamische
Baudrate aktiviert ist, versucht das Isolator Bricklet die Baudrate anhand des Datenaufkommens
zwischen Isolator Bricklet und Bricklet anzupassen.

Die Baudratenkonfiguration für die Kommunikation zwischen
Brick und Isolator Bricklet kann in der API des Bricks eingestellt werden.

Die Baudrate wird exponentiell erhöht wenn viele Daten gesendet/empfangen werden
und linear verringert wenn wenig Daten gesendet/empfangen werden.

Diese Vorgehensweise verringert die Baudrate in Anwendungen wo nur wenig Daten
ausgetauscht werden müssen (z.B. eine Wetterstation) und erhöht die Robustheit.
Wenn immer viele Daten ausgetauscht werden (z.B. Thermal Imaging Bricklet), wird
die Baudrate automatisch erhöht.

In Fällen wo wenige Daten all paar Sekunden so schnell wie Möglich übertragen werden
sollen (z.B. RS485 Bricklet mit hoher Baudrate aber kleinem Payload) kann die
dynamische Baudrate zum maximieren der Performance ausgestellt werden.

Die maximale Baudrate kann pro Port mit der Funktion :func:`Set SPITFP Baudrate`.
gesetzt werden. Falls die dynamische Baudrate nicht aktiviert ist, wird die Baudrate
wie von :func:`Set SPITFP Baudrate` gesetzt statisch verwendet.

Die minimale dynamische Baudrate hat einen Wertebereich von 400000 bis 2000000 Baud.

Standardmäßig ist die dynamische Baudrate aktiviert und die minimale dynamische Baudrate ist 400000.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get SPITFP Baudrate Config',
'elements': [('Enable Dynamic Baudrate', 'bool', 1, 'out'),
             ('Minimum Dynamic Baudrate', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the baudrate config, see :func:`Set SPITFP Baudrate Config`.
""",
'de':
"""
Gibt die Baudratenkonfiguration zurück, siehe :func:`Set SPITFP Baudrate Config`.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set SPITFP Baudrate',
'elements': [('Baudrate', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Sets the baudrate for a the communication between Isolator Bricklet
and the connected Bricklet. The baudrate for communication between
Brick and Isolator Bricklet can be set through the API of the Brick.

The baudrate can be in the range 400000 to 2000000.

If you want to increase the throughput of Bricklets you can increase
the baudrate. If you get a high error count because of high
interference (see :func:`Get SPITFP Error Count`) you can decrease the
baudrate.

If the dynamic baudrate feature is enabled, the baudrate set by this
function corresponds to the maximum baudrate (see :func:`Set SPITFP Baudrate Config`).

Regulatory testing is done with the default baudrate. If CE compatibility
or similar is necessary in you applications we recommend to not change
the baudrate.

The default baudrate for all ports is 1400000.
""",
'de':
"""
Setzt die Baudrate für die Kommunikation zwischen Isolator Bricklet
und angeschlossenem Bricklet. Die Baudrate für die Kommunikation zwischen
Brick und Isolator Bricklet kann in der API des Bricks eingestellt werden.

Die Baudrate hat einen möglichen Wertebereich von 400000 bis 2000000.

Für einen höheren Durchsatz der Bricklets kann die Baudrate erhöht werden.
Wenn der Fehlerzähler auf Grund von lokaler Störeinstrahlung hoch ist
(siehe :func:`Get SPITFP Error Count`) kann die Baudrate verringert werden.

Wenn das Feature der dynamische Baudrate aktiviert ist, setzt diese Funktion
die maximale Baudrate (siehe :func:`Set SPITFP Baudrate Config`).

EMV Tests werden mit der Standardbaudrate durchgeführt. Falls eine
CE-Kompatibilität o.ä. in der Anwendung notwendig ist empfehlen wir die
Baudrate nicht zu ändern.

Die Standardbaudrate für alle Ports ist 1400000.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get SPITFP Baudrate',
'elements': [('Baudrate', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the baudrate, see :func:`Set SPITFP Baudrate`.
""",
'de':
"""
Gibt die Baudrate zurück, siehe :func:`Set SPITFP Baudrate`.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Isolator SPITFP Error Count',
'elements': [('Error Count ACK Checksum', 'uint32', 1, 'out'),
             ('Error Count Message Checksum', 'uint32', 1, 'out'),
             ('Error Count Frame', 'uint32', 1, 'out'),
             ('Error Count Overflow', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the error count for the communication between Isolator Bricklet and
the connected Bricklet. Call :func:`Get SPITFP Error Count` to get the
error count between Isolator Bricklet and Brick.

The errors are divided into

* ACK checksum errors,
* message checksum errors,
* framing errors and
* overflow errors.
""",
'de':
"""
Gibt die Anzahl der Fehler die während der Kommunikation zwischen Isolator Bricklet
und Bricklet aufgetreten sind zurück. Rufe :func:`Get SPITFP Error Count` um die
Anzahl der Fehler zwischen Isolator Bricklet und Brick zu bekommen.

Die Fehler sind aufgeteilt in

* ACK-Checksummen Fehler,
* Message-Checksummen Fehler,
* Framing Fehler und
* Overflow Fehler.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Statistics Callback Configuration',
'elements': [('Period', 'uint32', 1, 'in'),
             ('Value Has To Change', 'bool', 1, 'in')],
'since_firmware': [2, 0, 2],
'doc': ['ccf', {
'en':
"""
The period in ms is the period with which the :cb:`Statistics`
callback is triggered periodically. A value of 0 turns the callback off.

If the `value has to change`-parameter is set to true, the callback is only
triggered after the value has changed. If the value didn't change within the
period, the callback is triggered immediately on change.

If it is set to false, the callback is continuously triggered with the period,
independent of the value.

The default value is (0, false).
""",
'de':
"""
Die Periode in ms ist die Periode mit der der :cb:`Statistics`
Callback ausgelöst wird. Ein Wert von 0 schaltet den Callback ab.

Wenn der `value has to change`-Parameter auf True gesetzt wird, wird der
Callback nur ausgelöst, wenn der Wert sich im Vergleich zum letzten mal geändert
hat. Ändert der Wert sich nicht innerhalb der Periode, so wird der Callback
sofort ausgelöst, wenn der Wert sich das nächste mal ändert.

Wird der Parameter auf False gesetzt, so wird der Callback dauerhaft mit der
festen Periode ausgelöst unabhängig von den Änderungen des Werts.

Der Standardwert ist (0, false).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Statistics Callback Configuration',
'elements': [('Period', 'uint32', 1, 'out'),
             ('Value Has To Change', 'bool', 1, 'out')],
'since_firmware': [2, 0, 2],
'doc': ['ccf', {
'en':
"""
Returns the callback configuration as set by
:func:`Set Statistics Callback Configuration`.
""",
'de':
"""
Gibt die Callback-Konfiguration zurück, wie mittels
:func:`Set Statistics Callback Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Statistics',
'elements': [('Messages From Brick', 'uint32', 1, 'out'),
             ('Messages From Bricklet', 'uint32', 1, 'out'),
             ('Connected Bricklet Device Identifier', 'uint16', 1, 'out'),
             ('Connected Bricklet UID', 'string', 8, 'out')],
'since_firmware': [2, 0, 2],
'doc': ['c', {
'en':
"""
This callback is triggered periodically according to the configuration set by
:func:`Set Statistics Callback Configuration`.

The :word:`parameters` are the same as :func:`Get Statistics`.
""",
'de':
"""
Dieser Callback wird periodisch ausgelöst abhängig von der mittels
:func:`Set Statistics Callback Configuration` gesetzten Konfiguration

Die :word:`parameters` sind der gleiche wie :func:`Get Statistics`.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Statistics', 'statistics'), [(('Messages From Brick', 'Messages From Brick'), 'uint32', 1, None, None, None), (('Messages From Bricklet', 'Messages From Bricklet'), 'uint32', 1, None, None, None), (('Connected Bricklet Device Identifier', 'Connected Bricklet Device Identifier'), 'uint16', 1, None, None, None), (('Connected Bricklet UID', 'Connected Bricklet UID'), 'string', 8, None, None, None)], [])]
})

def statistics_channel(name_words, name_headless):
    return  {
        'id': name_words,
        'type': name_words,

        'getters': [{
            'packet': 'Get Statistics',
            'packet_params': [],
            'transform': 'new QuantityType<>(value.{}, SmartHomeUnits.ONE)'.format(name_headless)}],

        'callbacks': [{
            'packet': 'Statistics',
            'transform': 'new QuantityType<>({}, SmartHomeUnits.ONE)'.format(name_headless),
            'filter': 'true'}],

        'is_trigger_channel': False
    }

com['openhab'] = {
    'imports': oh_generic_channel_imports() + ['org.eclipse.smarthome.core.library.types.StringType'],
    'param_groups': oh_generic_channel_param_groups(),
    'params': [
        update_interval('Statistics', 'all statistics data')
    ],
    'init_code': """this.setStatisticsCallbackConfiguration(cfg.statisticsUpdateInterval, true);""",
    'channels': [
        statistics_channel('Messages From Brick', 'messagesFromBrick'),
        statistics_channel('Messages From Bricklet', 'messagesFromBricklet'),
        {
            'id': 'Connected Bricklet Device Name',
            'type': 'Connected Bricklet Device Name',

            'getters': [{
                'packet': 'Get Statistics',
                'packet_params': [],
                'transform': 'new StringType(Helper.getDeviceName(value.connectedBrickletDeviceIdentifier))'}],

            'callbacks': [{
                'packet': 'Statistics',
                'transform': 'new StringType(Helper.getDeviceName(connectedBrickletDeviceIdentifier))',
                'filter': 'true'}],

            'is_trigger_channel': False
        }, {
            'id': 'Connected Bricklet UID',
            'type': 'Connected Bricklet UID',

            'getters': [{
                'packet': 'Get Statistics',
                'packet_params': [],
                'transform': 'new StringType(value.connectedBrickletUID)'}],

            'callbacks': [{
                'packet': 'Statistics',
                'transform': 'new StringType(connectedBrickletUID)',
                'filter': 'true'}],

            'is_trigger_channel': False
        }
    ],
    'channel_types': [
        oh_generic_channel_type('Messages From Brick', 'Number:Dimensionless', 'Messages From Brick',
                    description='Messages passed through the Isolator from the controlling Brick.',
                    read_only=True,
                    pattern='%d'),
        oh_generic_channel_type('Messages From Bricklet', 'Number:Dimensionless', 'Messages From Bricklet',
                    description='Messages passed through the Isolator from the isolated Bricklet.',
                    read_only=True,
                    pattern='%d'),
        oh_generic_channel_type('Connected Bricklet Device Name', 'String', 'Connected Bricklet Device Name',
                     description='Device Name of the isolated Bricklet.',
                     read_only=True),
        oh_generic_channel_type('Connected Bricklet UID', 'String', 'Connected Bricklet UID',
                     description='UID of the isolated Bricklet.',
                     read_only=True),
    ]
}
