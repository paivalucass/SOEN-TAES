def rounded_avg(n, m):
    """
    You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """

    # input validation
    if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
        return -1

    if n > m:
        return -1
    average = (n + m) / 2
    rounded = round(average)
    return bin(rounded)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")

if __name__ == '__main__':
    unittest.main()