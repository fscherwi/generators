# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Particulate Matter Bricklet communication config

from openhab_common import *

com = {
    'author': 'Matthias Bolte <matthias@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 2110,
    'name': 'Particulate Matter',
    'display_name': 'Particulate Matter',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Measures Particulate Matter concentration (PM1.0, PM2.5 and PM10)',
        'de': 'Misst Feinstaub concentration (PM1.0, PM2.5 und PM10)'
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
'name': 'Get PM Concentration',
'elements': [('PM10', 'uint16', 1, 'out'),
             ('PM25', 'uint16', 1, 'out'),
             ('PM100', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the particulate matter concentration in µg/m³, broken down as:

* PM\ :sub:`1.0`\ ,
* PM\ :sub:`2.5`\  and
* PM\ :sub:`10.0`\ .

If the sensor is disabled (see :func:`Set Enable`) then the last known good
values from the sensor are returned.

If you want to get the values periodically, it is recommended to use the
:cb:`PM Concentration` callback. You can set the callback configuration
with :func:`Set PM Concentration Callback Configuration`.
""",
'de':
"""
Gibt die Feinstaub-Konzentration in µg/m³ zurück, aufgeschlüsselt nach:

* PM\ :sub:`1.0`\ ,
* PM\ :sub:`2.5`\  und
* PM\ :sub:`10.0`\ .

Wenn der Sensor deaktiviert ist (siehe :func:`Set Enable`), dann wird weiterhin
der letzte Sensorwert zurückgegeben.

Wenn die Werte periodisch benötigt werden, kann auch der :cb:`PM Concentration` Callback
verwendet werden. Der Callback wird mit der Funktion
:func:`Set PM Concentration Callback Configuration` konfiguriert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get PM Count',
'elements': [('Greater03um', 'uint16', 1, 'out'),
             ('Greater05um', 'uint16', 1, 'out'),
             ('Greater10um', 'uint16', 1, 'out'),
             ('Greater25um', 'uint16', 1, 'out'),
             ('Greater50um', 'uint16', 1, 'out'),
             ('Greater100um', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the number of particulates in 100 ml of air, broken down by their
diameter:

* greater 0.3µm,
* greater 0.5µm,
* greater 1.0µm,
* greater 2.5µm,
* greater 5.0µm and
* greater 10.0µm.

If the sensor is disabled (see :func:`Set Enable`) then the last known good
value from the sensor is returned.

If you want to get the values periodically, it is recommended to use the
:cb:`PM Count` callback. You can set the callback configuration
with :func:`Set PM Count Callback Configuration`.
""",
'de':
"""
Gibt die Anzahl der Feinstaub-Teilchen in 100ml Luft zurück, aufgeschlüsselt
nach deren Durchmesser:

* größer 0,3µm,
* größer 0,5µm,
* größer 1,0µm,
* größer 2,5µm,
* größer 5,0µm und
* größer 10,0µm.

Wenn der Sensor deaktiviert ist (siehe :func:`Set Enable`), dann wird weiterhin
der letzte Sensorwert zurückgegeben.

Wenn die Werte periodisch benötigt werden, kann auch der :cb:`PM Count` Callback
verwendet werden. Der Callback wird mit der Funktion
:func:`Set PM Count Callback Configuration` konfiguriert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Enable',
'elements': [('Enable', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Enables/Disables the fan and the laser diode of the sensors. The sensor is
enabled by default.

The sensor takes about 30 seconds after it is enabled to settle and produce stable
values.

The laser diode has a lifetime of about 8000 hours. If you want to measure in
an interval with a long idle time (e.g. hourly) you should turn the
laser diode off between the measurements.
""",
'de':
"""
Aktiviert/deaktiviert den Lüfter und die Laserdiode des Sensors. Der Sensor
ist standardmäßig aktiv.

Der Sensor benötigt ca. 30 Sekunden nach der Aktivierung um sich einzuschwingen
und stabile Werte zu produzieren.

Die Lebensdauer der Laserdiode beträgt ca. 8000 Stunden. Wenn Messungen in
größeren Abständen stattfinden sollen (z.B. stündlich) lohnt es sich die
Laserdiode zwischen den Messungen auszumachen.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Enable',
'elements': [('Enable', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the state of the sensor as set by :func:`Set Enable`.
""",
'de':
"""
Gibt den Zustand des Sensors zurück, wie von :func:`Set Enable` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Sensor Info',
'elements': [('Sensor Version', 'uint8', 1, 'out'),
             ('Last Error Code', 'uint8', 1, 'out'),
             ('Framing Error Count', 'uint8', 1, 'out'),
             ('Checksum Error Count', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns information about the sensor:

* the sensor version number,
* the last error code reported by the sensor (0 means no error) and
* the number of framing and checksum errors that occurred in the communication
  with the sensor.
""",
'de':
"""
Gibt Informationen über den Sensor zurück:

* die Versionsnummer des Sensors,
* den letzten Fehlercode den der Sensor gemeldet (0 bedeute kein Fehler) hat,
* die Anzahl der Framing und Prüfsummenfehler die in der Kommunikation mit dem
  Sensor aufgetreten sind.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set PM Concentration Callback Configuration',
'elements': [('Period', 'uint32', 1, 'in'),
             ('Value Has To Change', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
The period in ms is the period with which the :cb:`PM Concentration`
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
Die Periode in ms ist die Periode mit der der :cb:`PM Concentration`
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
'name': 'Get PM Concentration Callback Configuration',
'elements': [('Period', 'uint32', 1, 'out'),
             ('Value Has To Change', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the callback configuration as set by
:func:`Set PM Concentration Callback Configuration`.
""",
'de':
"""
Gibt die Callback-Konfiguration zurück, wie mittels
:func:`Set PM Concentration Callback Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set PM Count Callback Configuration',
'elements': [('Period', 'uint32', 1, 'in'),
             ('Value Has To Change', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
The period in ms is the period with which the :cb:`PM Count` callback
is triggered periodically. A value of 0 turns the callback off.

If the `value has to change`-parameter is set to true, the callback is only
triggered after the value has changed. If the value didn't change within the
period, the callback is triggered immediately on change.

If it is set to false, the callback is continuously triggered with the period,
independent of the value.

The default value is (0, false).
""",
'de':
"""
Die Periode in ms ist die Periode mit der der :cb:`PM Count` Callback
ausgelöst wird. Ein Wert von 0 schaltet den Callback ab.

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
'name': 'Get PM Count Callback Configuration',
'elements': [('Period', 'uint32', 1, 'out'),
             ('Value Has To Change', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the callback configuration as set by
:func:`Set PM Count Callback Configuration`.
""",
'de':
"""
Gibt die Callback-Konfiguration zurück, wie mittels
:func:`Set PM Count Callback Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'PM Concentration',
'elements': [('PM10', 'uint16', 1, 'out'),
             ('PM25', 'uint16', 1, 'out'),
             ('PM100', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically according to the configuration set by
:func:`Set PM Concentration Callback Configuration`.

The :word:`parameters` are the same as :func:`Get PM Concentration`.
""",
'de':
"""
Dieser Callback wird periodisch ausgelöst abhängig von der mittels
:func:`Set PM Concentration Callback Configuration` gesetzten Konfiguration

Die :word:`parameters` sind der gleiche wie :func:`Get PM Concentration`.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'PM Count',
'elements': [('Greater03um', 'uint16', 1, 'out'),
             ('Greater05um', 'uint16', 1, 'out'),
             ('Greater10um', 'uint16', 1, 'out'),
             ('Greater25um', 'uint16', 1, 'out'),
             ('Greater50um', 'uint16', 1, 'out'),
             ('Greater100um', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically according to the configuration set by
:func:`Set PM Count Callback Configuration`.

The :word:`parameters` are the same as :func:`Get PM Count`.
""",
'de':
"""
Dieser Callback wird periodisch ausgelöst abhängig von der mittels
:func:`Set PM Count Callback Configuration` gesetzten Konfiguration

Die :word:`parameters` sind der gleiche wie :func:`Get PM Count`.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get PM Concentration', 'PM concentration'), [(('PM10', 'PM 1.0'), 'uint16', 1, None, 'µg/m³', None), (('PM25', 'PM 2.5'), 'uint16', 1, None, 'µg/m³', None), (('PM100', 'PM 10.0'), 'uint16', 1, None, 'µg/m³', None)], [])]
})

com['examples'].append({
'name': 'Callback',
'functions': [('callback', ('PM Concentration', 'PM concentration'), [(('PM10', 'PM 1.0'), 'uint16', 1, None, 'µg/m³', None), (('PM25', 'PM 2.5'), 'uint16', 1, None, 'µg/m³', None), (('PM100', 'PM 10.0'), 'uint16', 1, None, 'µg/m³', None)], None, None),
              ('callback_configuration', ('PM Concentration', 'PM concentration'), [], 1000, False, None, [])]
})

def concentration_channel(size):
    return {
        'id': 'PM{} Concentration'.format(size),
        'type': 'PM{} Concentration'.format(size),
        'init_code':"""this.setPMConcentrationCallbackConfiguration(cfg.pmConcentrationUpdateInterval, true);""",
        'dispose_code': """this.setPMConcentrationCallbackConfiguration(0, true);""",
        'getters': [{
            'packet': 'Get PM Concentration',
            'packet_params': [],
            'transform': 'new QuantityType<>(value.pm{}{{divisor}}, {{unit}})'.format(size)}],

        'callbacks': [{
            'packet': 'PM Concentration',
            'transform': 'new QuantityType<>(pm{}{{divisor}}, {{unit}})'.format(size)}],

        'java_unit': 'SmartHomeUnits.MICROGRAM_PER_CUBICMETRE',
        'divisor': 1,
        'is_trigger_channel': False
    }

def concentration_channel_type(size):
    return oh_generic_channel_type('PM{} Concentration'.format(size), 'Number:Density', 'PM {:.1f} Concentration'.format(size / 10),
                     description='The particulate matter {:.1f} concentration. If the sensor is disabled then the last known good values from the sensor are returned.'.format(size / 10),
                     read_only=True,
                     pattern='%d %unit%')

def count_channel(size):
    return {
        'id': 'Part Count {}'.format(size),
        'type': 'Part Count {}'.format(size),
        'init_code':"""this.setPMCountCallbackConfiguration(cfg.pmCountUpdateInterval, true);""",
        'dispose_code': """this.setPMCountCallbackConfiguration(0, true);""",
        'getters': [{
            'packet': 'Get PM Count',
            'packet_params': [],
            'transform': 'new QuantityType<>(value.greater{:02}um{{divisor}}, {{unit}})'.format(size)}],

        'callbacks': [{
            'packet': 'PM Count',
            'transform': 'new QuantityType<>(greater{:02}um{{divisor}}, {{unit}})'.format(size)}],

        'java_unit': 'SmartHomeUnits.ONE',
        'divisor': 1,
        'is_trigger_channel': False
    }
def count_channel_type(size):
    return oh_generic_channel_type('Part Count {}'.format(size), 'Number:Dimensionless', 'Particulates Greater {:.1f}µm'.format(size / 10),
                     description='The number of particulates greater than {:.1f}µm in 100 ml of air. If the sensor is disabled then the last known good values from the sensor are returned.'.format(size / 10),
                     read_only=True,
                     pattern='%d')

com['openhab'] = {
    'imports': oh_generic_channel_imports() + ['org.eclipse.smarthome.core.library.types.OnOffType'],
    'param_groups': oh_generic_channel_param_groups(),
    'params': [{
            'name': 'PM Concentration Update Interval',
            'type': 'integer',
            'unit': 'ms',
            'label': 'PM Concentration Update Interval',
            'description': 'Specifies the update interval for all PM concentration data in milliseconds. A value of 0 disables automatic updates.',
            'default': 1000,
            'groupName': 'update_intervals'
        }, {
            'name': 'PM Count Update Interval',
            'type': 'integer',
            'unit': 'ms',
            'label': 'PM Count Update Interval',
            'description': 'Specifies the update interval for all PM count data in milliseconds. A value of 0 disables automatic updates.',
            'default': 1000,
            'groupName': 'update_intervals'
        }],
    'channels': [concentration_channel(i) for i in [10, 25, 100]] +
                [count_channel(i) for i in [3, 5, 10, 25, 50, 100]] + [
                {
                    'id': 'Sensor Enabled',
                    'label': 'Sensor Enabled',
                    'description': 'Enables/Disables the fan and the laser diode of the sensors.<br/><br/>The sensor takes about 30 seconds after it is enabled to settle and produce stable values.<br/><br/>The laser diode has a lifetime of about 8000 hours. If you want to measure in an interval with a long idle time (e.g. hourly) you should turn the laser diode off between the measurements.',

                    'type': 'Sensor Enabled',

                    'getters': [{
                        'packet': 'Get Enable',
                        'transform': 'value ? OnOffType.ON : OnOffType.OFF'}],

                    'setters': [{
                        'packet': 'Set Enable',
                        'packet_params': ['cmd == OnOffType.ON']}],
                    'setter_command_type': "OnOffType",
                }
                ],
    'channel_types':
        [concentration_channel_type(i) for i in [10, 25, 100]] +
        [count_channel_type(i) for i in [3, 5, 10, 25, 50, 100]] +
        [oh_generic_channel_type('Sensor Enabled', 'Switch', 'NOT USED',
                        description='NOT USED')]
}

