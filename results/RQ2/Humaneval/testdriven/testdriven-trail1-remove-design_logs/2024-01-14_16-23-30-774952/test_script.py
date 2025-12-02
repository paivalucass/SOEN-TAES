def make_a_pile(n):
    if n <= 0 or type(n) != int or n > 1000000000:
        return "Invalid Input"
    stones = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones.append(n + 2 * i)
        else:
            stones.append(n + 2 * i + 1)
    return stones
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()