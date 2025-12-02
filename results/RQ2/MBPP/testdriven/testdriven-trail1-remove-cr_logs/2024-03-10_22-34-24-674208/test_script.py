def number_of_substrings(s): 
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            count += 1
    return count

assert number_of_substrings("abc") == 6
import unittest

class Test(unittest.TestCase):
    def test_number_of_substrings(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()