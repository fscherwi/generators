#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
C/C++ Bindings Tester
Copyright (C) 2012-2018 Matthias Bolte <matthias@tinkerforge.com>

test_c_bindings.py: Tests the C/C++ bindings

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

import sys
import os
import glob
import shutil

sys.path.append(os.path.split(os.getcwd())[0])
import common

class CExamplesTester(common.Tester):
    def __init__(self, root_dir, compiler, extra_paths):
        common.Tester.__init__(self, 'c', '.c', root_dir, comment=compiler, extra_paths=extra_paths)

        self.compiler = compiler

    def test(self, cookie, path, extra):
        uses_libgd = False

        with open(path, 'r') as f:
            uses_libgd = '#include <gd.h>' in f.read()

        # skip OLED scribble example because mingw32 has no libgd package
        if self.compiler.startswith('mingw32-') and uses_libgd:
            self.handle_result(cookie, 0, '>>> skipping')
            return

        if extra:
            shutil.copy(path, '/tmp/tester/c')
            path = os.path.join('/tmp/tester/c', os.path.split(path)[1])

        output = path[:-2]

        if not extra and '/brick' in path:
            dirname = os.path.split(path)[0]
            device = '/tmp/tester/c/source/{0}_{1}.c'.format(os.path.split(os.path.split(dirname)[0])[-1], os.path.split(dirname)[-1])
        else:
            device = ''

        args = []

        if self.compiler == 'gcc':
            args += ['gcc', '-std=c99', '-pthread']
        elif self.compiler == 'g++':
            args += ['g++', '-std=c++98', '-pthread']
        elif self.compiler == 'mingw32-gcc':
            args += ['x86_64-w64-mingw32-gcc', '-Wno-error=return-type']
        elif self.compiler == 'mingw32-g++':
            args += ['x86_64-w64-mingw32-g++', '-Wno-error=return-type']
        elif self.compiler == 'clang':
            args += ['clang', '-std=c99', '-pthread']
        elif self.compiler == 'scan-build clang':
            args += ['scan-build', 'clang', '-std=c99', '-pthread']
        else:
            raise common.GeneratorError('Invalid compiler ' + self.compiler)

        args += ['-Wall',
                 '-Wextra',
                 '-Werror',
                 '-O2',
                 '-I/tmp/tester/c/source',
                 '-o',
                 output,
                 '/tmp/tester/c/source/ip_connection.c']

        if len(device) > 0:
            args.append(device)
        elif extra:
            dependencies = glob.glob('/tmp/tester/c/source/*.c')
            dependencies.remove('/tmp/tester/c/source/ip_connection.c')
            args.append('-Wno-error=unused-parameter')
            args += dependencies

        args.append(path)

        if self.compiler.startswith('mingw32-'):
            args += ['-lws2_32']

        if uses_libgd:
            args += ['-lm', '-lgd']

        self.execute(cookie, args)

    def check_success(self, exit_code, output):
        if self.compiler == 'scan-build clang' and exit_code == 0 and 'scan-build: No bugs found.\n' not in output:
            return False

        return exit_code == 0

def run(root_dir):
    extra_paths = [os.path.join(root_dir, '../../weather-station/write_to_lcd/c/weather_station.c'),
                   os.path.join(root_dir, '../../hardware-hacking/remote_switch/c/remote_switch.c'),
                   os.path.join(root_dir, '../../hardware-hacking/smoke_detector/c/smoke_detector.c')]

    if not CExamplesTester(root_dir, 'gcc', extra_paths).run():
        return False

    if not CExamplesTester(root_dir, 'g++', extra_paths).run():
        return False

    if not CExamplesTester(root_dir, 'mingw32-gcc', extra_paths).run():
        return False

    if not CExamplesTester(root_dir, 'mingw32-g++', extra_paths).run():
        return False

    if not CExamplesTester(root_dir, 'clang', extra_paths).run():
        return False

    return CExamplesTester(root_dir, 'scan-build clang', extra_paths).run()

if __name__ == '__main__':
    run(os.getcwd())
