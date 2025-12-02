def min_of_three(a, b, c):
    # Input validation
    if not all(isinstance(n, (int, float)) for n in [a, b, c]):
        raise ValueError("All input parameters must be integers or floats")

    # Using built-in min() function to find the minimum value
    return min(a, b, c)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_of_three(10, 20, 0), 0)

if __name__ == '__main__':
    unittest.main()