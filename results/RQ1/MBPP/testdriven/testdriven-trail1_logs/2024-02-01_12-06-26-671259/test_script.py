def find_length(string):
    def find_substrings(string):
        substrings = []
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                substrings.append(string[i:j])
        return substrings

    def count_zeros_ones(substring):
        count_0 = substring.count('0')
        count_1 = substring.count('1')
        return count_0 - count_1

    def max_difference(string):
        if not string:
            return 0
        substrings = find_substrings(string)
        max_diff = 0
        for substr in substrings:
            diff = count_zeros_ones(substr)
            max_diff = max(max_diff, diff)
        return max_diff

    return max_difference(string)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()