# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Industrial Counter Bricklet communication config

from openhab_common import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 293,
    'name': 'Industrial Counter',
    'display_name': 'Industrial Counter',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': '4 channel counter up to 4MHz',
        'de': '4-Kanal Zähler bis zu 4MHz'
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

com['constant_groups'].append({
'name': 'Channel',
'type': 'uint8',
'constants': [('0', 0),
              ('1', 1),
              ('2', 2),
              ('3', 3)]
})

com['constant_groups'].append({
'name': 'Count Edge',
'type': 'uint8',
'constants': [('Rising', 0),
              ('Falling', 1),
              ('Both', 2)]
})

com['constant_groups'].append({
'name': 'Count Direction',
'type': 'uint8',
'constants': [('Up', 0),
              ('Down', 1),
              ('External Up', 2),
              ('External Down', 3)]
})

com['constant_groups'].append({
'name': 'Duty Cycle Prescaler',
'type': 'uint8',
'constants': [('1', 0),
              ('2', 1),
              ('4', 2),
              ('8', 3),
              ('16', 4),
              ('32', 5),
              ('64', 6),
              ('128', 7),
              ('256', 8),
              ('512', 9),
              ('1024', 10),
              ('2048', 11),
              ('4096', 12),
              ('8192', 13),
              ('16384', 14),
              ('32768', 15)]
})

com['constant_groups'].append({
'name': 'Frequency Integration Time',
'type': 'uint8',
'constants': [('128 MS', 0),
              ('256 MS', 1),
              ('512 MS', 2),
              ('1024 MS', 3),
              ('2048 MS', 4),
              ('4096 MS', 5),
              ('8192 MS', 6),
              ('16384 MS', 7),
              ('32768 MS', 8)]
})

com['constant_groups'].append({
'name': 'Channel LED Config',
'type': 'uint8',
'constants': [('Off', 0),
              ('On', 1),
              ('Show Heartbeat', 2),
              ('Show Channel Status', 3)]
})

com['packets'].append({
'type': 'function',
'name': 'Get Counter',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Counter', 'int64', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current counter value for the given channel.
""",
'de':
"""
Gibt den aktuellen Zählerstand für den gegebenen Kanal zurück.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get All Counter',
'elements': [('Counter', 'int64', 4, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current counter values for all four channels.
""",
'de':
"""
Gibt die Zählerstände für alle vier Kanäle zurück.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Counter',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Counter', 'int64', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the counter value for the given channel.

The default value for the counters on startup is 0.
""",
'de':
"""
Setzt den Zählerstand für den gegebenen Kanal.

Der Standardwert für alle Zähler nach dem Start ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set All Counter',
'elements': [('Counter', 'int64', 4, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the counter values for all four channels.

The default value for the counters on startup is 0.
""",
'de':
"""
Setzt die Zählerstände für alle vier Kanäle.

Der Standardwert für die Zähler nach dem Starten ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Signal Data',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Duty Cycle', 'uint16', 1, 'out'),
             ('Period', 'uint64', 1, 'out'),
             ('Frequency', 'uint32', 1, 'out'),
             ('Value', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the signal data (duty cycle, period, frequency and value) for the
given channel.

The units are:

* Duty Cycle: 1/100 %
* Period: ns
* Frequency: mHz (1/1000 Hz)
* Value: true = high, false = low
""",
'de':
"""
Gibt die Signaldaten (Tastverhältnis, Periode, Frequenz und Status) für den
gegebenen Kanal.

Die Einheiten sind:

* Tastverhältnis: 1/100 %
* Periode: ns
* Frequenz: mHz (1/1000 Hz)
* Wert: true = high, false = low
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get All Signal Data',
'elements': [('Duty Cycle', 'uint16', 4, 'out'),
             ('Period', 'uint64', 4, 'out'),
             ('Frequency', 'uint32', 4, 'out'),
             ('Value', 'bool', 4, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the signal data (duty cycle, period, frequency and value) for all four
channels.

The units are:

* Duty Cycle: 1/100 %
* Period: ns
* Frequency: mHz (1/1000 Hz)
* Value: true = high, false = low
""",
'de':
"""
Gibt die Signaldaten (Tastverhältnis, Periode, Frequenz und Status) für alle
vier Kanäle zurück.

Die Einheiten sind:

* Tastverhältnis: 1/100 %
* Periode: ns
* Frequenz: mHz (1/1000 Hz)
* Wert: true = high, false = low
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Counter Active',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Active', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Activates/deactivates the counter of the given channel.

true = activate, false = deactivate.

By default all channels are activated.
""",
'de':
"""
Aktiviert/Deaktiviert den Zähler für den gegebenen Kanal.

true = aktivieren, false = deaktivieren.

Standardmäßig sind alle Kanäle aktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set All Counter Active',
'elements': [('Active', 'bool', 4, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Activates/deactivates the counter of all four channels.

true = activate, false = deactivate.

By default all channels are activated.
""",
'de':
"""
Aktiviert/Deaktiviert den Zähler für alle vier Kanäle.

true = aktivieren, false = deaktivieren.

Standardmäßig sind alle Kanäle aktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Counter Active',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Active', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the activation state of the given channel.

true = activated, false = deactivated.
""",
'de':
"""
Gibt den Zustand (aktiviert/deaktiviert) des gegebenen Zähler zurück.

true = aktiviert, false = deaktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get All Counter Active',
'elements': [('Active', 'bool', 4, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the activation state of all four channels.

true = activated, false = deactivated.
""",
'de':
"""
Gibt den Zustand (aktiviert/deaktiviert) aller vier Zähler zurück.

true = aktiviert, false = deaktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Counter Configuration',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Count Edge', 'uint8', 1, 'in', {'constant_group': 'Count Edge'}),
             ('Count Direction', 'uint8', 1, 'in', {'constant_group': 'Count Direction'}),
             ('Duty Cycle Prescaler', 'uint8', 1, 'in', {'constant_group': 'Duty Cycle Prescaler'}),
             ('Frequency Integration Time', 'uint8', 1, 'in', {'constant_group': 'Frequency Integration Time'})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the counter configuration for the given channel.

* Count Edge: Counter can count on rising, falling or both edges. Default is rising.
* Count Direction: Counter can count up or down. You can also use
  another channel as direction input, see
  `here <https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Industrial_Counter.html#external-count-direction>`__
  for details. Default is up.
* Duty Cycle Prescaler: Sets a divider for the internal clock. See
  `here <https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Industrial_Counter.html#duty-cycle-prescaler-and-frequency-integration-time>`__
  for details. Default is 1.
* Frequency Integration Time: Sets the integration time for the
  frequency measurement. See
  `here <https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Industrial_Counter.html#duty-cycle-prescaler-and-frequency-integration-time>`__
  for details. Default is 1024ms.
""",
'de':
"""
Setzt die Zähler-Konfiguration für den gegebenen Kanal.

* Zählflanke: Der Zähler kann bei der steigenden, fallenden oder beiden Flanken zählen. Standardwert ist steigend.
* Zählrichtung: Der Zähler kann hoch- oder runterzählen. Es kann auch ein weiterer
  Kanal als Richtungseingang genutzt werden. Siehe
  `hier <https://www.tinkerforge.com/de/doc/Hardware/Bricklets/Industrial_Counter.html#external-count-direction>`__
  für weitere Details. Standardwert ist hochzählend.
* Tastverhältnis Prescaler: Setzt einen Teiler für die interne Clock. Siehe
  `hier <https://www.tinkerforge.com/de/doc/Hardware/Bricklets/Industrial_Counter.html#duty-cycle-prescaler-und-frequency-integration-time>`__
  für weitere Details. Standardwert ist 1.
* Frequenz-Integration: Setzt die Integrationszeit für die Frequenzmessung. Siehe
  `hier <https://www.tinkerforge.com/de/doc/Hardware/Bricklets/Industrial_Counter.html#duty-cycle-prescaler-und-frequency-integration-time>`__
  für weitere Details. Standardwert ist 1024ms.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Counter Configuration',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Count Edge', 'uint8', 1, 'out', {'constant_group': 'Count Edge'}),
             ('Count Direction', 'uint8', 1, 'out', {'constant_group': 'Count Direction'}),
             ('Duty Cycle Prescaler', 'uint8', 1, 'out', {'constant_group': 'Duty Cycle Prescaler'}),
             ('Frequency Integration Time', 'uint8', 1, 'out', {'constant_group': 'Frequency Integration Time'})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the counter configuration as set by :func:`Set Counter Configuration`.
""",
'de':
"""
Gibt die Zähler-Konfiguration zurück, wie Sie mittels
:func:`Set Counter Configuration` gesetzt wurde.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set All Counter Callback Configuration',
'elements': [('Period', 'uint32', 1, 'in'),
             ('Value Has To Change', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
The period in ms is the period with which the :cb:`All Counter`
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
Die Periode in ms ist die Periode mit der der :cb:`All Counter`
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
'name': 'Get All Counter Callback Configuration',
'elements': [('Period', 'uint32', 1, 'out'),
             ('Value Has To Change', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the callback configuration as set by
:func:`Set All Counter Callback Configuration`.
""",
'de':
"""
Gibt die Callback-Konfiguration zurück, wie mittels
:func:`Set All Counter Callback Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set All Signal Data Callback Configuration',
'elements': [('Period', 'uint32', 1, 'in'),
             ('Value Has To Change', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
The period in ms is the period with which the :cb:`All Signal Data`
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
Die Periode in ms ist die Periode mit der der :cb:`All Signal Data`
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
'name': 'Get All Signal Data Callback Configuration',
'elements': [('Period', 'uint32', 1, 'out'),
             ('Value Has To Change', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the callback configuration as set by
:func:`Set All Signal Data Callback Configuration`.
""",
'de':
"""
Gibt die Callback-Konfiguration zurück, wie mittels
:func:`Set All Signal Data Callback Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Channel LED Config',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Config', 'uint8', 1, 'in', {'constant_group': 'Channel LED Config'})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Each channel has a corresponding LED. You can turn the LED off, on or show a
heartbeat. You can also set the LED to "Channel Status". In this mode the
LED is on if the channel is high and off otherwise.

By default all channel LEDs are configured as "Channel Status".
""",
'de':
"""
Jeder Kanal hat eine dazugehörige LED. Die LEDs können individuell an- oder
ausgeschaltet werden. Zusätzlich kann ein Heartbeat oder der Kanalstatus
angezeigt werden. Falls Kanalstatus gewählt wird ist die LED an wenn
ein High-Signal am Kanal anliegt und sonst aus.

Standardmäßig sind die LEDs für alle Kanäle auf Kanalstatus konfiguriert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Channel LED Config',
'elements': [('Channel', 'uint8', 1, 'in', {'constant_group': 'Channel'}),
             ('Config', 'uint8', 1, 'out', {'constant_group': 'Channel LED Config'})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the channel LED configuration as set by :func:`Set Channel LED Config`
""",
'de':
"""
Gibt die Kanal-LED-Konfiguration zurück, wie von :func:`Set Channel LED Config` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'All Counter',
'elements': [('Counter', 'int64', 4, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically according to the configuration set by
:func:`Set All Counter Callback Configuration`.

The :word:`parameters` are the same as :func:`Get All Counter`.
""",
'de':
"""
Dieser Callback wird periodisch ausgelöst abhängig von der mittels
:func:`Set All Counter Callback Configuration` gesetzten Konfiguration

Die :word:`parameters` sind der gleiche wie :func:`Get All Counter`.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'All Signal Data',
'elements': [('Duty Cycle', 'uint16', 4, 'out'),
             ('Period', 'uint64', 4, 'out'),
             ('Frequency', 'uint32', 4, 'out'),
             ('Value', 'bool', 4, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically according to the configuration set by
:func:`Set All Signal Data Callback Configuration`.

The :word:`parameters` are the same as :func:`Get All Signal Data`.
""",
'de':
"""
Dieser Callback wird periodisch ausgelöst abhängig von der mittels
:func:`Set All Signal Data Callback Configuration` gesetzten Konfiguration

Die :word:`parameters` sind der gleiche wie :func:`Get All Signal Data`.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Counter', 'counter from channel 0'), [(('Counter', 'Counter (Channel 0)'), 'int64', 1, None, None, None)], [('uint8:constant', 0)]),
              ('getter', ('Get Signal Data', 'signal data from channel 0'), [(('Duty Cycle', 'Duty Cycle (Channel 0)'), 'uint16', 1, 100.0, '%', None), (('Period', 'Period (Channel 0)'), 'uint64', 1, None, 'ns', None), (('Frequency', 'Frequency (Channel 0)'), 'uint32', 1, 1000.0, 'Hz', None), (('Value', 'Value (Channel 0)'), 'bool', 1, None, None, None)], [('uint8:constant', 0)])]
})

# FIXME: add all-counter / all-signal-data callback example


def signal_data_channel(idx, data_words, data_headless, divisor, java_unit):
    return {
        'predicate': 'cfg.enableChannel{}'.format(idx),
        'id': '{} {}'.format(data_words, idx),
        'label': 'Channel {} - {}'.format(idx, data_words),
        'type': data_words,

        'getters': [{
            'packet': 'Get Signal Data',
            'packet_params': [str(idx)],
            'transform': 'new QuantityType<>(value.{}{{divisor}}, {{unit}})'.format(data_headless)
        }],
        'callbacks': [{
                'packet': 'All Signal Data',
                'transform': 'new QuantityType<>({}[{}]{{divisor}}, {{unit}})'.format(data_headless, idx)
        }],

        'java_unit': java_unit,
        'divisor': divisor
    }

def value_channel(idx):
    return {
        'predicate': 'cfg.enableChannel{}'.format(idx),
        'id': 'Value {}'.format(idx),
        'label': 'Channel {} - Value'.format(idx),
        'type': 'Value',

        'getters': [{
            'packet': 'Get Signal Data',
            'packet_params': [str(idx)],
            'transform': 'value.value ? OnOffType.ON : OnOffType.OFF'
        }],
        'callbacks': [{
                'packet': 'All Signal Data',
                'transform': 'value[{}] ? OnOffType.ON : OnOffType.OFF'.format(idx)
        }],
    }


def counter_channel(idx):
    return {
            'predicate': 'cfg.enableChannel{}'.format(idx),
            'id': 'Counter Channel {0}'.format(idx),
            'type': 'Counter',
            'label': 'Channel {0} - Counter'.format(idx),

            'init_code':"""this.setCounterConfiguration({0}, channelCfg.countEdge, channelCfg.countDirection, channelCfg.dutyCyclePrescaler, channelCfg.frequencyIntegrationTime);
            this.setChannelLEDConfig({0}, channelCfg.channelLEDConfiguration);""".format(idx),

            'getters': [{
                'packet': 'Get Counter',
                'packet_params': [str(idx)],
                'transform': 'new QuantityType<>(value, {unit})'
            }],
            'callbacks': [{
                'packet': 'All Counter',
                'transform': 'new QuantityType<>(counter[{}], {{unit}})'.format(idx)
            }],
            'setters': [{
                'packet': 'Set Counter',
                'packet_params': [str(idx), 'cmd.longValue()']
            }],
            'setter_command_type': 'Number',

            'java_unit': 'SmartHomeUnits.ONE',
            'is_trigger_channel': False
        }

def enable_config(idx):
    return {
            'name': 'Enable Channel {}'.format(idx),
            'type': 'boolean',
            'default': 'true',

            'label': 'Enable Channel {}'.format(idx),
            'description': 'Activates/deactivates the counter of channel {}.'.format(idx),
        }

channels = [counter_channel(i) for i in range(0, 4)]
channels += [signal_data_channel(i, 'Duty Cycle', 'dutyCycle', 100.0, 'SmartHomeUnits.PERCENT') for i in range(0, 4)]
channels += [signal_data_channel(i, 'Period', 'period', 1e9, 'SmartHomeUnits.SECOND') for i in range(0, 4)]
channels += [signal_data_channel(i, 'Frequency', 'frequency', 1000.0, 'SmartHomeUnits.HERTZ') for i in range(0, 4)]
channels += [value_channel(i) for i in range(0, 4)]

com['openhab'] = {
    'imports': oh_generic_channel_imports() + ['org.eclipse.smarthome.core.library.types.OnOffType', 'org.eclipse.smarthome.core.library.types.StringType'],
    'params': [enable_config(i) for i in range(0, 4)] + [update_interval('Counter', 'all counters'), update_interval('Signal Data', 'all signal data')],
    'init_code': """this.setAllCounterCallbackConfiguration(cfg.counterUpdateInterval, true);
    this.setAllSignalDataCallbackConfiguration(cfg.signalDataUpdateInterval, true);""",
    'dispose_code': """this.setAllCounterCallbackConfiguration(0, true);
    this.setAllSignalDataCallbackConfiguration(0, true);""",
    'channels': channels,
    'channel_types': [
        oh_generic_channel_type('Duty Cycle', 'Number:Dimensionless', 'NOT USED',
                     description='The signal duty cycle.',
                     min_=0,
                     max_=100,
                     read_only=True),
        oh_generic_channel_type('Period', 'Number:Time', 'NOT USED',
                     description='The signal period',
                     read_only=False),
        oh_generic_channel_type('Frequency', 'Number:Frequency', 'NOT USED',
                     description='The signal frequency.',
                     read_only=True),
        oh_generic_channel_type('Value', 'Switch', 'NOT USED',
                     description='The signal value',
                     read_only=False),
        oh_generic_channel_type('Counter', 'Number:Dimensionless', 'Counter',
            description='The current counter value for the given channel.',
            read_only=False,
            params=[{
                'name': 'Count Edge',
                'type': 'integer',
                'options': [('Rising', 0),
                            ('Falling', 1),
                            ('Both', 2)],
                'limitToOptions': 'true',
                'default': '0',

                'label': 'Count Edge',
                'description': 'Counter can count on rising, falling or both edges.',
            }, {
                'name': 'Count Direction',
                'type': 'integer',
                'options': [('Up', 0),
                            ('Down', 1),
                            ('External Up', 2),
                            ('External Down', 3)],
                'limitToOptions': 'true',
                'default': '0',

                'label': 'Count Direction',
                'description': 'Counter can count up or down. You can also use another channel as direction input: Channel 0 additionally supports to use the input of channel 2 as direction. You can configure channel 0 to count up if the value of channel 2 is high and down if the value is low and the other way around. Additionally channel 3 can use channel 1 as direction input in the same manner.',
            }, {
                'name': 'Duty Cycle Prescaler',
                'type': 'integer',
                'options': [('1', 0),
                            ('2', 1),
                            ('4', 2),
                            ('8', 3),
                            ('16', 4),
                            ('32', 5),
                            ('64', 6),
                            ('128', 7),
                            ('256', 8),
                            ('512', 9),
                            ('1024', 10),
                            ('2048', 11),
                            ('4096', 12),
                            ('8192', 13),
                            ('16384', 14),
                            ('32768', 15)],
                'limitToOptions': 'true',
                'default': '0',

                'label': 'Duty Cycle Prescaler',
                'description': 'Sets a divider for the internal clock. See <a href=\\\"https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Industrial_Counter.html#duty-cycle-prescaler-and-frequency-integration-time\\\">here</a> for details.',
            }, {
                'name': 'Frequency Integration Time',
                'type': 'integer',
                'options': [('128 MS', 0),
                            ('256 MS', 1),
                            ('512 MS', 2),
                            ('1024 MS', 3),
                            ('2048 MS', 4),
                            ('4096 MS', 5),
                            ('8192 MS', 6),
                            ('16384 MS', 7),
                            ('32768 MS', 8)],
                'limitToOptions': 'true',
                'default': '3',

                'label': 'Frequency Integration Time',
                'description': 'Sets the integration time for the frequency measurement. See <a href=\\\"https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Industrial_Counter.html#duty-cycle-prescaler-and-frequency-integration-time\\\">here</a> for details.',
            }, {
                'name': 'Channel LED Configuration',
                'type': 'integer',
                'options': [('Off', 0),
                            ('On', 1),
                            ('Show Heartbeat', 2),
                            ('Show Channel Status', 3)],
                'limitToOptions': 'true',
                'default': '3',

                'label': 'Channel LED Configuration',
                'description': 'Each channel has a corresponding LED. You can turn the LED off, on or show a heartbeat. You can also set the LED to \\\"Channel Status\\\". In this mode the LED is on if the channel is high and off otherwise.',
            },

            ])
    ]
}
