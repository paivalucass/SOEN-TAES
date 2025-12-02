def len_log(list1):
    return max(len(word) for word in list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python","PHP","bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()