def number_of_substrings(s: str) -> int:
    length = len(s)
    return int(length * (length + 1) / 2)
import unittest

class Test(unittest.TestCase):
    def test_number_of_substrings(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()