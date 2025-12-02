def len_log(word_list):
    if not isinstance(word_list, list) or len(word_list) == 0:
        return 0
    longest_word_length = max(len(word) for word in word_list)
    return longest_word_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python","PHP","bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()