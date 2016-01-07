#!/opt/sac/bin/python
import sys

from sacpython import displaytouched

if not displaytouched():
    sys.exit(1)
