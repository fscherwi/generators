# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# IMU Brick 2.0 communication config

from openhab_common import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 3],
    'category': 'Brick',
    'device_identifier': 18,
    'name': 'IMU V2',
    'display_name': 'IMU 2.0',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Full fledged AHRS with 9 degrees of freedom',
        'de': 'Voll ausgestattetes AHRS mit 9 Freiheitsgraden'
    },
    'released': True,
    'documented': True,
    'discontinued': False,
    'features': [
        'brick_get_identity',
        'brick_status_led',
        'brick_reset',
        'brick_chip_temperature',
        'send_timeout_count',
        'eeprom_bricklet_host',
        'comcu_bricklet_host'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append({
'name': 'Magnetometer Rate',
'type': 'uint8',
'constants': [('2Hz', 0),
              ('6Hz', 1),
              ('8Hz', 2),
              ('10Hz', 3),
              ('15Hz', 4),
              ('20Hz', 5),
              ('25Hz', 6),
              ('30Hz', 7)]
})

com['constant_groups'].append({
'name': 'Gyroscope Range',
'type': 'uint8',
'constants': [('2000DPS', 0),
              ('1000DPS', 1),
              ('500DPS', 2),
              ('250DPS', 3),
              ('125DPS', 4)]
})

com['constant_groups'].append({
'name': 'Gyroscope Bandwidth',
'type': 'uint8',
'constants': [('523Hz', 0),
              ('230Hz', 1),
              ('116Hz', 2),
              ('47Hz', 3),
              ('23Hz', 4),
              ('12Hz', 5),
              ('64Hz', 6),
              ('32Hz', 7)]
})

com['constant_groups'].append({
'name': 'Accelerometer Range',
'type': 'uint8',
'constants': [('2G', 0),
              ('4G', 1),
              ('8G', 2),
              ('16G', 3)]
})

com['constant_groups'].append({
'name': 'Accelerometer Bandwidth',
'type': 'uint8',
'constants': [('7 81Hz', 0),
              ('15 63Hz', 1),
              ('31 25Hz', 2),
              ('62 5Hz', 3),
              ('125Hz', 4),
              ('250Hz', 5),
              ('500Hz', 6),
              ('1000Hz', 7)]
})

com['constant_groups'].append({
'name': 'Sensor Fusion',
'type': 'uint8',
'constants': [('Off', 0),
              ('On', 1),
              ('On Without Magnetometer', 2),
              ('On Without Fast Magnetometer Calibration', 3)]
})

com['packets'].append({
'type': 'function',
'name': 'Get Acceleration',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the calibrated acceleration from the accelerometer for the
x, y and z axis in 1/100 m/s².

If you want to get the acceleration periodically, it is recommended
to use the :cb:`Acceleration` callback and set the period with
:func:`Set Acceleration Period`.
""",
'de':
"""
Gibt die kalibrierten Beschleunigungen des Beschleunigungsmessers für die
X-, Y- und Z-Achse in 1/100 m/s².

Wenn die Beschleunigungen periodisch abgefragt werden soll, wird empfohlen
den :cb:`Acceleration` Callback zu nutzen und die Periode mit
:func:`Set Acceleration Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Magnetic Field',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the calibrated magnetic field from the magnetometer for the
x, y and z axis in 1/16 µT (Microtesla).

If you want to get the magnetic field periodically, it is recommended
to use the :cb:`Magnetic Field` callback and set the period with
:func:`Set Magnetic Field Period`.
""",
'de':
"""
Gibt das kalibrierte magnetische Feld des Magnetometers mit den X-, Y- und
Z-Komponenten in 1/16 µT zurück (Microtesla).

Wenn das magnetische Feld periodisch abgefragt werden soll, wird empfohlen
den :cb:`Magnetic Field` Callback zu nutzen und die Periode mit
:func:`Set Magnetic Field Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Angular Velocity',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the calibrated angular velocity from the gyroscope for the
x, y and z axis in 1/16 °/s.

If you want to get the angular velocity periodically, it is recommended
to use the :cb:`Angular Velocity` acallback nd set the period with
:func:`Set Angular Velocity Period`.
""",
'de':
"""
Gibt die kalibrierte Winkelgeschwindigkeiten des Gyroskops für die X-, Y- und
Z-Achse in 1/16 °/s zurück.

Wenn die Winkelgeschwindigkeiten periodisch abgefragt werden sollen, wird
empfohlen den :cb:`Angular Velocity` Callback zu nutzen und die Periode mit
:func:`Set Angular Velocity Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Temperature',
'elements': [('Temperature', 'int8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the temperature of the IMU Brick. The temperature is given in
°C. The temperature is measured in the core of the BNO055 IC, it is not the
ambient temperature
""",
'de':
"""
Gibt die Temperatur (in °C) des IMU Brick zurück. Die Temperatur wird im Kern
des BNO055 ICs gemessen, es handelt sich nicht um die Umgebungstemperatur.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Orientation',
'elements': [('Heading', 'int16', 1, 'out'),
             ('Roll', 'int16', 1, 'out'),
             ('Pitch', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current orientation (heading, roll, pitch) of the IMU Brick as
independent Euler angles in 1/16 degree. Note that Euler angles always
experience a `gimbal lock <https://en.wikipedia.org/wiki/Gimbal_lock>`__.
We recommend that you use quaternions instead, if you need the absolute
orientation.

The rotation angle has the following ranges:

* heading: 0° to 360°
* roll: -90° to +90°
* pitch: -180° to +180°

If you want to get the orientation periodically, it is recommended
to use the :cb:`Orientation` callback and set the period with
:func:`Set Orientation Period`.
""",
'de':
"""
Gibt die aktuelle Orientierung (Gier-, Roll-, Nickwinkel) des IMU Brick in
unabhängigen Eulerwinkeln (in 1/16 °) zurück. Zu beachten ist, dass Eulerwinkel
immer eine `kardanische Blockade <https://de.wikipedia.org/wiki/Gimbal_Lock>`__
erfahren. Wir empfehlen daher stattdessen Quaternionen zu verwenden, wenn die
absolute Lage im Raum bestimmt werden soll.

Die Rotationswinkel haben den folgenden Wertebereich:

* Gierwinkel: 0° bis 360°
* Rollwinkel: -90° bis +90°
* Nickwinkel: -180° bis +180°

Wenn die Orientierung periodisch abgefragt werden sollen, wird empfohlen den
:cb:`Orientation` Callback zu nutzen und die Periode mit
:func:`Set Orientation Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Linear Acceleration',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the linear acceleration of the IMU Brick for the
x, y and z axis in 1/100 m/s².

The linear acceleration is the acceleration in each of the three
axis of the IMU Brick with the influences of gravity removed.

It is also possible to get the gravity vector with the influence of linear
acceleration removed, see :func:`Get Gravity Vector`.

If you want to get the linear acceleration periodically, it is recommended
to use the :cb:`Linear Acceleration` callback and set the period with
:func:`Set Linear Acceleration Period`.
""",
'de':
"""
Gibt die lineare Beschleunigungen des IMU Brick für die
X-, Y- und Z-Achse in 1/100 m/s² zurück.

Die lineare Beschleunigung ist die Beschleunigung in jede der drei
Achsen. Der Einfluss von Erdbeschleunigung ist entfernt.

Es ist auch möglich einen Vektor der Erdbeschleunigung zu bekommen, siehe
:func:`Get Gravity Vector`

Wenn die Beschleunigungen periodisch abgefragt werden soll, wird empfohlen
den :cb:`Linear Acceleration` Callback zu nutzen und die Periode mit
:func:`Set Linear Acceleration Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Gravity Vector',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current gravity vector of the IMU Brick for the
x, y and z axis in 1/100 m/s².

The gravity vector is the acceleration that occurs due to gravity.
Influences of additional linear acceleration are removed.

It is also possible to get the linear acceleration with the influence
of gravity removed, see :func:`Get Linear Acceleration`.

If you want to get the gravity vector periodically, it is recommended
to use the :cb:`Gravity Vector` callback and set the period with
:func:`Set Gravity Vector Period`.
""",
'de':
"""
Gibt den Vektor der Erdbeschleunigung des IMU Brick für die
X-, Y- und Z-Achse in 1/100 m/s² zurück.

Die Erdbeschleunigung ist die Beschleunigung die auf Grund von Schwerkraft
entsteht. Einflüsse von linearen Beschleunigungen sind entfernt.

Es ist auch möglich die lineare Beschleunigung zu bekommen, siehe
:func:`Get Linear Acceleration`

Wenn die Erdbeschleunigungen periodisch abgefragt werden soll, wird empfohlen
den :cb:`Gravity Vector` Callback zu nutzen und die Periode mit
:func:`Set Gravity Vector Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Quaternion',
'elements': [('W', 'int16', 1, 'out'),
             ('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current orientation (w, x, y, z) of the IMU Brick as
`quaternions <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__.

You have to divide the returns values by 16383 (14 bit) to get
the usual range of -1.0 to +1.0 for quaternions.

If you want to get the quaternions periodically, it is recommended
to use the :cb:`Quaternion` callback and set the period with
:func:`Set Quaternion Period`.
""",
'de':
"""
Gibt die aktuelle Orientierung (w, x, y, z) des IMU Brick als
`Quaterinonen <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__ zurück.

Die zurückgegebenen Werte müssen mit 16383 (14 Bit) dividiert werden um
in den üblichen Wertebereich für Quaternionen (-1,0 bis +1,0) gebracht zu werden.

Wenn die Quaternionen periodisch abgefragt werden sollen, wird empfohlen den
:cb:`Quaternion` Callback zu nutzen und die Periode mit
:func:`Set Quaternion Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get All Data',
'elements': [('Acceleration', 'int16', 3, 'out'),
             ('Magnetic Field', 'int16', 3, 'out'),
             ('Angular Velocity', 'int16', 3, 'out'),
             ('Euler Angle', 'int16', 3, 'out'),
             ('Quaternion', 'int16', 4, 'out'),
             ('Linear Acceleration', 'int16', 3, 'out'),
             ('Gravity Vector', 'int16', 3, 'out'),
             ('Temperature', 'int8', 1, 'out'),
             ('Calibration Status', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Return all of the available data of the IMU Brick.

* acceleration in 1/100 m/s² (see :func:`Get Acceleration`)
* magnetic field in 1/16 µT (see :func:`Get Magnetic Field`)
* angular velocity in 1/16 °/s (see :func:`Get Angular Velocity`)
* Euler angles in 1/16 ° (see :func:`Get Orientation`)
* quaternion 1/16383 (see :func:`Get Quaternion`)
* linear acceleration 1/100 m/s² (see :func:`Get Linear Acceleration`)
* gravity vector 1/100 m/s² (see :func:`Get Gravity Vector`)
* temperature in 1 °C (see :func:`Get Temperature`)
* calibration status (see below)

The calibration status consists of four pairs of two bits. Each pair
of bits represents the status of the current calibration.

* bit 0-1: Magnetometer
* bit 2-3: Accelerometer
* bit 4-5: Gyroscope
* bit 6-7: System

A value of 0 means for "not calibrated" and a value of 3 means
"fully calibrated". In your program you should always be able to
ignore the calibration status, it is used by the calibration
window of the Brick Viewer and it can be ignored after the first
calibration. See the documentation in the calibration window for
more information regarding the calibration of the IMU Brick.

If you want to get the data periodically, it is recommended
to use the :cb:`All Data` callback and set the period with
:func:`Set All Data Period`.
""",
'de':
"""
Gibt alle Daten zurück die dem IMU Brick zur Verfügung stehen.

* Beschleunigung in 1/100 m/s² (see :func:`Get Acceleration`)
* Magnetfeld in 1/16 µT (see :func:`Get Magnetic Field`)
* Winkelgeschwindigkeit in 1/16 °/s (see :func:`Get Angular Velocity`)
* Eulerwinkel in 1/16 ° (see :func:`Get Orientation`)
* Quaternion 1/16383 (see :func:`Get Quaternion`)
* Lineare Beschleunigung 1/100 m/s² (see :func:`Get Linear Acceleration`)
* Erdbeschleunigungsvektor 1/100 m/s² (see :func:`Get Gravity Vector`)
* Temperatur in 1 °C (see :func:`Get Temperature`)
* Kalibrierungsstatus (siehe unten)

Der Kalibrierungsstatus besteht aus vier paaren von je zwei Bits. Jedes
Paar von Bits repräsentiert den Status der aktuellen Kalibrierung.

* Bit 0-1: Magnetometer
* Bit 2-3: Beschleunigungsmesser
* Bit 4-5: Gyroskop
* Bit 6-7: System

Ein Wert von 0 bedeutet "nicht kalibriert" und ein Wert von 3
bedeutet "vollständig kalibriert". Normalerweise kann der
Kalibrierungsstatus vollständig ignoriert werden. Er wird vom
Brick Viewer im Kalibrierungsfenster benutzt und nur für die
initiale Kalibrierung benötigt. Mehr Information zur Kalibrierung
des IMU Bricks gibt es im Kalibrierungsfenster.

Wenn die Daten periodisch abgefragt werden sollen, wird empfohlen den
:cb:`All Data` Callback zu nutzen und die Periode mit
:func:`Set All Data Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Leds On',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Turns the orientation and direction LEDs of the IMU Brick on.
""",
'de':
"""
Aktiviert die Orientierungs- und Richtungs-LEDs des IMU Brick.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Leds Off',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Turns the orientation and direction LEDs of the IMU Brick off.
""",
'de':
"""
Deaktiviert die Orientierungs- und Richtungs-LEDs des IMU Brick.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Are Leds On',
'elements': [('Leds', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns *true* if the orientation and direction LEDs of the IMU Brick
are on, *false* otherwise.
""",
'de':
"""
Gibt zurück ob die Orientierungs- und Richtungs-LEDs des IMU Brick aktiv sind.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Save Calibration',
'elements': [('Calibration Done', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
A call of this function saves the current calibration to be used
as a starting point for the next restart of continuous calibration
of the IMU Brick.

A return value of *true* means that the calibration could be used and
*false* means that it could not be used (this happens if the calibration
status is not "fully calibrated").

This function is used by the calibration window of the Brick Viewer, you
should not need to call it in your program.
""",
'de':
"""
Ein Aufruf dieser Funktion speichert die aktuelle Kalibrierung damit
sie beim nächsten Neustart des IMU Brick als Startpunkt für die
kontinuierliche Kalibrierung genutzt werden kann.

Ein Rückgabewert von *true* bedeutet das die Kalibrierung genutzt werden
konnte und *false* bedeutet das die Kalibrierung nicht genutzt werden
konnte (dies passiert wenn der Kalibrierungsstatus nicht "fully calibrated"
ist).

Diese Funktion wird vom Kalibrierungsfenster des Brick Viewer benutzt. Sie
sollte in einem normalen Benutzerprogramm nicht aufgerufen werden müssen.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Acceleration Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Acceleration` callback is triggered
periodically. A value of 0 turns the callback off.

The default value is 0.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Acceleration` Callback ausgelöst
wird. Ein Wert von 0 deaktiviert den Callback.

Der Standardwert ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Acceleration Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Acceleration Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Acceleration Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Magnetic Field Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Magnetic Field` callback is triggered
periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Magnetic Field` Callback ausgelöst
wird. Ein Wert von 0 deaktiviert den Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Magnetic Field Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Magnetic Field Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Magnetic Field Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Angular Velocity Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Angular Velocity` callback is
triggered periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Angular Velocity` Callback
ausgelöst wird. Ein Wert von 0 deaktiviert den Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Angular Velocity Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Angular Velocity Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Angular Velocity Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Temperature Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Temperature` callback is triggered
periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Temperature` Callback ausgelöst
wird. Ein Wert von 0 deaktiviert den Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Temperature Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Temperature Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Temperature Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Orientation Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Orientation` callback is triggered
periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Orientation` Callback ausgelöst
wird. Ein Wert von 0 deaktiviert den Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Orientation Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Orientation Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Orientation Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Linear Acceleration Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Linear Acceleration` callback is
triggered periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Linear Acceleration` Callback
ausgelöst wird. Ein Wert von 0 deaktiviert den Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Linear Acceleration Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Linear Acceleration Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Linear Acceleration Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Gravity Vector Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Gravity Vector` callback is triggered
periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Gravity Vector` Callback ausgelöst
wird. Ein Wert von 0 deaktiviert den Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Gravity Vector Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Gravity Vector Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Gravity Vector Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Quaternion Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Quaternion` callback is triggered
periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Quaternion` Callback ausgelöst
wird. Ein Wert von 0 deaktiviert den Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Quaternion Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Quaternion Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Quaternion Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set All Data Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`All Data` callback is triggered
periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`All Data` Callback ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get All Data Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set All Data Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set All Data Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Acceleration',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Acceleration Period`. The :word:`parameters` are the acceleration
for the x, y and z axis.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Acceleration Period`, ausgelöst. Die :word:`parameters` sind die
Beschleunigungen der X, Y und Z-Achse.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Magnetic Field',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Magnetic Field Period`. The :word:`parameters` are the magnetic
field for the x, y and z axis.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Magnetic Field Period`, ausgelöst. Die :word:`parameters` sind die
Magnetfeldkomponenten der X, Y und Z-Achse.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Angular Velocity',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Angular Velocity Period`. The :word:`parameters` are the angular
velocity for the x, y and z axis.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Angular Velocity Period`, ausgelöst. Die :word:`parameters` sind die
Winkelgeschwindigkeiten der X, Y und Z-Achse.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Temperature',
'elements': [('Temperature', 'int8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Temperature Period`. The :word:`parameter` is the temperature.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Temperature Period`, ausgelöst. Der :word:`parameter` ist die
Temperatur.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Linear Acceleration',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Linear Acceleration Period`. The :word:`parameters` are the
linear acceleration for the x, y and z axis.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Linear Acceleration Period`, ausgelöst. Die :word:`parameter` sind
die linearen Beschleunigungen der X, Y und Z-Achse.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Gravity Vector',
'elements': [('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Gravity Vector Period`. The :word:`parameters` gravity vector
for the x, y and z axis.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Gravity Vector Period`, ausgelöst. Die :word:`parameter` sind die
Erdbeschleunigungsvektor-Werte der X, Y und Z-Achse.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Orientation',
'elements': [('Heading', 'int16', 1, 'out'),
             ('Roll', 'int16', 1, 'out'),
             ('Pitch', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Orientation Period`. The :word:`parameters` are the orientation
(heading (yaw), roll, pitch) of the IMU Brick in Euler angles. See
:func:`Get Orientation` for details.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Orientation Period`, ausgelöst. Die :word:`parameters` sind die
Orientierung (Gier-, Roll-, Nickwinkel) des IMU Brick in Eulerwinkeln. Siehe
:func:`Get Orientation` für Details.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Quaternion',
'elements': [('W', 'int16', 1, 'out'),
             ('X', 'int16', 1, 'out'),
             ('Y', 'int16', 1, 'out'),
             ('Z', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Quaternion Period`. The :word:`parameters` are the orientation
(x, y, z, w) of the IMU Brick in quaternions. See :func:`Get Quaternion`
for details.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set Quaternion Period`, ausgelöst. Die :word:`parameters` sind die
Orientierung (x, y, z, w) des IMU Brick in Quaternionen. Siehe
:func:`Get Quaternion` für Details.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'All Data',
'elements': [('Acceleration', 'int16', 3, 'out'),
             ('Magnetic Field', 'int16', 3, 'out'),
             ('Angular Velocity', 'int16', 3, 'out'),
             ('Euler Angle', 'int16', 3, 'out'),
             ('Quaternion', 'int16', 4, 'out'),
             ('Linear Acceleration', 'int16', 3, 'out'),
             ('Gravity Vector', 'int16', 3, 'out'),
             ('Temperature', 'int8', 1, 'out'),
             ('Calibration Status', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set All Data Period`. The :word:`parameters` are as for
:func:`Get All Data`.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit
:func:`Set All Data Period`, ausgelöst. Die :word:`parameter` sind die
gleichen wie bei :func:`Get All Data`.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Sensor Configuration',
'elements': [('Magnetometer Rate', 'uint8', 1, 'in', {'constant_group': 'Magnetometer Rate'}),
             ('Gyroscope Range', 'uint8', 1, 'in', {'constant_group': 'Gyroscope Range'}),
             ('Gyroscope Bandwidth', 'uint8', 1, 'in', {'constant_group': 'Gyroscope Bandwidth'}),
             ('Accelerometer Range', 'uint8', 1, 'in', {'constant_group': 'Accelerometer Range'}),
             ('Accelerometer Bandwidth', 'uint8', 1, 'in', {'constant_group': 'Accelerometer Bandwidth'})],
'since_firmware': [2, 0, 5],
'doc': ['af', {
'en':
"""
Sets the available sensor configuration for the Magnetometer, Gyroscope and
Accelerometer. The Accelerometer Range is user selectable in all fusion modes,
all other configurations are auto-controlled in fusion mode.

The default values are:

* Magnetometer Rate 20Hz
* Gyroscope Range 2000°/s
* Gyroscope Bandwidth 32Hz
* Accelerometer Range +/-4G
* Accelerometer Bandwidth 62.5Hz
""",
'de':
"""
Setzt die verfügbaren Sensor-Konfigurationen für Magnetometer, Gyroskop und
Beschleunigungssensor. Der Beschleunigungssensor-Wertebereich ist in allen
Fusion-Modi wählbar, während alle anderen Konfigurationen im Fusion-Modus
automatisch kontrolliert werden.

Die Standardwerte sind:

* Magnetometer-Rate 20Hz
* Gyroskop-Wertebereich 2000°/s
* Gyroskop-Bandweite 32Hz
* Beschleunigungssensor-Wertebereich +/-4G
* Beschleunigungssensor-Bandweite 62.5Hz
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Sensor Configuration',
'elements': [('Magnetometer Rate', 'uint8', 1, 'out', {'constant_group': 'Magnetometer Rate'}),
             ('Gyroscope Range', 'uint8', 1, 'out', {'constant_group': 'Gyroscope Range'}),
             ('Gyroscope Bandwidth', 'uint8', 1, 'out', {'constant_group': 'Gyroscope Bandwidth'}),
             ('Accelerometer Range', 'uint8', 1, 'out', {'constant_group': 'Accelerometer Range'}),
             ('Accelerometer Bandwidth', 'uint8', 1, 'out', {'constant_group': 'Accelerometer Bandwidth'})],
'since_firmware': [2, 0, 5],
'doc': ['af', {
'en':
"""
Returns the sensor configuration as set by :func:`Set Sensor Configuration`.
""",
'de':
"""
Gibt die Sensor-Konfiguration zurück, wie von :func:`Set Sensor Configuration`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Sensor Fusion Mode',
'elements': [('Mode', 'uint8', 1, 'in', {'constant_group': 'Sensor Fusion',})],
'since_firmware': [2, 0, 5],
'doc': ['af', {
'en':
"""
If the fusion mode is turned off, the functions :func:`Get Acceleration`,
:func:`Get Magnetic Field` and :func:`Get Angular Velocity` return uncalibrated
and uncompensated sensor data. All other sensor data getters return no data.

Since firmware version 2.0.6 you can also use a fusion mode without magnetometer.
In this mode the calculated orientation is relative (with magnetometer it is
absolute with respect to the earth). However, the calculation can't be influenced
by spurious magnetic fields.

Since firmware version 2.0.13 you can also use a fusion mode without fast
magnetometer calibration. This mode is the same as the normal fusion mode,
but the fast magnetometer calibration is turned off. So to find the orientation
the first time will likely take longer, but small magnetic influences might
not affect the automatic calibration as much.

By default sensor fusion is on.
""",
'de':
"""
Wenn der Fusion-Modus deaktiviert wird, geben die Funktionen
:func:`Get Acceleration`, :func:`Get Magnetic Field` und
:func:`Get Angular Velocity` unkalibrierte und umkompensierte Sensorwerte
zurück. Alle anderen Sensordaten-Getter geben keine Daten zurück.

Seit Firmware Version 2.0.6 kann auch ein Fusion-Modus ohne Magnetometer ausgewählt
werden. In diesem Modus wird die Orientierung relativ berechnet (mit Magnetometer
ist sie absolut in Bezug auf die Erde). Allerdings kann die Berechnung in diesem
Fall nicht von störenden Magnetfeldern beeinflusst werden.

Seit Firmware Version 2.0.13 kann auch ein Fusion-Modus ohne schnelle
Magnetometer-Kalibrierung ausgewählt werden. Dieser Modus ist der gleiche wie der
"normale" Fusion-Modus, aber die schnelle Magnetometer-Kalibrierung ist aus. D.h.
die Orientierung zu finden mag beim ersten start länger dauern, allerdings mag
es sein das kleine magnetische einflüsse die automatische Kalibrierung nicht
so stark stören.

Standardmäßig ist der Fusion-Modus aktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Sensor Fusion Mode',
'elements': [('Mode', 'uint8', 1, 'out', {'constant_group': 'Sensor Fusion'})],
'since_firmware': [2, 0, 5],
'doc': ['af', {
'en':
"""
Returns the sensor fusion mode as set by :func:`Set Sensor Fusion Mode`.
""",
'de':
"""
Gibt den aktuellen Sensor-Fusion-Modus zurück, wie von
:func:`Set Sensor Fusion Mode` gesetzt.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Quaternion', 'quaternion'), [(('W', 'Quaternion [W]'), 'int16', 1, 16383.0, None, None), (('X', 'Quaternion [X]'), 'int16', 1, 16383.0, None, None), (('Y', 'Quaternion [Y]'), 'int16', 1, 16383.0, None, None), (('Z', 'Quaternion [Z]'), 'int16', 1, 16383.0, None, None)], [])]
})

com['examples'].append({
'name': 'Callback',
'functions': [('callback', ('Quaternion', 'quaternion'), [(('W', 'Quaternion [W]'), 'int16', 1, 16383.0, None, None), (('X', 'Quaternion [X]'), 'int16', 1, 16383.0, None, None), (('Y', 'Quaternion [Y]'), 'int16', 1, 16383.0, None, None), (('Z', 'Quaternion [Z]'), 'int16', 1, 16383.0, None, None)], None, None),
              ('callback_period', ('Quaternion', 'quaternion'), [], 100)]
})

com['examples'].append({
'name': 'All Data',
'functions': [('callback', ('All Data', 'all data'), [(('Acceleration', ['Acceleration [X]', 'Acceleration [Y]', 'Acceleration [Z]']), 'int16', 3, 100.0, 'm/s²', None), (('Magnetic Field', ['Magnetic Field [X]', 'Magnetic Field [Y]', 'Magnetic Field [Z]']), 'int16', 3, 16.0, 'µT', None), (('Angular Velocity', ['Angular Velocity [X]', 'Angular Velocity [Y]', 'Angular Velocity [Z]']), 'int16', 3, 16.0, '°/s', None), (('Euler Angle', ['Euler Angle [X]', 'Euler Angle [Y]', 'Euler Angle [Z]']), 'int16', 3, 16.0, '°', None), (('Quaternion', ['Quaternion [W]', 'Quaternion [X]', 'Quaternion [Y]', 'Quaternion [Z]']), 'int16', 4, 16383.0, None, None), (('Linear Acceleration', ['Linear Acceleration [X]', 'Linear Acceleration [Y]', 'Linear Acceleration [Z]']), 'int16', 3, 100.0, 'm/s²', None), (('Gravity Vector', ['Gravity Vector [X]', 'Gravity Vector [Y]', 'Gravity Vector [Z]']), 'int16', 3, 100.0, 'm/s²', None), (('Temperature', 'Temperature'), 'int8', 1, None, '°C', None), (('Calibration Status', 'Calibration Status'), 'uint8:bitmask:8', 1, None, None, None)], None, None),
              ('callback_period', ('All Data', 'all data'), [], 100)]
})

com['openhab'] = {
    'imports': oh_generic_channel_imports() + ["org.eclipse.smarthome.core.library.types.OnOffType"],
    'params': [{
            'name': 'Magnetometer Rate',
            'type': 'integer',
            'options':[('2Hz', 0),
                       ('6Hz', 1),
                       ('8Hz', 2),
                       ('10Hz', 3),
                       ('15Hz', 4),
                       ('20Hz', 5),
                       ('25Hz', 6),
                       ('30Hz', 7)],
            'limitToOptions': 'true',
            'default': 5,
            'label': 'Magnetometer Rate',
            'description': 'This option is auto-controlled in fusion mode.'
        }, {
            'name': 'Gyroscope Range',
            'type': 'integer',
            'options':[('2000°/s', 0),
                        ('1000°/s', 1),
                        ('500°/s', 2),
                        ('250°/s', 3),
                        ('125°/s', 4)],
            'limitToOptions': 'true',
            'default': 0,
            'label': 'Gyroscope Range',
            'description': 'This option is auto-controlled in fusion mode.'
        }, {
            'name': 'Gyroscope Bandwidth',
            'type': 'integer',
            'options':[('523Hz', 0),
                       ('230Hz', 1),
                       ('116Hz', 2),
                       ('47Hz', 3),
                       ('23Hz', 4),
                       ('12Hz', 5),
                       ('64Hz', 6),
                       ('32Hz', 7)],
            'limitToOptions': 'true',
            'default': 7,
            'label': 'Gyroscope Bandwidth',
            'description': 'This option is auto-controlled in fusion mode.'
        }, {
            'name': 'Accelerometer Range',
            'type': 'integer',
            'options':[('±2G', 0),
                       ('±4G', 1),
                       ('±8G', 2),
                       ('±16G', 3)],
            'limitToOptions': 'true',
            'default': 1,
            'label': 'Accelerometer Range',
            'description': 'This option is user selectable in all fusion modes.'
        }, {
            'name': 'Accelerometer Bandwidth',
            'type': 'integer',
            'options':[('7.81Hz', 0),
                       ('15.63Hz', 1),
                       ('31.25Hz', 2),
                       ('62.5Hz', 3),
                       ('125Hz', 4),
                       ('250Hz', 5),
                       ('500Hz', 6),
                       ('1000Hz', 7)],
            'limitToOptions': 'true',
            'default': 3,
            'label': 'Accelerometer Bandwidth',
            'description': 'This option is auto-controlled in fusion mode.'
        }, {
            'name': 'Sensor Fusion Mode',
            'type': 'integer',
            'options':[('Off', 0),
                       ('On', 1),
                       ('On Without Magnetometer', 2),
                       ('On Without Fast Magnetometer Calibration', 3)],
            'default': 1,
            'limitToOptions': 'true',
            'label': 'Sensor Fusion Mode',
            'description': "If the fusion mode is turned off, the Acceleration, Magnetic Field and Angular Velocity channels return uncalibrated and uncompensated sensor data. All other sensor channels return no data.<br/><br/>Since firmware version 2.0.6 you can also use a fusion mode without magnetometer. In this mode the calculated orientation is relative (with magnetometer it is absolute with respect to the earth). However, the calculation can't be influenced by spurious magnetic fields.<br/><br/>Since firmware version 2.0.13 you can also use a fusion mode without fast magnetometer calibration. This mode is the same as the normal fusion mode, but the fast magnetometer calibration is turned off. So to find the orientation the first time will likely take longer, but small magnetic influences might not affect the automatic calibration as much.<br/><br/>By default sensor fusion is on."
        },
        update_interval('Acceleration', 'the acceleration'),
        update_interval('Magnetic Field', 'the magnetic field'),
        update_interval('Angular Velocity', 'the angular velocity'),
        update_interval('Orientation', 'the orientation as euler angles'),
        update_interval('Quaternion', 'the orientation as quaternion'),
        update_interval('Linear Acceleration', 'the linear acceleration'),
        update_interval('Gravity Vector', 'the gravity vector'),
        update_interval('Temperature', 'the temperature'),
        ],
    'param_groups': oh_generic_channel_param_groups(),
    'init_code': """
    this.setAccelerationPeriod(cfg.accelerationUpdateInterval);
    this.setMagneticFieldPeriod(cfg.magneticFieldUpdateInterval);
    this.setAngularVelocityPeriod(cfg.angularVelocityUpdateInterval);
    this.setOrientationPeriod(cfg.orientationUpdateInterval);
    this.setQuaternionPeriod(cfg.quaternionUpdateInterval);
    this.setLinearAccelerationPeriod(cfg.linearAccelerationUpdateInterval);
    this.setGravityVectorPeriod(cfg.gravityVectorUpdateInterval);
    this.setTemperaturePeriod(cfg.temperatureUpdateInterval);
    this.setSensorConfiguration(cfg.magnetometerRate.shortValue(), cfg.gyroscopeRange.shortValue(), cfg.gyroscopeBandwidth.shortValue(), cfg.accelerometerRange.shortValue(), cfg.accelerometerBandwidth.shortValue());
    this.setSensorFusionMode(cfg.sensorFusionMode.shortValue());
    """,
    'channels': [{
            'id': 'Acceleration {}'.format(axis.upper()),
            'type': 'Acceleration',
            'label': 'Acceleration - {}'.format(axis.upper()),

            'getters': [{
                'packet': 'Get Acceleration',
                'transform': 'new QuantityType(value.{}{{divisor}}, {{unit}})'.format(axis.lower())}],

            'callbacks': [{
                'packet': 'Acceleration',
                'transform': 'new QuantityType({}{{divisor}}, {{unit}})'.format(axis.lower())}],
            'java_unit': 'SmartHomeUnits.METRE_PER_SQUARE_SECOND',
            'divisor': 100.0,
            'is_trigger_channel': False
        } for axis in ['X', 'Y', 'Z']
    ] + [{
            'id': 'Magnetic Field {}'.format(axis.upper()),
            'type': 'Magnetic Field',
            'label': 'Magnetic Field - {}'.format(axis.upper()),

            'getters': [{
                'packet': 'Get Magnetic Field',
                'transform': 'new QuantityType(value.{}{{divisor}}, {{unit}})'.format(axis.lower())}],

            'callbacks': [{
                'packet': 'Magnetic Field',
                'transform': 'new QuantityType({}{{divisor}}, {{unit}})'.format(axis.lower())}],
            'java_unit': 'SmartHomeUnits.TESLA',
            'divisor': 16000000.0,
            'is_trigger_channel': False
        } for axis in ['X', 'Y', 'Z']
    ] +  [{
            'id': 'Angular Velocity {}'.format(axis.upper()),
            'type': 'Angular Velocity',
            'label': 'Angular Velocity - {}'.format(axis.upper()),

            'getters': [{
                'packet': 'Get Angular Velocity',
                'transform': 'new QuantityType(value.{}{{divisor}}, {{unit}})'.format(axis.lower())}],

            'callbacks': [{
                'packet': 'Angular Velocity',
                'transform': 'new QuantityType({}{{divisor}}, {{unit}})'.format(axis.lower())}],
            'java_unit': 'SmartHomeUnits.ONE',
            'divisor': 16.0,
            'is_trigger_channel': False
        } for axis in ['X', 'Y', 'Z']
    ] + [{
            'id': 'Orientation {}'.format(angle),
            'type': 'Orientation',
            'label': 'Orientation - {}'.format(angle),

            'getters': [{
                'packet': 'Get Orientation',
                'transform': 'new QuantityType(value.{}{{divisor}}, {{unit}})'.format(angle.lower())}],

            'callbacks': [{
                'packet': 'Orientation',
                'transform': 'new QuantityType({}{{divisor}}, {{unit}})'.format(angle.lower())}],
            'java_unit': 'SmartHomeUnits.DEGREE_ANGLE',
            'divisor': 16.0,
            'is_trigger_channel': False
        } for angle in ['Heading', 'Roll', 'Pitch']
    ] + [{
            'id': 'Quaternion {}'.format(axis.upper()),
            'type': 'Quaternion',
            'label': 'Quaternion - {}'.format(axis.upper()),

            'getters': [{
                'packet': 'Get Quaternion',
                'transform': 'new QuantityType(value.{}{{divisor}}, {{unit}})'.format(axis.lower())}],

            'callbacks': [{
                'packet': 'Quaternion',
                'transform': 'new QuantityType({}{{divisor}}, {{unit}})'.format(axis.lower())}],
            'java_unit': 'SmartHomeUnits.ONE',
            'divisor': 16383.0,
            'is_trigger_channel': False
        } for axis in ['W', 'X', 'Y', 'Z']
    ] + [{
            'id': 'Linear Acceleration {}'.format(axis.upper()),
            'type': 'Linear Acceleration',
            'label': 'Linear Acceleration - {}'.format(axis.upper()),

            'getters': [{
                'packet': 'Get Linear Acceleration',
                'transform': 'new QuantityType(value.{}{{divisor}}, {{unit}})'.format(axis.lower())}],

            'callbacks': [{
                'packet': 'Linear Acceleration',
                'transform': 'new QuantityType({}{{divisor}}, {{unit}})'.format(axis.lower())}],
            'java_unit': 'SmartHomeUnits.METRE_PER_SQUARE_SECOND',
            'divisor': 100.0,
            'is_trigger_channel': False
        } for axis in ['X', 'Y', 'Z']
    ] + [{
            'id': 'Gravity Vector {}'.format(axis.upper()),
            'type': 'Gravity Vector',
            'label': 'Gravity Vector - {}'.format(axis.upper()),

            'getters': [{
                'packet': 'Get Gravity Vector',
                'transform': 'new QuantityType(value.{}{{divisor}}, {{unit}})'.format(axis.lower())}],

            'callbacks': [{
                'packet': 'Gravity Vector',
                'transform': 'new QuantityType({}{{divisor}}, {{unit}})'.format(axis.lower())}],
            'java_unit': 'SmartHomeUnits.STANDARD_GRAVITY',
            'divisor': 980.665,
            'is_trigger_channel': False
        } for axis in ['X', 'Y', 'Z']
    ] + [{
        'id': 'Temperature',
        'type': 'Temperature',
        'label': 'Temperature',

        'getters': [{
            'packet': 'Get Temperature',
            'transform': 'new QuantityType(value{divisor}, {unit})'}],

        'callbacks': [{
            'packet': 'Temperature',
            'transform': 'new QuantityType(temperature{divisor}, {unit})'}],
        'java_unit': 'SIUnits.CELSIUS',
        'divisor': 1.0,
        'is_trigger_channel': False
    }] + [{
            'id': 'Enable LEDs',
            'type': 'Enable LEDs',

            'setters': [{
                'predicate': 'cmd == OnOffType.ON',
                'packet': 'Leds On',
            }, {
                'predicate': 'cmd == OnOffType.OFF',
                'packet': 'Leds Off',
            },],
            'setter_command_type': "OnOffType",

            'getters': [{
                'packet': 'Are Leds On',
                'transform': 'value? OnOffType.ON : OnOffType.OFF'}]
        }
    ],
    'channel_types': [
        oh_generic_channel_type('Acceleration', 'Number:Acceleration', 'NOT USED',
                     description='The acceleration from the accelerometer for the x, y and z axis in m/s².',
                     read_only=True,
                     pattern='%.3f %unit%'),
        oh_generic_channel_type('Magnetic Field', 'Number:MagneticFluxDensity', 'NOT USED',
                     description='The calibrated magnetic field from the magnetometer for the x, y and z axis in Tesla.',
                     read_only=True,
                     pattern='%.9f %unit%'),
        oh_generic_channel_type('Angular Velocity', 'Number:Dimensionless', 'NOT USED',
                     description='The calibrated angular velocity from the gyroscope for the x, y and z axis in °/s.',
                     read_only=True,
                     pattern='%.3f'),
        oh_generic_channel_type('Orientation', 'Number:Angle', 'NOT USED',
                     description='The current orientation (heading, roll, pitch) of the IMU Brick as independent Euler angles in 1/16 degree. Note that Euler angles always experience a gimbal lock. We recommend that you use quaternions instead, if you need the absolute orientation.',
                     read_only=True,
                     pattern='%.2f %unit%'),
        oh_generic_channel_type('Quaternion', 'Number:Dimensionless', 'NOT USED',
                     description='The current orientation (w, x, y, z) of the IMU Brick as quaternions.',
                     read_only=True,
                     pattern='%.4f %unit%'),
        oh_generic_channel_type('Linear Acceleration', 'Number:Acceleration', 'NOT USED',
                     description='The linear acceleration from the accelerometer for the x, y and z axis in m/s. The linear acceleration is the acceleration in each of the three axis of the IMU Brick with the influences of gravity removed.',
                     read_only=True,
                     pattern='%.2f %unit%'),
        oh_generic_channel_type('Gravity Vector', 'Number:Acceleration', 'NOT USED',
                     description='The current gravity vector of the IMU Brick for the x, y and z axis in g (1g = 9.80665m/s²). The gravity vector is the acceleration that occurs due to gravity. Influences of additional linear acceleration are removed.',
                     read_only=True,
                     pattern='%.2f %unit%'),
        oh_generic_channel_type('Temperature', 'Number:Temperature', 'NOT USED',
                     description='The temperature of the IMU Brick. The temperature is given in °C. The temperature is measured in the core of the BNO055 IC, it is not the ambient temperature.',
                     read_only=True,
                     pattern='%d %unit%'),
        oh_generic_channel_type('Enable LEDs', 'Switch', 'Enable LEDs',
                     description='Enable/disable the orientation and direction LEDs of the IMU Brick.'),
    ]
}
