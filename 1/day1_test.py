import unittest

from day1 import fuel_counter


# python -m unittest day1_test.py
class FuelTestCase(unittest.TestCase):
    def test_mass_to_fuel(self):
        masses = [12, 14, 1969, 100756]
        output_fuel = [2, 2, 654, 33583]

        for i in range(len(masses)):
            assert fuel_counter(masses[i]) == output_fuel[i]
