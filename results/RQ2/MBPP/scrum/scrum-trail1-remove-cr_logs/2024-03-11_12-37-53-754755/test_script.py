def len_log(list1):
    if not isinstance(list1, list):
        return "Error: Input is not a list"
    if not list1:
        return 0
    
    max_len = 0
    for word in list1:
        if isinstance(word, str) and word.isalpha() and len(word) > max_len:
            max_len = len(word)
    
    return max_len
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python","PHP","bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()