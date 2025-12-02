def count_reverse_pairs(test_list):
    count = 0
    reverse_dict = {}
    if not test_list or not all(isinstance(s, str) for s in test_list):
        return 0
    for s in test_list:
        if s[::-1] in reverse_dict and s != s[::-1]:
            count += reverse_dict[s[::-1]]
        reverse_dict[s] = reverse_dict.get(s, 0) + 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]), 2)

if __name__ == '__main__':
    unittest.main()