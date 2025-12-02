def make_a_pile(n):
    pile = []
    for i in range(n):
        if n % 2 == 1:
            pile.append(n + 2*i)
        else:
            pile.append(n + 2*i + 1)
    return pile
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()