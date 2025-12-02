def calculate_third_side_right_angle(side1: float, side2: float) -> float:
    if side1 <= 0 or side2 <= 0:
        raise ValueError("Input values must be non-negative")
    side3 = (side1 ** 2 + side2 ** 2) ** 0.5
    return round(side3, 11)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()