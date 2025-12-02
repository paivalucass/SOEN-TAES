def perimeter_pentagon(side_length):
    if side_length <= 0:
        raise ValueError("Invalid side length. Please enter a positive value for the side length of the pentagon.")
    return 5 * side_length
import unittest

class Test(unittest.TestCase):
    def test_perimeter_pentagon(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()