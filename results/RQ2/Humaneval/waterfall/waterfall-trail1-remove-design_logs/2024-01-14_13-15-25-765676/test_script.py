def make_a_pile(n):
    pile = []
    if n % 2 == 0:
        for i in range(n):
            pile.append(n + 2 * i + 1)
    else:
        for i in range(n):
            pile.append(n + 2 * i)
    return pile
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()