def solve(N):
    total_sum = sum([int(i) for i in str(N)])
    return bin(total_sum)[2:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1000), "1")
        self.assertEqual(function_under_test(150), "110")
        self.assertEqual(function_under_test(147), "1100")

if __name__ == '__main__':
    unittest.main()