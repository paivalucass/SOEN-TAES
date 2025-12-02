def sum_to_n(n: int) -> int:
    if n <= 0:
        raise ValueError("n should be a positive integer")

    sum_result = (n * (n + 1)) // 2
    return sum_result
import unittest

class Test(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()