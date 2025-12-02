def count_Substrings(s):
    def calculate_sum_of_digits(sub):
        total = 0
        for digit in sub:
            total += int(digit)
        return total

    def count_substrings_with_sum_equal_length(s):
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if len(sub) == calculate_sum_of_digits(sub):
                    count += 1
        return count

    return count_substrings_with_sum_equal_length(s)
import unittest

class TestCountSubstrings(unittest.TestCase):
    def test_count_Substrings(self):
        self.assertEqual(count_Substrings('112112'), 6)

if __name__ == '__main__':
    unittest.main()