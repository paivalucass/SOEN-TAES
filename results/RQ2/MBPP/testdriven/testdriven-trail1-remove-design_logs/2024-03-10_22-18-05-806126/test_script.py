def count_reverse_pairs(test_list):
    count = 0
    for i in range(len(test_list)):
        for j in range(i+1, len(test_list)):
            if test_list[i][::-1] == test_list[j]:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]), 2)

if __name__ == '__main__':
    unittest.main()