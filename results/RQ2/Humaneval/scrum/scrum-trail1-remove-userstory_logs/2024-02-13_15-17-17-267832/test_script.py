def make_a_pile(n):
    pile = [n]
    for i in range(n-1):
        if n % 2 == 0:
            n += 2
        else:
            n += 2
        pile.append(n)
    return pile
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(1), [1])

if __name__ == '__main__':
    unittest.main()