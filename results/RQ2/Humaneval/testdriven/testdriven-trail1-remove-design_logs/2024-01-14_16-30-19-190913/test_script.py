def make_a_pile(n):
    pile = [n]
    for i in range(1, n):
        if pile[0] % 2 == 0:
            pile.append(pile[-1] + 2 * i)
        else:
            pile.append(pile[-1] + 2 * i + 1)
    return pile
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()