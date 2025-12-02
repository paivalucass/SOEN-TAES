def dog_age(h_age):
    dog_years = 0
    if h_age <= 2:
        dog_years = h_age * 10.5
    else:
        dog_years = 21 + (h_age - 2) * 4
    return round(dog_years)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()