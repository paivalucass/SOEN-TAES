def odd_num_sum(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    result = sum((2*i-1) ** 4 for i in range(1, n+1))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()