def find_lucas(n): 
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input parameter n must be a non-negative integer")

    if n == 0:
        return 2
    elif n == 1:
        return 1

    a, b = 2, 1
    for _ in range(2, n+1):
        a, b = b, a + b

    return b

assert find_lucas(9) == 76
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()