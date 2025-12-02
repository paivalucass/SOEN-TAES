def triangle_area(base, height):
    """
    Calculate the area of a triangle given the base and height.
    
    Args:
    base (int or float): The length of the base of the triangle.
    height (int or float): The height of the triangle.
    
    Returns:
    float: The calculated area of the triangle.
    """
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        return "Error: Invalid input"
    if base <= 0 or height <= 0:
        return "Error: Invalid input"
    return 0.5 * base * height
import unittest

class Test(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()