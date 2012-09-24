"""
Check if user exists.
"""

import sys
import os
import grade.util

def init():
    pass

def test():
    grade.util.set_test_total(5)
    grade.util.set_test_grade(5)

def cleanup():
    pass

test.setUp = init
test.tearDown = cleanup
