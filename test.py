try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser
import argparse
import contextlib
import datetime

import re
import os

import requests

import signal
import subprocess
import time
import traceback
import xmlrpc.client


def log(*args):
    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print('')
    print(ts)
    print(('saas.py >>> ' + ', '.join([str(a) for a in args])))