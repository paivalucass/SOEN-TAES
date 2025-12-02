def solve(N):
    binary_sum = 0
    while N > 0:
        binary_sum += N % 2
        N = N // 2
    return bin(binary_sum)[2:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(150), "110")
        self.assertEqual(solve(147), "1100")

if __name__ == '__main__':
    unittest.main()