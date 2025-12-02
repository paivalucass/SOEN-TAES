def count_reverse_pairs(test_list):
    count = 0
    reverse_pairs = {}
    for word in test_list:
        reverse_word = word[::-1]
        if reverse_word in reverse_pairs:
            count += reverse_pairs[reverse_word]
        if word in reverse_pairs:
            reverse_pairs[word] += 1
        else:
            reverse_pairs[word] = 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]), 2)

if __name__ == '__main__':
    unittest.main()