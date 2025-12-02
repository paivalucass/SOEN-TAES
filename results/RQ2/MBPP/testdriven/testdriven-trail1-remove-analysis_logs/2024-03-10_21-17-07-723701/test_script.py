def find_lucas(n):
    '''Write a function to find the n'th lucas number.
    assert find_lucas(9) == 76'''
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1  # Initialize the first two terms of Lucas series
        for _ in range(2, n + 1):  # Calculate the n'th term of Lucas series
            a, b = b, a + b
        return b  # Return the n'th term of Lucas series
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()