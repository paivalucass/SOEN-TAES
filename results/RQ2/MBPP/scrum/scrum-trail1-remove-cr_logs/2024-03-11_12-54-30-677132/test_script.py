def number_of_substrings(str):
    substr_count = 0
    for i in range(len(str)):
        for j in range(i, len(str)):
            substr_count += 1
    return substr_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()