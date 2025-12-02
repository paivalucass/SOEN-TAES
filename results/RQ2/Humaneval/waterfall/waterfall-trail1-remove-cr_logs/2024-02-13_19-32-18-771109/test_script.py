def make_a_pile(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    pile = [n]
    for i in range(1, n):
        if pile[i-1] % 2 == 0:
            next_stone = pile[i-1] + 1
        else:
            next_stone = pile[i-1] + 2
        pile.append(next_stone)
    return pile
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()