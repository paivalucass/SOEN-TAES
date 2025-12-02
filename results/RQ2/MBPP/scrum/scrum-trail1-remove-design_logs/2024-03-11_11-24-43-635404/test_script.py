def add_pairwise(test_tup):
    if len(test_tup) < 2:
        return "Input tuple should have at least 2 elements"
    return tuple(test_tup[i] + test_tup[i+1] for i in range(len(test_tup)-1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_pairwise((1, 5, 7, 8, 10)), (6, 12, 15, 18))

if __name__ == '__main__':
    unittest.main()