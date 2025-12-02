def pair_wise(l1):
    if len(l1) < 2:
        return "Input list should have at least two elements"

    pairs = [(l1[i-1], l1[i]) for i in range(1, len(l1))]

    return pairs
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_wise([1,1,2,3,3,4,4,5]), [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)])

if __name__ == '__main__':
    unittest.main()