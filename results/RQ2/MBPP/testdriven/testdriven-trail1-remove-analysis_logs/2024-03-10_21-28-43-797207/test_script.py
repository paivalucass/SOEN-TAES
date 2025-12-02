def count_reverse_pairs(test_list):
    count = 0
    reverse_set = set()
    for string in test_list:
        if string[::-1] in reverse_set:
            count += 1
            reverse_set.remove(string[::-1])
        else:
            reverse_set.add(string)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]), 2)

if __name__ == '__main__':
    unittest.main()