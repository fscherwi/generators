# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Analog Out Bricklet communication config

from openhab_common import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 220,
    'name': 'Analog Out',
    'display_name': 'Analog Out',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Generates configurable DC voltage between 0V and 5V',
        'de': 'Erzeugt konfigurierbare Gleichspannung zwischen 0V und 5V'
    },
    'released': True,
    'documented': True,
    'discontinued': True, # replaced by Analog Out Bricklet 2.0
    'features': [
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append({
'name': 'Mode',
'type': 'uint8',
'constants': [('Analog Value', 0),
              ('1k To Ground', 1),
              ('100k To Ground', 2),
              ('500k To Ground', 3)]
})

com['packets'].append({
'type': 'function',
'name': 'Set Voltage',
'elements': [('Voltage', 'uint16', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the voltage in mV. The possible range is 0V to 5V (0-5000).
Calling this function will set the mode to 0 (see :func:`Set Mode`).

The default value is 0 (with mode 1).
""",
'de':
"""
Setzt die Spannung in mV. Der mögliche Bereich ist 0V bis 5V (0-5000).
Dieser Funktionsaufruf setzt den Modus auf 0 (siehe :func:`Set Mode`).

Der Standardwert ist 0 (im Modus 1).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Voltage',
'elements': [('Voltage', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the voltage as set by :func:`Set Voltage`.
""",
'de':
"""
Gibt die Spannung zurück, wie von :func:`Set Voltage` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Mode',
'elements': [('Mode', 'uint8', 1, 'in', {'constant_group': 'Mode'})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the mode of the analog value. Possible modes:

* 0: Normal Mode (Analog value as set by :func:`Set Voltage` is applied)
* 1: 1k Ohm resistor to ground
* 2: 100k Ohm resistor to ground
* 3: 500k Ohm resistor to ground

Setting the mode to 0 will result in an output voltage of 0. You can jump
to a higher output voltage directly by calling :func:`Set Voltage`.

The default mode is 1.
""",
'de':
"""
Setzt den Modus des Analogwertes. Mögliche Modi:

* 0: normaler Modus (Analogwert, wie von :func:`Set Voltage` gesetzt, wird ausgegeben.)
* 1: 1k Ohm Widerstand gegen Masse
* 2: 100k Ohm Widerstand gegen Masse
* 3: 500k Ohm Widerstand gegen Masse

Ein setzten des Modus auf 0 resultiert in einer Ausgabespannung von 0. Es kann auf eine
höhere Ausgabespannung direkt gewechselt werden über einen Aufruf von :func:`Set Voltage`.

Der Standardmodus ist 1.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Mode',
'elements': [('Mode', 'uint8', 1, 'out', {'constant_group': 'Mode'})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the mode as set by :func:`Set Mode`.
""",
'de':
"""
Gibt den Modus zurück, wie von :func:`Set Mode` gesetzt.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('setter', 'Set Voltage', [('uint16', 3300)], 'Set output voltage to 3.3V', None)]
})

com['openhab'] = {
    'imports': oh_generic_channel_imports(),
    'param_groups': oh_generic_channel_param_groups(),
    'channels': [{
            'id': 'Voltage',
            'type': 'Voltage',
            'getters': [{
                'packet': 'Get {title_words}',
                'packet_params': [],
                'transform': 'new QuantityType<>(value{divisor}, {unit})'}],
            'setters':[{
                'packet': 'Set {title_words}',
                'packet_params': ['(int)Math.round(cmd.doubleValue() * 1000.0)'],
            }],
            'setter_command_type': 'Number',
            'setter_refreshs': [{
                'channel': 'Mode',
                'delay': 0
            }],

            'java_unit': 'SmartHomeUnits.VOLT',
            'divisor': 1000.0,
            'is_trigger_channel': False
        }, {
            'id': 'Mode',
            'type': 'Mode',
            'getters': [{
                'packet': 'Get {title_words}',
                'transform': 'new QuantityType(value, SmartHomeUnits.ONE)'}],
            'setters':[{
                'packet': 'Set {title_words}',
                'packet_params': ['cmd.shortValue()'],
            }],
            'setter_command_type': 'Number',
            'setter_refreshs': [{
                'channel': 'Voltage',
                'delay': 0
            }],
            'is_trigger_channel': False
        }
    ],
    'channel_types': [
         oh_generic_channel_type('Voltage', 'Number:ElectricPotential', 'Voltage',
                     description='The output voltage. The possible range is 0V to 5V. Sending a command to this channel will set the Mode to Analog Value.',
                     pattern='%.3f %unit%',
                     min_=0,
                     max_=5),
         {
            'id': 'Mode',
            'item_type': 'Number:Dimensionless',
            'label': 'Mode',
            'description': 'The mode of the output. Setting the mode to Analog Value will result in an output voltage of 0. You can jump to a higher output voltage directly by sending a command to the Voltage Channel.',
            'read_only': False,
            'pattern': '%d',
            'min': 0,
            'max': 7,
            'is_trigger_channel': False,
            'options':[('Analog Value', 0),
                        ('1k To Ground', 1),
                        ('100k To Ground', 2),
                        ('500k To Ground', 3)]
        },
    ]
}
