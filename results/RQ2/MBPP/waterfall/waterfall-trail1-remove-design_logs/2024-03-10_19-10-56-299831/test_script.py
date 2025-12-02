def dog_age(h_age):
    if h_age <= 0:
        return "Error: Invalid input age"
    else:
        return h_age * 7
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()