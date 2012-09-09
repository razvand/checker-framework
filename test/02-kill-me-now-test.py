"""
Check if user exists.
"""

import sys
import os
import grade

def init():
    print os.path.basename(__file__), ": init"

def test():
    grade.set_test_total(5)
    print os.path.basename(__file__), ": test"
    grade.set_test_grade(5)

def cleanup():
    print os.path.basename(__file__), ": cleanup"

test.setUp = init
test.tearDown = cleanup
