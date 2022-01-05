# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one
from sw_dtoolkit.toolkit import SWToolkit

class TestToolkit(unittest.TestCase):

    def test_calc_list(self):
        toolkit = SWToolkit()

        toolkitRun1 = toolkit.listCalcs()

        self.assertEqual(toolkitRun1, 'hello from SWToolkit.listCalcs()')

    def test_calculate(self):
        toolkit = SWToolkit()

        toolkitRun1 = toolkit.calculate('test1', null)

        self.assertEqual(toolkitRun1, 'hello from TestCalculator1.calculate()')

if __name__ == '__main__':
    unittest.main()
