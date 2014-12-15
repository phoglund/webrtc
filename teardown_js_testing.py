#!/usr/bin/python

import os
import signal
import sys

USAGE = """%prog"""


def _Kill(pid_path):
  if not os.path.exists(pid_path):
    return
  with open(pid_path, 'r') as pid_file:
    try:
      pid = int(pid_file.read())
      os.kill(pid, signal.SIGTERM)
    except:
      print 'Failed to kill %s, ignoring error.' % pid_path
  
  os.remove(pid_path)


def main():
  _Kill('jstestdriver.pid')
  _Kill('firefox.pid')


if __name__ == '__main__':
    sys.exit(main())
