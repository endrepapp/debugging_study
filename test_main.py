from main import *

from unittest import TestCase

class TestMain(TestCase):

    def test__main_is_callable(self):
        main()

    def test__prime_range1(self):
        expected = [2,3,5,7]
        result = give_primes(9)
        self.assertEqual(expected, result)

    def test__prime_factors1(self):
        expected = '2 * 5'
        result = prime_factors(10)
        self.assertEqual(expected, result)