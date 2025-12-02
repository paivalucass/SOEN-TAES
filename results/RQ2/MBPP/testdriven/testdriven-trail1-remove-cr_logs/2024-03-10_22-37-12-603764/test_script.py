def square_Sum(n):
    # Implementation details
    # Use the separate utility function to calculate the square of a number
    # Calculate the sum of squares of the first n even natural numbers
    return sum([i * i * 4 for i in range(1, n + 1)])  # Example: for n=2, it will return 2*2 + 4*4 = 20

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()