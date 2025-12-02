def otherside_rightangle(width, height):
    if width <= 0 or height <= 0:
        return "Invalid Input"

    hypotenuse = (width ** 2 + height ** 2) ** 0.5
    return hypotenuse
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()