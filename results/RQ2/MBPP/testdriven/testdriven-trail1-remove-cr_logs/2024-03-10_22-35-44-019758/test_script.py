def dog_age(h_age):
    if type(h_age) != int or h_age < 0:
        return "Invalid input"
    elif h_age == 0:
        return 0
    elif h_age < 3:
        return h_age * 10.5
    else:
        return 21 + (h_age - 2) * 4

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dog_age(12), 61)

if __name__ == '__main__':
    unittest.main()