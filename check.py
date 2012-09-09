"""
Checker Framework

Top level checker module. Goes through checkers/tests and prints out percentage
of passed tests.
"""

import sys
import os
import pkgutil
import importlib
import grade.util

# folder where checkers/tests are stored
TEST_FOLDER = "test"

def main():
    """Sample usage:
    python check.py

    Goes through all tests in TEST_FOLDER and runs them. Update grading stats
    accordingly.
    """

    test_folder_path = os.path.join(os.path.dirname(__file__), TEST_FOLDER)

    # Go through all modules in TEST_FOLDER.
    for f in os.listdir(test_folder_path):
        if f == '__init__.py' or f == '__init__.pyc' or f[-3:] != '.py':
            continue

        # Retrive module from module name.
        module_name = f[:-3]
        module = importlib.import_module('test.%s' % (module_name))

        # Retrive checker functions and call them.
        init_function = getattr(module, 'init')
        test_function = getattr(module, 'test')
        cleanup_function = getattr(module, 'cleanup')

        grade.util.init_test_stats()
        init_function()
        test_function()
        cleanup_function()
        grade.util.update_stats()
        grade.util.print_test_stats(module_name)

    grade.util.print_stats()   # Print grading stats.


if __name__ == "__main__":
    sys.exit(main())
