def dog_age(h_age):
    return h_age * 5
import unittest

class Test(unittest.TestCase):
    def test_dog_age(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()