"""
Checker Framework

Nose plugin for grading tests.
"""

import sys
import os
import logging
import nose.plugins
import grade.util

logger = logging.getLogger('nose.plugins')
logger.setLevel(logging.ERROR)

class NoseGradePlugin(nose.plugins.Plugin):
    name = 'grade-plugin'

    def options(self, parser, env=os.environ):
        super(NoseGradePlugin, self).options(parser, env=env)

    def configure(self, options, conf):
        super(NoseGradePlugin, self).configure(options, conf)
        if not self.enabled:
            return

    def prepareTestResult(self, result):
        #Monkey patch the TextTestResult to not print
        #it's summary.
        result.dots = False
        def _mpPrintSummary(start, stop):
            pass
        result.printSummary = _mpPrintSummary

    def startTest(self, test):
        grade.util.init_test_stats()

    def stopTest(self, test):
        grade.util.update_stats()
        grade.util.print_test_stats(test.id())

    def report(self, stream):
        grade.util.print_stats()
