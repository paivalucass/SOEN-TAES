def make_a_pile(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    
    stones = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones.append(n + i)
        else:
            stones.append(n + 2 * i)
    
    return stones
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()