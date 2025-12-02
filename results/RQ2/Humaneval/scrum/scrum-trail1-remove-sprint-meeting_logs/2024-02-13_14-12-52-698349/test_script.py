def make_a_pile(n):
    stones = []
    for i in range(n):
        stones.append(n + 2*i)
    return stones
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()