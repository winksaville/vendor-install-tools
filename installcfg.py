# Copyright (C) 2015 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import installlib

installlib.register('ninja', 'installers/ninja.py', version='1.6.0')
installlib.register('meson', 'installers/meson.py', version='0.27.0')
installlib.register('qemu', 'installers/qemu.py', version='2.4.91', co_version='2.5.0-rc1')
installlib.register('binutils', 'installers/binutils.py', version='2.25.1', cross_dir='cross', target='arm-eabi')
installlib.register('gcc', 'installers/gcc.py', version='5.2.0', cross_dir='cross', target='arm-eabi',
  gmp_version='6.0.0a', mpfr_version='3.1.3', mpc_version='1.0.3')
