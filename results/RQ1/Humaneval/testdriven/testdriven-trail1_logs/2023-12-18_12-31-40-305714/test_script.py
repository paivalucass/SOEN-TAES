def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 \
        @N integer
             Constraints: 0 \
        @N integer
             Constraints: 0 \
        @N integer
             Constraints: 0 \u2264 N \u2264 10000.
    Output:
         a string of binary number
    """
    def input_validation(N):
        if N < 0 or N > 10000:
            return False
        return True

    def binary_conversion(N):
        binary_sum = bin(sum(int(digit) for digit in str(N)))[2:]
        return binary_sum

    if not input_validation(N):
        return "Invalid input"
    return binary_conversion(N)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1000), "1")
        self.assertEqual(function_under_test(150), "110")
        self.assertEqual(function_under_test(147), "1100")

if __name__ == '__main__':
    unittest.main()