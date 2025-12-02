def is_sum_of_powers_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n - 1)) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()