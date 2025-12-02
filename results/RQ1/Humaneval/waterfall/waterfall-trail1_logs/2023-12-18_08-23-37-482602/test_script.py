def make_a_pile(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    pile = [2*i + 1 for i in range(n)]

    return [n + sum(pile[:i]) for i in range(1, n+1)]
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(1), [1])

if __name__ == '__main__':
    unittest.main()