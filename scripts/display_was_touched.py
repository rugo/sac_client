#!/opt/sac/bin/python
import os
import sys

if os.getuid() != 0:
    sys.stderr.write("Only root can to this.\n")
    sys.exit(2)

from sacpython import displaytouched

if not displaytouched():
    sys.exit(1)
