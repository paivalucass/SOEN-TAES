def check_smaller(test_tup1, test_tup2):
    for ele1, ele2 in zip(test_tup1, test_tup2):
        if ele2 >= ele1:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_check_smaller(self):
        self.assertEqual(check_smaller((1, 2, 3), (2, 3, 4)), False)

if __name__ == '__main__':
    unittest.main()