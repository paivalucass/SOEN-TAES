def sum_series(n):
    if not isinstance(n, int):
        return "Invalid Input"
    if n > 0:
        result = 0
        for i in range(n // 2 + 1):
            result += n - 2*i
        return result
    elif n < 0:
        result = 0
        for i in range(n // 2 - 1, -1, -1):
            result += n - 2*i
        return result
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()