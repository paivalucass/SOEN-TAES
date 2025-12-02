def dog_age(h_age: int) -> int:
    dog_years = h_age * 5 + 1
    return dog_years
import unittest

class TestDogAge(unittest.TestCase):
    def test_dog_age(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()