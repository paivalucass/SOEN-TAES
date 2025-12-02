def make_a_pile(n):
    pile = []
    stones = n
    for i in range(n):
        pile.append(stones)
        if stones % 2 == 0:
            stones += 2
        else:
            stones += 1
    return pile
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])

if __name__ == '__main__':
    unittest.main()