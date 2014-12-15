#!/usr/bin/python

import os
import optparse
import signal
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

  def TermHandler(signum, _):
    jstestdriver_server.kill()
    firefox.kill()

  signal.signal(signal.SIGTERM, TermHandler)
  try:
    firefox.wait()
  except:
    return 'Interrupted by user.'


if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    sys.exit(main(port=9875))
