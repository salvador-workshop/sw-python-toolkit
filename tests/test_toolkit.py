# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

    # from sample.simple import add_one
from src.sw_dtoolkit.toolkit import SWDToolkit

class TestToolkit(unittest.TestCase):

    def test_calc_list(self):
        toolkit = SWDToolkit()
        toolkitRun1 = toolkit.listCalcs()

        self.assertEqual(toolkitRun1, 'hello from SWDToolkit.listCalcs()')

    def test_calculate(self):
        toolkit = SWDToolkit()
        toolkitRun1 = toolkit.calculate('test1', None)
        toolkitRun2 = toolkit.calculate('test2', None)

        self.assertEqual(toolkitRun1, 'hello from TestCalculator1.calculate()')
        self.assertEqual(toolkitRun2, 'hello from TestCalculator2.calculate()')

if __name__ == '__main__':
    unittest.main()
