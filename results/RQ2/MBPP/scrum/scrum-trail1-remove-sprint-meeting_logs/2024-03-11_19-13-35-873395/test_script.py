def sum_odd(l, r):
    if l > r:
        return "Invalid Input"
    sum = 0
    for num in range(l, r+1):
        if num % 2 != 0:
            sum += num
    return sum
import unittest

class Test(unittest.TestCase):
    def test_sum_odd(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()