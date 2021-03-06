"""
Checker Framwork

Manage grading stats.
"""

import sys
import StringIO

GRADE = 0
TOTAL = 0

test_grade = 0
test_total = 0

def init_test_stats():
    global test_grade
    global test_total
    test_grade = 0
    test_total = 0

def set_test_total(total):
    global test_total
    test_total = total

def set_test_grade(grade):
    global test_grade
    test_grade = grade

def update_stats():
    global GRADE
    global TOTAL
    GRADE += test_grade
    TOTAL += test_total

def print_test_stats(testname):
    """Print test grading stats.
    """
    length = len(testname)
    if length > 40:
        length = 40
        testname = testname[:40]
    rest = 63 - length
    print testname,
    for i in range(1, rest):
        sys.stdout.write('.')
    print '{:3d}/{:3d}'.format(test_grade, test_total)

def print_stats():
    """Print overall grading stats.
    """
    print '{:>60}: {:3d}/{:3d}'.format('Total', GRADE, TOTAL)
