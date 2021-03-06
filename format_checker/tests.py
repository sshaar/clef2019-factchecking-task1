from unittest import TestCase
from os.path import join, dirname

from format_checker import task1, task2

_ROOT_DIR = dirname(dirname(__file__))
_TEST_DATA_FOLDER = join(_ROOT_DIR, 'format_checker/data')


class FormatCheckerTask1(TestCase):
    _OK_FILES = ['task1_OK.txt']
    _NOT_OK_FILES = ['task1_NOTOK_0.txt', 'task1_NOTOK_MISSING_ID.txt', 'task1_NOTOK_DUP_LINE_NUM.txt']

    def test_ok(self):
        for _file in self._OK_FILES:
            self.assertTrue(task1.check_format(join(_TEST_DATA_FOLDER, _file)))

    def test_not_ok(self):
        for _file in self._NOT_OK_FILES:
            self.assertFalse(task1.check_format(join(_TEST_DATA_FOLDER, _file)))
