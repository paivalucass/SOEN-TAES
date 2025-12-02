def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    """
    if not isinstance(n, int) or n < 2:
        return 1
    for i in range(int(n**0.5), 1, -1):
        if n % i == 0:
            return i
    return 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()