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

import subprocess
import os
import traceback
from urllib.parse import urlparse

def git(cmd, params):
    if cmd is None:
        return
    cmds = ['git', cmd]
    if not params is None:
        cmds.extend(params)
    subprocess.check_call(cmds)

def wget_extract(url, tmp_dir='.', dst_path='.', timeout=20):
    '''Gets a file using wget and then extracts the tar file.
    '''
    print('wget_extract: START timeout={} url={} to dst_path={}'.format(timeout, url, dst_path))
    dst_path = os.path.abspath(dst_path)
    tmp_dir = os.path.abspath(tmp_dir)
    os.makedirs(tmp_dir, exist_ok=True)
    wgetdst_filename = 'wget.tmp'
    wgetdst_path = os.path.join(tmp_dir, wgetdst_filename)
    if os.path.exists(wgetdst_path):
        os.remove(wgetdst_path)
    print('wget: get timeout={} url={} wgetdst_path={}'.format(timeout, url, wgetdst_path))
    p = subprocess.Popen('wget --timeout={} -qO- {} > {}'.format(timeout, url, wgetdst_path), shell=True)
    os.waitpid(p.pid, 0)
    os.makedirs(dst_path, exist_ok=False)
    print('wget: extract wgetdst_path={} dst_path={}'.format(wgetdst_path, dst_path))
    subprocess.check_call(['tar', '-xf', wgetdst_path, '--strip-components=1', '-C', dst_path])
    os.remove(wgetdst_path)
    print('wget_extract: DONE timeout={} url={} to dst_path={}'.format(timeout, url, dst_path))

def bash(cmd, stdout=None, stderr=None):
    if cmd is None:
        return
    print('bash: cmd=', cmd)

    subprocess.run(['bash', '-c', cmd],
            stdout=stdout,
            stderr=stderr,
            check=True)

def bashPython2(cmd, stdout=None, stderr=None):
    bash(('[ ! -d venv2 ] && virtualenv --python=/usr/bin/python2 venv2; ' +
          'source venv2/bin/activate; ' +
          '{c}').format(c=cmd),
         stdout, stderr)
