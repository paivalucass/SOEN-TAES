def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
    a -- length of a side of the triangle (positive non-zero value with specified units of measurement)
    h -- height of the triangle (positive non-zero value with specified units of measurement)

    Returns:
    area of the triangle (numeric value with specified units of measurement)

    Raises:
    ValueError: if either a or h is not a positive non-zero value
    TypeError: if either a or h is not a numeric value
    OverflowError: if the result of the calculation exceeds the maximum representable value
    """
    def validate_input_values(a, h) -> None:
        """
        Validates that a and h are numeric, non-zero, and positive.

        Raises:
        ValueError: if either a or h is not a positive non-zero value
        TypeError: if either a or h is not a numeric value
        """
        if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
            raise TypeError("a and h must be numeric values")
        if a <= 0 or h <= 0:
            raise ValueError("a and h must be positive non-zero values")

    try:
        validate_input_values(a, h)
        area = 0.5 * a * h
    except (ValueError, TypeError):
        raise
    except OverflowError:
        raise OverflowError("The result of the calculation exceeds the maximum representable value")
    else:
        return area
import unittest

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 3), 7.5)
        self.assertEqual(triangle_area(7, 4), 14.0)
        self.assertEqual(triangle_area(10, 2), 10.0)

if __name__ == '__main__':
    unittest.main()