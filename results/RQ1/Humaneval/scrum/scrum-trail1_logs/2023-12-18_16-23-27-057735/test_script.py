def make_a_pile(n):
    pile = []
    for i in range(1, n+1):
        if n % 2 == 0:
            pile.append(i * 2 + n - 1)
        else:
            pile.append(i * 2 + n - 2)
    return pile
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()