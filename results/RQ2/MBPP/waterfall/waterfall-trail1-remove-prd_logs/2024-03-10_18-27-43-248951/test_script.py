def len_log(list1):
    max_length = 0
    if not isinstance(list1, list):
        return "Error"
    if len(list1) == 0:
        return 0
    for word in list1:
        if len(word) > max_length:
            max_length = len(word)
    return max_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python","PHP","bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()