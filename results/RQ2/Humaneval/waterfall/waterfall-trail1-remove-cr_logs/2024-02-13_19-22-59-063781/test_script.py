def solve(N):
    binary_sum = bin(sum(int(digit) for digit in str(N)))[2:]
    return binary_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(150), "110")
        self.assertEqual(solve(147), "1100")

if __name__ == '__main__':
    unittest.main()