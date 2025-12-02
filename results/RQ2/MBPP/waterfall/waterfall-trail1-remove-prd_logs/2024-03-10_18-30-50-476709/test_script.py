def perimeter_pentagon(side_length: float) -> float:
    if side_length <= 0 or not isinstance(side_length, (int, float)):
        raise ValueError("Invalid input: side length must be a positive number")

    perimeter = side_length * 5
    return perimeter
import unittest

class Test(unittest.TestCase):
    def test_perimeter_pentagon(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()