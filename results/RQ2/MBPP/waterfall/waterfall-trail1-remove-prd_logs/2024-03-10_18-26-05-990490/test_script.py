def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        digit_sum = 0
        for j in range(i, len(s)):
            digit_sum += int(s[j])
            if digit_sum == (j - i + 1):
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_Substrings(self):
        self.assertEqual(count_Substrings('112112'), 6)

if __name__ == '__main__':
    unittest.main()