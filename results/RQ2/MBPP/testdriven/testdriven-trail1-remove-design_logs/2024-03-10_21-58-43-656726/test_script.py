def find_length(string):
    max_diff = 0
    diff_map = {0: -1}
    count_0 = 0
    count_1 = 0
    for i, char in enumerate(string):
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1
        diff = count_0 - count_1
        if diff in diff_map:
            max_diff = max(max_diff, i - diff_map[diff])
        else:
            diff_map[diff] = i
    return max_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()