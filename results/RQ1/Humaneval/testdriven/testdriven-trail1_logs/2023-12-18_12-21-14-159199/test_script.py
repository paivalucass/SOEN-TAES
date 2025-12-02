def largest_divisor(n: int) -> int:
    """
    Find the largest proper divisor of a given number
    :param n: int
    :return: int
    """
    if n <= 0:
        return 1
    if n == 1:
        return 1
    largest_div = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            largest_div = i
    if n % (n // largest_div) == 0:
        return n // largest_div
    return largest_div
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()