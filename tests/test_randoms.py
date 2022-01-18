import unittest
from datetime import datetime, timedelta

from src.sw_dtoolkit.calculators.utils.random_entity_generator import RandomEntityGenerator

class TestRandomEntityGenerator(unittest.TestCase):

    def test_random_person(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_person()

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

    def test_random_address(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_address()

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

    def test_random_datetime(self):
        randomGen = RandomEntityGenerator()
        time_start = datetime.strptime('1/1/2032 1:30 PM', '%m/%d/%Y %I:%M %p')
        time_end = datetime.strptime('12/30/2099 4:50 AM', '%m/%d/%Y %I:%M %p')
        randomGenRun1 = randomGen.random_datetime(time_start, time_end)

        self.assertTrue(isinstance(randomGenRun1, datetime))

    def test_business_name(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_business_name()

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

    def test_business_industries(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_business_industries(3)

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

    def test_music_act(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_music_act()

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

    def test_music_genres(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_music_genres(3)

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

    def test_music_album(self):
        randomGen = RandomEntityGenerator()
        randomGenRun1 = randomGen.random_music_album(9)

        # check that strings are getting output
        self.assertTrue(type(randomGenRun1) == str)
        self.assertGreater(len(randomGenRun1), 0)

if __name__ == '__main__':
    unittest.main()
