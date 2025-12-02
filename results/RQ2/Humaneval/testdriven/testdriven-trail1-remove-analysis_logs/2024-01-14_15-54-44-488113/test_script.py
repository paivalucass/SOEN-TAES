def make_a_pile(n):
    pile_of_stones = []
    for level in range(n):
        if n % 2 == 0:
            pile_of_stones.append(n + 2 * level - 1)
        else:
            pile_of_stones.append(n + 2 * level)
    return pile_of_stones
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()