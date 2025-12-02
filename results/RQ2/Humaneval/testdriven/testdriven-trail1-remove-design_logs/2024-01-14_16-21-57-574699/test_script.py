def solve(N):
    binary_representation = bin(N)[2:]
    total_sum = str(bin(N)[2:].count('1'))
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1000), "1")
        self.assertEqual(function_under_test(150), "110")
        self.assertEqual(function_under_test(147), "1100")

if __name__ == '__main__':
    unittest.main()