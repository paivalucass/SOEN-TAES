def solve(N):
    if not isinstance(N, int) or N < 0 or N > 10000:
        return "Invalid input"

    binary_sum = 0
    while N > 0:
        binary_sum += N % 2
        N //= 2

    binary_string = ""
    while binary_sum > 0:
        binary_string = str(binary_sum % 2) + binary_string
        binary_sum //= 2

    return binary_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1000), "1")
        self.assertEqual(function_under_test(150), "110")
        self.assertEqual(function_under_test(147), "1100")

if __name__ == '__main__':
    unittest.main()