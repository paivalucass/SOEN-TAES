def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1]:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()