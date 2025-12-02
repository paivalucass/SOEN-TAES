def largest_divisor(n: int) -> int:
	if n == 1:
		return -1
	for i in range(n-1, 0, -1):
		if n % i == 0:
			return i
	return -1
import unittest

class Test(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(12), 6)
        self.assertEqual(largest_divisor(2), 1)
        self.assertEqual(largest_divisor(1), -1)

if __name__ == '__main__':
    unittest.main()