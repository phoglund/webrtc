#!/usr/bin/python

import os
import optparse
import subprocess
import sys

USAGE = """%prog"""


def main(port):
  jstestdriver_jar = os.path.join('node_modules', 'grunt-jstestdriver',
                                  'lib', 'jstestdriver.jar')
  jstestdriver_server = subprocess.Popen(
      ['java', '-jar', jstestdriver_jar, '--port', '%s' % port])
  try:
    firefox = subprocess.Popen(
        ['firefox', 'http://localhost:%s/capture' % port])
  except:
    jstestdriver_server.kill()
    raise

  print firefox.pid, "!"
  with open('jstestdriver.pid', 'w') as pidfile:
    pidfile.write(str(jstestdriver_server.pid))
  with open('firefox.pid', 'w') as pidfile:
    pidfile.write(str(firefox.pid))

if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    sys.exit(main(port=9875))
