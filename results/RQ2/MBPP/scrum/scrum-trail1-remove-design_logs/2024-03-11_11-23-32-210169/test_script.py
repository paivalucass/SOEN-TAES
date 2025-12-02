def number_of_substrings(s):
    if not isinstance(s, str):
        raise TypeError("Input should be a string")

    if len(s) == 0:
        return 0

    return int(len(s) * (len(s) + 1) / 2)
import unittest

class Test(unittest.TestCase):
    def test_number_of_substrings(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()