def solve(N):
    if not isinstance(N, int) or N < 0 or N > 10000:
        return "Invalid input"
    
    def calculate_digit_sum(number):
        return bin(sum(int(digit) for digit in str(number)))[2:]
    
    return calculate_digit_sum(N)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1000), "1")
        self.assertEqual(function_under_test(150), "110")
        self.assertEqual(function_under_test(147), "1100")

if __name__ == '__main__':
    unittest.main()