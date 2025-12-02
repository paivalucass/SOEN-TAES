def number_of_substrings(input_string):
    count = 0
    n = len(input_string)
    for i in range(n):
        for j in range(i, n):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_number_of_substrings(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()