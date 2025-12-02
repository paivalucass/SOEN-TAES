def solve(N):
    sum_of_digits = sum(int(digit) for digit in bin(N)[2:])
    return bin(sum_of_digits)[2:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(1000), '1')
        self.assertEqual(solve(150), '110')
        self.assertEqual(solve(147), '1100')

if __name__ == '__main__':
    unittest.main()