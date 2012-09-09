"""
Checker Framework

Use nose to run tests. Use NoseGradePlugin to compute test grades.
"""

import sys
import os
import nose
import grade.plugin

# folder where checkers/tests are stored
TEST_FOLDER = "test"

def main():
    """Sample usage:
    python nose-check.py

    Uses nose to go through all tests in TEST_FOLDER and run them. Use
    NoseGradePlugin to compute grades accordingly.
    """
    nose.main(defaultTest=TEST_FOLDER,
            argv=['nose-check.py', '-s', '--with-grade-plugin'],
            addplugins=[grade.plugin.NoseGradePlugin()])

if __name__ == "__main__":
    sys.exit(main())
