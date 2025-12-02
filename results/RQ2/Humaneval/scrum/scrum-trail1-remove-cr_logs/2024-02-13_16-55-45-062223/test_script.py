def triangle_area(side_length, triangle_height):
    if side_length < 0 or triangle_height < 0:
        return "Input Error: side_length and triangle_height must be non-negative"

    area = 0.5 * side_length * triangle_height
    return round(area, 10)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()