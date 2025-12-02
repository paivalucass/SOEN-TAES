def perimeter_pentagon(a):
    if a <= 0:
        raise ValueError("Length of side 'a' must be a positive number")

    NUM_SIDES = 5
    perimeter = NUM_SIDES * a
    return perimeter
import unittest

class Test(unittest.TestCase):
    def test_perimeter_pentagon(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()