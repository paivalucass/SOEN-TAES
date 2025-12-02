def len_log(wordList):
    if not isinstance(wordList, list):
        return "Invalid Input Type Error"
    if not wordList:
        return "Empty List Error"
    if all(isinstance(word, str) for word in wordList):
        longest_word_length = max(len(word) for word in wordList)
        return longest_word_length
    else:
        return "Invalid Input Type Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python","PHP","bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()