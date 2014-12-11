#!/usr/bin/python

import glob
import os
import optparse
import sys
import unittest

USAGE = """%prog SRC_DIR OUT_DIR
Generate js-test-driver config files, one for each test.

Assumes test files are named _test.js and that tests are stored together
with their source files.

SRC_DIR path to the javascript source.
OUT_DIR where to write output files.
"""


def _WriteOneFile(test_file, src_files, out_file_path):
  lines = []
  lines.append('load:')
  for src_file in src_files:
    lines.append('  - ' + src_file)
  lines.append('test:')
  lines.append('  - ' + test_file)
  lines.append('  - samples/web/js/jsunit_adapter.js')

  with open(out_file_path, 'w') as out_file:
    out_file.write('\n'.join(lines))


def main(src_dir, out_dir):
  test_files = glob.glob(os.path.join(src_dir, '*_test.js'))
  if not test_files:
    return 'Found no tests in %s.' % src_dir
  
  src_files = glob.glob(os.path.join(src_dir, '*.js'))
  src_files = [src_file for src_file in src_files
               if not src_file.endswith('_test.js')]

  if not src_files:
    return 'Found no non-test js files in %s.' % src_dir

  for test_file in test_files:
    test_filename = os.path.splitext(os.path.basename(test_file))[0]
    out_file_path = os.path.join(out_dir, test_filename + '_jstestdriver.conf')
    _WriteOneFile(test_file, src_files, out_file_path)


if __name__ == '__main__':
  parser = optparse.OptionParser(USAGE)
  options, args = parser.parse_args()
  if len(args) != 2:
    print 'Error: Exactly 2 arguments required.'
    parser.print_help()
    sys.exit(1)
    
  sys.exit(main(src_dir=args[0], out_dir=args[1]))
