# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# IMU Brick communication config

from openhab_common import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 4],
    'category': 'Brick',
    'device_identifier': 16,
    'name': 'IMU',
    'display_name': 'IMU',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Full fledged AHRS with 9 degrees of freedom',
        'de': 'Voll ausgestattetes AHRS mit 9 Freiheitsgraden'
    },
    'released': True,
    'documented': True,
    'discontinued': True, # replaced by IMU Brick 2.0
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
'name': 'Calibration Type',
'type': 'uint8',
'constants': [('Accelerometer Gain', 0),
              ('Accelerometer Bias', 1),
              ('Magnetometer Gain', 2),
              ('Magnetometer Bias', 3),
              ('Gyroscope Gain', 4),
              ('Gyroscope Bias', 5)]
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
x, y and z axis in g/1000 (1g = 9.80665m/s²).

If you want to get the acceleration periodically, it is recommended
to use the :cb:`Acceleration` callback and set the period with
:func:`Set Acceleration Period`.
""",
'de':
"""
Gibt die kalibrierten Beschleunigungen des Beschleunigungsmessers für die
X, Y und Z-Achse in g/1000 zurück (1g = 9,80665m/s²).

Wenn die kalibrierten Beschleunigungen periodisch abgefragt werden soll, wird
empfohlen den :cb:`Acceleration` Callback zu nutzen und die Periode mit
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
x, y and z axis in mG (Milligauss or Nanotesla).

If you want to get the magnetic field periodically, it is recommended
to use the :cb:`Magnetic Field` callback and set the period with
:func:`Set Magnetic Field Period`.
""",
'de':
"""
Gibt das kalibrierte magnetische Feld des Magnetometers mit den X-, Y- und
Z-Komponenten in mG zurück (Milligauss oder Nanotesla).

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
x, y and z axis in °/14.375s (you have to divide by 14.375 to
get the value in °/s).

If you want to get the angular velocity periodically, it is recommended
to use the :cb:`Angular Velocity` callback and set the period with
:func:`Set Angular Velocity Period`.
""",
'de':
"""
Gibt die kalibrierten Winkelgeschwindigkeiten des Gyroskops für die X-, Y- und
Z-Achse in °/14,375s zurück. (Um den Wert in °/s zu erhalten ist es notwendig
durch 14,375 zu teilen)

Wenn die Winkelgeschwindigkeiten periodisch abgefragt werden sollen, wird
empfohlen den :cb:`Angular Velocity` Callback zu nutzen und die Periode mit
:func:`Set Angular Velocity Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get All Data',
'elements': [('Acc X', 'int16', 1, 'out'),
             ('Acc Y', 'int16', 1, 'out'),
             ('Acc Z', 'int16', 1, 'out'),
             ('Mag X', 'int16', 1, 'out'),
             ('Mag Y', 'int16', 1, 'out'),
             ('Mag Z', 'int16', 1, 'out'),
             ('Ang X', 'int16', 1, 'out'),
             ('Ang Y', 'int16', 1, 'out'),
             ('Ang Z', 'int16', 1, 'out'),
             ('Temperature', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the data from :func:`Get Acceleration`, :func:`Get Magnetic Field`
and :func:`Get Angular Velocity` as well as the temperature of the IMU Brick.

The temperature is given in °C/100.

If you want to get the data periodically, it is recommended
to use the :cb:`All Data` callback and set the period with
:func:`Set All Data Period`.
""",
'de':
"""
Gibt die Daten von :func:`Get Acceleration`, :func:`Get Magnetic Field`
und :func:`Get Angular Velocity` sowie die Temperatur des IMU Brick zurück.

Die Temperatur wird in °C/100 ausgegeben.

Wenn die Daten periodisch abgefragt werden sollen, wird empfohlen den
:cb:`All Data` Callback zu nutzen und die Periode mit
:func:`Set All Data Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Orientation',
'elements': [('Roll', 'int16', 1, 'out'),
             ('Pitch', 'int16', 1, 'out'),
             ('Yaw', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current orientation (roll, pitch, yaw) of the IMU Brick as Euler
angles in one-hundredth degree. Note that Euler angles always experience a
`gimbal lock <https://en.wikipedia.org/wiki/Gimbal_lock>`__.

We recommend that you use quaternions instead.

The order to sequence in which the orientation values should be applied is
roll, yaw, pitch.

If you want to get the orientation periodically, it is recommended
to use the :cb:`Orientation` callback and set the period with
:func:`Set Orientation Period`.
""",
'de':
"""
Gibt die aktuelle Orientierung (Roll-, Nick-, Gierwinkel) des IMU Brick in
Eulerwinkeln (in 1/100 °) zurück. Zu beachten ist, dass Eulerwinkel immer eine
`kardanische Blockade <https://de.wikipedia.org/wiki/Gimbal_Lock>`__ erfahren.

Wir empfehlen die Verwendung von Quaternionen stattdessen.

Die Reihenfolge in denen die Orientierungswerte angewandt werden sollten,
ist Roll-, Nick-, Gierwinkel.

Wenn die Orientierung periodisch abgefragt werden sollen, wird empfohlen den
:cb:`Orientation` Callback zu nutzen und die Periode mit
:func:`Set Orientation Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Quaternion',
'elements': [('X', 'float', 1, 'out'),
             ('Y', 'float', 1, 'out'),
             ('Z', 'float', 1, 'out'),
             ('W', 'float', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current orientation (x, y, z, w) of the IMU as
`quaternions <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__.

You can go from quaternions to Euler angles with the following formula::

 xAngle = atan2(2*y*w - 2*x*z, 1 - 2*y*y - 2*z*z)
 yAngle = atan2(2*x*w - 2*y*z, 1 - 2*x*x - 2*z*z)
 zAngle =  asin(2*x*y + 2*z*w)

This process is not reversible, because of the
`gimbal lock <https://en.wikipedia.org/wiki/Gimbal_lock>`__.

It is also possible to calculate independent angles. You can calculate
yaw, pitch and roll in a right-handed vehicle coordinate system according to
DIN70000 with::

 yaw   =  atan2(2*x*y + 2*w*z, w*w + x*x - y*y - z*z)
 pitch = -asin(2*w*y - 2*x*z)
 roll  = -atan2(2*y*z + 2*w*x, -w*w + x*x + y*y - z*z))

Converting the quaternions to an OpenGL transformation matrix is
possible with the following formula::

 matrix = [[1 - 2*(y*y + z*z),     2*(x*y - w*z),     2*(x*z + w*y), 0],
           [    2*(x*y + w*z), 1 - 2*(x*x + z*z),     2*(y*z - w*x), 0],
           [    2*(x*z - w*y),     2*(y*z + w*x), 1 - 2*(x*x + y*y), 0],
           [                0,                 0,                 0, 1]]

If you want to get the quaternions periodically, it is recommended
to use the :cb:`Quaternion` callback and set the period with
:func:`Set Quaternion Period`.
""",
'de':
"""
Gibt die aktuelle Orientierung (x, y, z, w) des IMU Brick als
`Quaterinonen <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`__
zurück.

Die Umrechnung von Quaternionen in Eulerwinkel ist mit folgender Formel möglich::

 xAngle = atan2(2*y*w - 2*x*z, 1 - 2*y*y - 2*z*z)
 yAngle = atan2(2*x*w - 2*y*z, 1 - 2*x*x - 2*z*z)
 zAngle =  asin(2*x*y + 2*z*w)

Es ist auch möglich unabhängige Winkel zu berechen. Yaw, Pitch und Roll
in einem rechtshändigen Fahrzeugkoordinatensystem nach DIN70000 können
wie folgt berechnet werden::

 yaw   =  atan2(2*x*y + 2*w*z, w*w + x*x - y*y - z*z)
 pitch = -asin(2*w*y - 2*x*z)
 roll  = -atan2(2*y*z + 2*w*x, -w*w + x*x + y*y - z*z))

Diese Umrechnung ist irreversibel aufgrund der
`kardanischen Blockade <https://de.wikipedia.org/wiki/Gimbal_lock>`__.

Die Umrechnung von Quaternionen in eine OpenGL Transformationsmatrix ist
mit folgender Formel möglich::

 matrix = [[1 - 2*(y*y + z*z),     2*(x*y - w*z),     2*(x*z + w*y), 0],
           [    2*(x*y + w*z), 1 - 2*(x*x + z*z),     2*(y*z - w*x), 0],
           [    2*(x*z - w*y),     2*(y*z + w*x), 1 - 2*(x*x + y*y), 0],
           [                0,                 0,                 0, 1]]

Wenn die Quaternionen periodisch abgefragt werden sollen, wird empfohlen den
:cb:`Quaternion` Callback zu nutzen und die Periode mit
:func:`Set Quaternion Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get IMU Temperature',
'elements': [('Temperature', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the temperature of the IMU Brick. The temperature is given in
°C/100.
""",
'de':
"""
Gibt die Temperatur (in °C/100) des IMU Brick zurück.
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
'name': 'Set Acceleration Range',
'elements': [('Range', 'uint8', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Not implemented yet.
""",
'de':
"""
Bisher nicht implementiert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Acceleration Range',
'elements': [('Range', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Not implemented yet.
""",
'de':
"""
Bisher nicht implementiert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Magnetometer Range',
'elements': [('Range', 'uint8', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Not implemented yet.
""",
'de':
"""
Bisher nicht implementiert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Magnetometer Range',
'elements': [('Range', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Not implemented yet.
""",
'de':
"""
Bisher nicht implementiert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Convergence Speed',
'elements': [('Speed', 'uint16', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the convergence speed of the IMU Brick in °/s. The convergence speed
determines how the different sensor measurements are fused.

If the orientation of the IMU Brick is off by 10° and the convergence speed is
set to 20°/s, it will take 0.5s until the orientation is corrected. However,
if the correct orientation is reached and the convergence speed is too high,
the orientation will fluctuate with the fluctuations of the accelerometer and
the magnetometer.

If you set the convergence speed to 0, practically only the gyroscope is used
to calculate the orientation. This gives very smooth movements, but errors of the
gyroscope will not be corrected. If you set the convergence speed to something
above 500, practically only the magnetometer and the accelerometer are used to
calculate the orientation. In this case the movements are abrupt and the values
will fluctuate, but there won't be any errors that accumulate over time.

In an application with high angular velocities, we recommend a high convergence
speed, so the errors of the gyroscope can be corrected fast. In applications with
only slow movements we recommend a low convergence speed. You can change the
convergence speed on the fly. So it is possible (and recommended) to increase
the convergence speed before an abrupt movement and decrease it afterwards
again.

You might want to play around with the convergence speed in the Brick Viewer to
get a feeling for a good value for your application.

The default value is 30.
""",
'de':
"""
Setzt die Konvergenzgeschwindigkeit des IMU Brick in °/s. Die
Konvergenzgeschwindigkeit bestimmt wie die unterschiedlichen Sensormessungen
vereinigt werden.

Wenn die Orientierung des IMU Brick eine Abweichung von 10° hat und die
Konvergenzgeschwindigkeit auf 20°/s konfiguriert ist, dann dauert es
0,5s bis die Orientierung korrigiert ist. Bei einer zu hohen Konvergenzgeschwindigkeit
wird nach Erreichen der korrekten Orientierung, diese um die Fluktuationen des
Beschleunigungsmessers und des Magnetometers schwanken.

Wenn die Konvergenzgeschwindigkeit auf 0 gesetzt wird, erfolgt die Berechnung der
Orientierung praktisch nur anhand der Gyroskopdaten. Dies ergibt sehr gleichmäßige
Bewegungen aber Fehler des Gyroskops werden nicht korrigiert. Wenn die
Konvergenzgeschwindigkeit über 500 gesetzt wird, erfolgt die Berechnung der
Orientierung praktisch nur anhand der Beschleunigungsmesser- und Magnetometerdaten.
In diesem Fall sind die Bewegungen abrupt und die Werte werden schwanken. Es
treten aber keine akkumulativen Fehler auf.

In Anwendungen mit hohen Winkelgeschwindigkeiten wird eine hohe Konvergenzgeschwindigkeit
empfohlen, so dass Fehler des Gyroskops schnell korrigiert werden können. In
Anwendungen mit langsamen Bewegungen wird entsprechend eine geringe
Konvergenzgeschwindigkeit empfohlen. Es ist möglich die Konvergenzgeschwindigkeit
spontan zu ändern. Dadurch ist es möglich (und empfohlen) direkt vor einer abrupten
Bewegung die Konvergenzgeschwindigkeit zu erhöhen und im Anschluss wieder zu verringern.

Um ein Gefühl für einen guten Wert, für die Konvergenzgeschwindigkeit,
in deiner Anwendung zu bekommen ist es ratsam im Brick Viewer verschiedenste Werte
auszuprobieren.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Convergence Speed',
'elements': [('Speed', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the convergence speed as set by :func:`Set Convergence Speed`.
""",
'de':
"""
Gibt die Konvergenzgeschwindigkeit zurück, wie von :func:`Set Convergence Speed` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Calibration',
'elements': [('Typ', 'uint8', 1, 'in', {'constant_group': 'Calibration Type'}),
             ('Data', 'int16', 10, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
There are several different types that can be calibrated:

.. csv-table::
 :header: "Type", "Description", "Values"
 :widths: 10, 30, 110

 "0",    "Accelerometer Gain", "``[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]``"
 "1",    "Accelerometer Bias", "``[bias x, bias y, bias z, 0, 0, 0, 0, 0, 0, 0]``"
 "2",    "Magnetometer Gain",  "``[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]``"
 "3",    "Magnetometer Bias",  "``[bias x, bias y, bias z, 0, 0, 0, 0, 0, 0, 0]``"
 "4",    "Gyroscope Gain",     "``[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]``"
 "5",    "Gyroscope Bias",     "``[bias xl, bias yl, bias zl, temp l, bias xh, bias yh, bias zh, temp h, 0, 0]``"

The calibration via gain and bias is done with the following formula::

 new_value = (bias + orig_value) * gain_mul / gain_div

If you really want to write your own calibration software, please keep
in mind that you first have to undo the old calibration (set bias to 0 and
gain to 1/1) and that you have to average over several thousand values
to obtain a usable result in the end.

The gyroscope bias is highly dependent on the temperature, so you have to
calibrate the bias two times with different temperatures. The values ``xl``,
``yl``, ``zl`` and ``temp l`` are the bias for ``x``, ``y``, ``z`` and the
corresponding temperature for a low temperature. The values ``xh``, ``yh``,
``zh`` and ``temp h`` are the same for a high temperatures. The temperature
difference should be at least 5°C. If you have a temperature where the
IMU Brick is mostly used, you should use this temperature for one of the
sampling points.

.. note::
 We highly recommend that you use the Brick Viewer to calibrate your
 IMU Brick.
""",
'de':
"""
Es sind folgende verschiedene Kalibrierungen möglich:

.. csv-table::
 :header: "Typ", "Beschreibung", "Werte"
 :widths: 10, 30, 110

 "0",    "Beschleunigungsmesser Verstärkung", "``[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]``"
 "1",    "Beschleunigungsmesser Versatz",     "``[bias x, bias y, bias z, 0, 0, 0, 0, 0, 0, 0]``"
 "2",    "Magnetometer Verstärkung",          "``[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]``"
 "3",    "Magnetometer Versatz",              "``[bias x, bias y, bias z, 0, 0, 0, 0, 0, 0, 0]``"
 "4",    "Gyroskop Verstärkung",              "``[mul x, mul y, mul z, div x, div y, div z, 0, 0, 0, 0]``"
 "5",    "Gyroskop Versatz",                  "``[bias xl, bias yl, bias zl, temp l, bias xh, bias yh, bias zh, temp h, 0, 0]``"

Die Kalibrierung mittels Verstärkung und Versatz wird über folgende Formel realisiert::

 new_value = (bias + orig_value) * gain_mul / gain_div

Für die Implementierung einer eigenen Kalibriersoftware sollte beachtet werden,
dass zuerst die bisherige Kalibrierung rückgängig gemacht werden muss (Versatz
auf 0 und Verstärkung auf 1/1 setzen) und das über mehrere tausend Werte
gemittelt werden sollte um ein benutzbares Ergebnis zu erhalten.

Der Versatz des Gyroskops ist sehr temperaturabhängig und daher muss die
Kalibrierung des Versatzes mit zwei unterschiedlichen Temperaturen erfolgen.
Die Werte ``xl``, ``yl``, ``zl`` und ``temp l`` sind der Versatz für ``x``,
``y``, ``z`` und die zugehörige geringe Temperatur. Die Werte ``xh``, ``yh``,
``zh`` und ``temp h`` sind entsprechend für eine höhere Temperatur. Die
Temperaturdifferenz sollte mindestens 5°C betragen. Die übliche
Betriebstemperatur des IMU Brick sollte einer der Kalibrierpunkte sein.

.. note::
 Wir empfehlen dringend den Brick Viewer zur Kalibrierung des IMU Brick zu
 verwenden.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Calibration',
'elements': [('Typ', 'uint8', 1, 'in', {'constant_group': 'Calibration Type'}),
             ('Data', 'int16', 10, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the calibration for a given type as set by :func:`Set Calibration`.
""",
'de':
"""
Gibt die Kalibrierung für den ausgewählten Typ zurück, wie von
:func:`Set Calibration` gesetzt.
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
Sets the period in ms with which the :cb:`Magnetic Field` callback is
triggered periodically. A value of 0 turns the callback off.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Magnetic Field` Callback
ausgelöst wird. Ein Wert von 0 deaktiviert den Callback.
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
'name': 'All Data',
'elements': [('Acc X', 'int16', 1, 'out'),
             ('Acc Y', 'int16', 1, 'out'),
             ('Acc Z', 'int16', 1, 'out'),
             ('Mag X', 'int16', 1, 'out'),
             ('Mag Y', 'int16', 1, 'out'),
             ('Mag Z', 'int16', 1, 'out'),
             ('Ang X', 'int16', 1, 'out'),
             ('Ang Y', 'int16', 1, 'out'),
             ('Ang Z', 'int16', 1, 'out'),
             ('Temperature', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set All Data Period`. The :word:`parameters` are the acceleration,
the magnetic field and the angular velocity for the x, y and z axis as
well as the temperature of the IMU Brick.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit :func:`Set All Data Period`,
ausgelöst. Die :word:`parameters` sind die Beschleunigungen, Magnetfeldkomponenten
und die Winkelgeschwindigkeiten der X, Y und Z-Achse sowie die Temperatur
des IMU Brick.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Orientation',
'elements': [('Roll', 'int16', 1, 'out'),
             ('Pitch', 'int16', 1, 'out'),
             ('Yaw', 'int16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Orientation Period`. The :word:`parameters` are the orientation
(roll, pitch and yaw) of the IMU Brick in Euler angles. See
:func:`Get Orientation` for details.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit :func:`Set Orientation Period`,
ausgelöst. Die :word:`parameters` sind die Orientierung (Roll-, Nick-, Gierwinkel) des
IMU Brick in Eulerwinkeln. Siehe :func:`Get Orientation` für Details.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Quaternion',
'elements': [('X', 'float', 1, 'out'),
             ('Y', 'float', 1, 'out'),
             ('Z', 'float', 1, 'out'),
             ('W', 'float', 1, 'out')],
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
Dieser Callback wird mit der Periode, wie gesetzt mit :func:`Set Quaternion Period`,
ausgelöst. Die :word:`parameters` sind die Orientierung (x, y, z, w) des
IMU Brick in Quaternionen. Siehe :func:`Get Quaternion` für Details.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Orientation Calculation On',
'elements': [],
'since_firmware': [2, 0, 2],
'doc': ['af', {
'en':
"""
Turns the orientation calculation of the IMU Brick on.

As default the calculation is on.
""",
'de':
"""
Aktiviert die Orientierungsberechnungen des IMU Brick.

Standardmäßig sind die Berechnungen an.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Orientation Calculation Off',
'elements': [],
'since_firmware': [2, 0, 2],
'doc': ['af', {
'en':
"""
Turns the orientation calculation of the IMU Brick off.

If the calculation is off, :func:`Get Orientation` will return
the last calculated value until the calculation is turned on again.

The trigonometric functions that are needed to calculate the orientation
are very expensive. We recommend to turn the orientation calculation
off if the orientation is not needed, to free calculation time for the
sensor fusion algorithm.

As default the calculation is on.
""",
'de':
"""
Deaktiviert die Orientierungsberechnungen des IMU Brick.

Wenn die Berechnungen deaktiviert sind, gibt :func:`Get Orientation` solange
den letzten berechneten Wer zurück bis die Berechnungen wieder
aktiviert werden.

Die trigonometrischen Funktionen die zur Berechnung der Orientierung
benötigt werden sind sehr teuer. Wir empfehlen die Orientierungsberechnungen
zu deaktivieren wenn sie nicht benötigt werden. Dadurch wird mehr
Rechenzeit für den Sensorfusions-Algorithmus freigegeben.

Standardmäßig sind die Berechnungen an.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Is Orientation Calculation On',
'elements': [('Orientation Calculation On', 'bool', 1, 'out')],
'since_firmware': [2, 0, 2],
'doc': ['af', {
'en':
"""
Returns *true* if the orientation calculation of the IMU Brick
is on, *false* otherwise.
""",
'de':
"""
Gibt zurück ob die Orientierungsberechnungen des IMU Brick aktiv sind.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Quaternion', 'quaternion'), [(('X', 'Quaternion [X]'), 'float', 1, None, None, None), (('Y', 'Quaternion [Y]'), 'float', 1, None, None, None), (('Z', 'Quaternion [Z]'), 'float', 1, None, None, None), (('W', 'Quaternion [W]'), 'float', 1, None, None, None)], [])]
})

com['examples'].append({
'name': 'Callback',
'functions': [('callback', ('Quaternion', 'quaternion'), [(('X', 'Quaternion [X]'), 'float', 1, None, None, None), (('Y', 'Quaternion [Y]'), 'float', 1, None, None, None), (('Z', 'Quaternion [Z]'), 'float', 1, None, None, None), (('W', 'Quaternion [W]'), 'float', 1, None, None, None)], None, None),
              ('callback_period', ('Quaternion', 'quaternion'), [], 1000)]
})

com['openhab'] = {
    'imports': oh_generic_channel_imports() + ["org.eclipse.smarthome.core.library.types.OnOffType"],
    'params': [{
            'name': 'Enable Orientation',
            'type': 'boolean',
            'default': 'true',
            'label': 'Enable Orientation',
            'description': 'Turns the orientation calculation of the IMU Brick on or off. The trigonometric functions that are needed to calculate the orientation are very expensive. We recommend to turn the orientation calculation off if the orientation is not needed, to free calculation time for the sensor fusion algorithm.'
        }, {
            'name': 'Convergence Speed',
            'type': 'integer',
            'min': 0,
            'max': 65536,
            'default': 30,
            'label': 'Convergence Speed',
            'description': "Sets the convergence speed of the IMU Brick in °/s. The convergence speed determines how the different sensor measurements are fused.<br/><br/>If the orientation of the IMU Brick is off by 10° and the convergence speed is set to 20°/s, it will take 0.5s until the orientation is corrected. However, if the correct orientation is reached and the convergence speed is too high, the orientation will fluctuate with the fluctuations of the accelerometer and the magnetometer.<br/><br/>If you set the convergence speed to 0, practically only the gyroscope is used to calculate the orientation. This gives very smooth movements, but errors of the gyroscope will not be corrected. If you set the convergence speed to something above 500, practically only the magnetometer and the accelerometer are used to calculate the orientation. In this case the movements are abrupt and the values will fluctuate, but there won't be any errors that accumulate over time.<br/><br/>In an application with high angular velocities, we recommend a high convergence speed, so the errors of the gyroscope can be corrected fast. In applications with only slow movements we recommend a low convergence speed. You can change the convergence speed on the fly. So it is possible (and recommended) to increase the convergence speed before an abrupt movement and decrease it afterwards again.<br/><br/>You might want to play around with the convergence speed in the Brick Viewer to get a feeling for a good value for your application.<br/><br/>The default value is 30."
        },
        update_interval('Orientation', 'the orientation as euler angles'),
        update_interval('Quaternion', 'the orientation as quaternion'),
        update_interval('Acceleration', 'the acceleration'),
        update_interval('Magnetic Field', 'the magnetic field'),
        update_interval('Angular Velocity', 'the angular velocity'),
        ],
    'param_groups': oh_generic_channel_param_groups(),
    'init_code': """if(cfg.enableOrientation) {{
        this.orientationCalculationOn();
        this.setOrientationPeriod(cfg.orientationUpdateInterval);
    }} else {{
        this.orientationCalculationOff();
        this.setOrientationPeriod(0);
    }}
    this.setConvergenceSpeed(cfg.convergenceSpeed);
    this.setQuaternionPeriod(cfg.quaternionUpdateInterval);
    this.setAccelerationPeriod(cfg.accelerationUpdateInterval);
    this.setMagneticFieldPeriod(cfg.magneticFieldUpdateInterval);
    this.setAngularVelocityPeriod(cfg.angularVelocityUpdateInterval);
    """,
    'channels': [ {
            'predicate': 'cfg.enableOrientation',
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
            'divisor': '100.0',
            'is_trigger_channel': False
        } for angle in ['Roll', 'Pitch', 'Yaw']
    ] + [{
            'id': 'Quaternion {}'.format(axis.upper()),
            'type': 'Quaternion',
            'label': 'Quaternion - {}'.format(axis.upper()),

            'getters': [{
                'packet': 'Get Quaternion',
                'transform': 'new QuantityType(value.{}, {{unit}})'.format(axis.lower())}],

            'callbacks': [{
                'packet': 'Quaternion',
                'transform': 'new QuantityType({}, {{unit}})'.format(axis.lower())}],
            'java_unit': 'SmartHomeUnits.ONE',
            'is_trigger_channel': False
        } for axis in ['X', 'Y', 'Z', 'W']
    ] + [{
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
    ] + [{
            'id': 'Acceleration {}'.format(axis.upper()),
            'type': 'Acceleration',
            'label': 'Acceleration - {}'.format(axis.upper()),

            'getters': [{
                'packet': 'Get Acceleration',
                'transform': 'new QuantityType(value.{}{{divisor}}, {{unit}})'.format(axis.lower())}],

            'callbacks': [{
                'packet': 'Acceleration',
                'transform': 'new QuantityType({}{{divisor}}, {{unit}})'.format(axis.lower())}],
            'java_unit': 'SmartHomeUnits.STANDARD_GRAVITY',
            'divisor': 1000.0,
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
            'divisor': 1000000000.0,
            'is_trigger_channel': False
        } for axis in ['X', 'Y', 'Z']
    ] + [{
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
            'divisor': 14.375,
            'is_trigger_channel': False
        } for axis in ['X', 'Y', 'Z']
    ],
    'channel_types': [
        oh_generic_channel_type('Orientation', 'Number:Angle', 'NOT USED',
                     description='The current orientation (roll, pitch, yaw) of the IMU Brick as Euler angles in °. Note that Euler angles always experience a gimbal lock.<br/><br/>We recommend that you use quaternions instead.<br/><br/>The order to sequence in which the orientation values should be applied is roll, yaw, pitch.',
                     read_only=True,
                     pattern='%.2f %unit%'),
        oh_generic_channel_type('Quaternion', 'Number:Dimensionless', 'NOT USED',
                     description='The current orientation (x, y, z, w) of the IMU as quaternions.',
                     read_only=True,
                     pattern='%f %unit%'),
        oh_generic_channel_type('Acceleration', 'Number:Acceleration', 'NOT USED',
                     description='The calibrated acceleration from the accelerometer for the x, y and z axis in g (1g = 9.80665m/s²).',
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
        oh_generic_channel_type('Enable LEDs', 'Switch', 'Enable LEDs',
                     description='Enable/disable the orientation and direction LEDs of the IMU Brick.'),
    ]
}
