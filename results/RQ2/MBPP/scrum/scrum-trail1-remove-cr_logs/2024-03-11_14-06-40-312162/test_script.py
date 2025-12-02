def left_rotate(n, d):
    # Ensure that the input data is valid
    if not isinstance(n, int) or not isinstance(d, int) or d < 0:
        return "Invalid input data"

    # Return the left rotated number
    return (n << d) | (n >> (32 - d))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_rotate(16, 2), 64)

if __name__ == '__main__':
    unittest.main()