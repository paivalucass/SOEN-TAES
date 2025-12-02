def odd_num_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**4
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()