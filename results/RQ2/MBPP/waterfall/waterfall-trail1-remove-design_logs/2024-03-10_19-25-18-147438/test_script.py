def count_reverse_pairs(test_list):
    count = 0
    reverse_map = {}
    for item in test_list:
        reverse = item[::-1]
        if reverse in reverse_map:
            count += reverse_map[reverse]
        if item in reverse_map:
            reverse_map[item] += 1
        else:
            reverse_map[item] = 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]), 2)

if __name__ == '__main__':
    unittest.main()