def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    :param n: An integer representing the upper limit for summing numbers
    :type n: int
    :return: The sum of numbers from 1 to n
    :rtype: int
    """
    if not isinstance(n, int):
        raise ValueError("Input should be an integer")
    if n < 0:
        raise ValueError("Input should be a positive integer")
    return (n*(n+1)) // 2
import unittest

class Test(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()