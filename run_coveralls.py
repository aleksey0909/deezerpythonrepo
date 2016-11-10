#!/bin/env/python
# -*- coding: utf-8

import os

from subprocess import call

if __name__ == '__main__':
    if 'TRAVIS' in os.environ:
        rc = call('coveralls')
        raise SystemExit(rc)
