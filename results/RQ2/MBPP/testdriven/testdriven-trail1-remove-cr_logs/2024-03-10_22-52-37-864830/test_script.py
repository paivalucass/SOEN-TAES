def pair_wise(l1):
    pairs = []
    for i in range(len(l1) - 1):
        pairs.append((l1[i], l1[i + 1]))
    return pairs
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_wise([1,1,2,3,3,4,4,5]), [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)])

if __name__ == '__main__':
    unittest.main()