#!/usr/bin/env python3

# Copyright 2015 wink saville
#
# licensed under the apache license, version 2.0 (the "license");
# you may not use this file except in compliance with the license.
# you may obtain a copy of the license at
#
#     http://www.apache.org/licenses/license-2.0
#
# unless required by applicable law or agreed to in writing, software
# distributed under the license is distributed on an "as is" basis,
# without warranties or conditions of any kind, either express or implied.
# see the license for the specific language governing permissions and
# limitations under the license.

# Install all or a specific set of the vendor tools

import parseinstallargs
import ninja_install
import meson_install
import crosstool_ng_install
import ct_ng_runner
import binutils_install
import gcc_install
import qemu_install

import argparse
import sys
import os
import subprocess
import argparse

all_apps = ['ninja', 'meson',
        #'binutils-i586-elf', 'binutils-arm-eabi',
        #'gcc-i586-elf', 'gcc-arm-eabi',
        'ct-ng',
        'gcc-x86_64', 'gcc-i386', 'gcc-arm',
        'qemu-system-arm']

args = parseinstallargs.InstallArgs('all', apps=all_apps)

if len(args.apps) == 0:
    args.print_help()
    sys.exit(0)

if 'all' in args.apps:
    args.apps = all_apps

cwd = os.getcwd();
# Install the apps
for app in args.apps:
    # Start in the current directory
    os.chdir(cwd)
    if app == 'ninja':
        installer = ninja_install.Installer()
        installer.install()
    elif app == 'meson':
        installer = meson_install.Installer()
        installer.install()
    elif app == 'ct-ng':
        installer = crosstool_ng_install.Installer()
        installer.install()
    elif app == 'binutils-arm-eabi':
        installer = binutils_install.Installer(defaultTarget='arm-eabi')
        installer.install()
    elif app == 'binutils-i586-elf':
        installer = binutils_install.Installer(defaultTarget='i586-elf')
        installer.install()
    elif app == 'gcc-arm-eabi':
        installer = gcc_install.Installer(defaultTarget='arm-eabi')
        installer.install()
    elif app == 'gcc-i586-elf':
        installer = gcc_install.Installer(defaultTarget='i586-elf')
        installer.install()
    elif app == 'gcc-x86_64':
        builder = ct_ng_runner.Builder(defaultTarget='x86_64-unknown-elf')
        builder.build()
    elif app == 'gcc-i386':
        builder = ct_ng_runner.Builder(defaultTarget='i386-unknown-elf')
        builder.build()
    elif app == 'gcc-arm':
        builder = ct_ng_runner.Builder(defaultTarget='arm-unknown-eabi')
        builder.build()
    elif app == 'qemu-system-arm':
        installer = qemu_install.Installer()
        installer.install()
    else:
        print('Unknown app:', app)
        sys.exit(1)
