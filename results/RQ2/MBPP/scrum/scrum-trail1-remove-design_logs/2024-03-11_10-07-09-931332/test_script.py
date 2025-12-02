def find_length(string):
    max_diff = 0
    count_0 = 0
    count_1 = 0
    for char in string:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1
        max_diff = max(max_diff, count_0 - count_1)
        if count_0 < count_1:
            count_0 = 0
            count_1 = 0
    return max_diff
import unittest

class Test(unittest.TestCase):
    def test_find_length(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()