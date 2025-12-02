def perimeter_pentagon(a):
    if not isinstance(a, (int, float)) or a <= 0:
        raise ValueError("Invalid input for side length 'a'. Side length 'a' must be a positive number.")
    return 5 * a

# Test the function
assert perimeter_pentagon(5) == 25
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()