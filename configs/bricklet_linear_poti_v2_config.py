# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Linear Poti Bricklet 2.0 communication config

from commonconstants import THRESHOLD_OPTION_CONSTANTS
from commonconstants import add_callback_value_function

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 2139,
    'name': 'Linear Poti V2',
    'display_name': 'Linear Poti 2.0',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': '59mm linear potentiometer',
        'de': '59mm Linearpotentiometer'
    },
    'comcu': True,
    'released': False,
    'documented': False,
    'discontinued': False,
    'packets': [],
    'examples': []
}

position_doc = {
'en':
"""
Returns the position of the linear potentiometer. The value is
between 0 (slider down) and 100 (slider up).
""",
'de':
"""
Gibt die Position des Linearpotentiometers zurück. Der Wertebereich
ist von 0 (Schieberegler unten) und 100 (Schieberegler oben).
"""
}

add_callback_value_function(
    packets   = com['packets'],
    name      = 'Get Position',
    data_name = 'Position',
    data_type = 'uint8',
    doc       = position_doc
)

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Position', 'position'), [(('Position', 'Position'), 'uint8', 1, None, '°', None)], [])]
})

com['examples'].append({
'name': 'Callback',
'functions': [('callback', ('Position', 'position'), [(('Position', 'Position'), 'uint8', 1, None, '°', None)], None, None),
              ('callback_configuration', ('Position', 'position'), [], 250, False, 'x', [(0, 0)])]
})