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
        logger.info('options')

    def configure(self, options, conf):
        logger.info('configure')
        super(NoseGradePlugin, self).configure(options, conf)
        if not self.enabled:
            return

    def startTest(self, test):
        logger.info('start test')
        grade.util.init_test_stats()

    def stopTest(self, test):
        logger.info('stop test')
        grade.util.update_stats()

    def report(self, stream):
        logger.info('report')
        grade.util.print_stats()
