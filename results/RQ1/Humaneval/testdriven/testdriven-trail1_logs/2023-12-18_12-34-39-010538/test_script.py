def make_a_pile(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    stone_levels = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stone_levels.append(n + 2*i)
        else:
            stone_levels.append(n + 2*i - 1)

    return stone_levels
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(1), [1])

if __name__ == '__main__':
    unittest.main()