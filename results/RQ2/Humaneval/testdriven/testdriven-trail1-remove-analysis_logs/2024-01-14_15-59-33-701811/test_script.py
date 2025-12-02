def is_equal_to_sum_even(n):
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if type(n) != int or n < 0:
        raise ValueError("Invalid input. Please provide a positive integer.")

    if n < 8:
        return False

    count = 0
    for i in range(2, n//4 + 1, 2):
        for j in range(i, n//4 + 1, 2):
            for k in range(j, n//4 + 1, 2):
                for l in range(k, n//4 + 1, 2):
                    if i + j + k + l == n:
                        count += 1

    return count > 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)
        self.assertEqual(is_equal_to_sum_even(8), True)

if __name__ == '__main__':
    unittest.main()