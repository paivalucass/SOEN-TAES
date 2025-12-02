def len_log(list1):
    longest_word_length = 0
    for word in list1:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python","PHP","bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()