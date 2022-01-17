import unittest

from src.sw_dtoolkit.calculators.utils.random_entity_generator import RandomEntityGenerator

class TestRandomEntityGenerator(unittest.TestCase):

    def test_business_name(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_business_name()

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

    def test_random_person(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_person()

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

if __name__ == '__main__':
    unittest.main()
