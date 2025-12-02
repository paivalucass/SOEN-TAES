def split_two_parts(list1, L):
    if len(list1) < L:
        return ([], list1)
    else:
        return (list1[:L], list1[L:])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()