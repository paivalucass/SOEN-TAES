def number_of_substrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if s[i:j]:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_number_of_substrings(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()