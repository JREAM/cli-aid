#!/usr/bin/env python
import sys
import os

# @ TODO Thoughts:
# ----------------
# Install to /usr/local/bin/hlp, otherwise probably:
#   I don't think it should be here, it's just a removable CLI tool
#
# For PIP Package: Install to ~/.local/lib/python2.X/sites-packages
#   I don't think it needs to be PIP
#
# For Friendly Use:
# ln -s /where-its-located/cmd_help.py /local/usr/bin/cmd_help
# or
# ln -s /where-its-located/cmd_help.py /local/usr/bin/hlp
# or
# .bashrc alias hlp='/location/cmd_help.py $1 $2' but then it's limited
#   to two args if it's upgraded.

# Allows the path to iterate
SYSTEM_PATH = sys.path
sorted(SYSTEM_PATH)
SYSTEM_PATH.pop(0)

# User HOME Path
PATH_HOME = os.environ['HOME']

# Get Python Version
MAJOR = sys.version_info[0]
MINOR = sys.version_info[1]
MICRO = sys.version_info[2]

PYTHON_VERSION = "python%s.%s" % (MAJOR, MINOR)

# See if Install Path exists
INSTALL_PATH = "%s/.local/lib/%s/site-packages/" % (PATH_HOME, PYTHON_VERSION)


# Check the PATH variable
if INSTALL_PATH not in SYSTEM_PATH:
    print "Error, missing the following in PATH:\n  %s" % INSTALL_PATH
    print "\nYour PATH contains:"
    print "\n  ".join(sys.path)
    sys.exit(0)

# Check for path
if not os.path.exists(INSTALL_PATH):
    print "Error, could locate and install to %s" % INSTALL_PATH
    sys.exit(0)


# Install To Path
# @ TODO here
#
# ...
