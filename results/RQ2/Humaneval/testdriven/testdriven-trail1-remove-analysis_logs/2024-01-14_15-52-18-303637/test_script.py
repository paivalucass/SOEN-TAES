def solve(N):
    if N < 0 or N > 10000:
        return "Invalid input: N should be between 0 and 10000"

    binary_sum = bin(N).count('1')

    return format(binary_sum, 'b')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1000), "1")
        self.assertEqual(function_under_test(150), "110")
        self.assertEqual(function_under_test(147), "1100")

if __name__ == '__main__':
    unittest.main()