#!/usr/bin/env python
"""This module is a CLI Application to build help and snippets
for you to remember while in terminal.
"""
from __future__ import print_function
import os
import sys

# Current Version
VERSION=0.01

# Path to topic files
PATH_TOPICS = 'topics'

# Get the CLI Args
if len(sys.argv) == 1:
    print("""
    Please pass two (2) arguments:
      - arg1: name of a topic file (try: demo).
      - arg2: name of a method within the topic file (try: basic)

    Usage   $ ./ci_help.py <command> <argument>
    Example $ ./cli.py demo basic
    """)
    sys.exit()
elif len(sys.argv) == 2:
    """
    @TODO:  Allow one arg only, and list out the method names
            for the topic.
    """
elif len(sys.argv) <= 2:
    # We want three arguments contain [scriptname, arg1, arg2]
    print('Please provide two arguments: <service> <command>')
    sys.exit()

# Assign Service and Command, lowercase is safecase!
ARG_SERVICE = sys.argv[1].lower()
ARG_COMMAND = sys.argv[2].lower()

# The module we hope to import
IMPORT_MODULE = '%s.%s' % (PATH_TOPICS, ARG_SERVICE)

# List Topics In Order: [__init__, git, etc]
AVAILABLE_TOPICS = sorted([
    # Strip the *.py Extensions for our list
    os.path.splitext(x)[0] for x in os.listdir(PATH_TOPICS)
])

# Make sure the TOPIC exists
if ARG_SERVICE not in AVAILABLE_TOPICS:
    print("Sorry, the topic %s is not available." % ARG_SERVICE)
    sys.exit()

if ARG_SERVICE in AVAILABLE_TOPICS:
    REAL_SERVICE = __import__(IMPORT_MODULE, fromlist=[''])

    # Make sure we have the ARG_COMMAND
    if not hasattr(REAL_SERVICE, ARG_COMMAND):
        print('Sorry, the topic %s has no command: %s' % ARG_COMMAND)
        sys.exit()

    # Process the Command
    RUN_METHOD = getattr(REAL_SERVICE, ARG_COMMAND)
    RESULT = RUN_METHOD()

    # Get Result Type
    result_type = None
    if isinstance(RESULT, dict):
        result_type = 'dict'
    elif isinstance(RESULT, str) and len(RESULT) != 0:
        result_type = 'str'

    # Set Flags
    ran_flags = False
    ran_commands = False
    ran_plain = False

    # Display based on type:
    if result_type is 'dict':
        # Print Out: flags
        if 'flags' in RESULT:
            ran_flags = True
            print("Flags:" + RESULT['flags'])

        # Print Out: commands
        if 'commands' in RESULT:
            ran_commands = True
            print("Commands:" + RESULT['commands'])
            sys.exit()
    elif result_type is 'str':
        # Print Out: Plain text
        if len(RESULT) != 0:
            ran_plain = True
            print(RESULT)
            sys.exit()

    # No Results
    print('No information returned from: $%s.%s' % (ARG_SERVICE, ARG_COMMAND))
    sys.exit()
