def count_reverse_pairs(test_list):
    reverse_count = 0
    reverse_map = {}
    
    for word in test_list:
        reverse_word = word[::-1]
        if reverse_word in reverse_map:
            reverse_count += reverse_map[reverse_word]
        reverse_map[word] = reverse_map.get(word, 0) + 1
    
    return reverse_count
import unittest

class Test(unittest.TestCase):
    def test_count_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]), 2)

if __name__ == '__main__':
    unittest.main()