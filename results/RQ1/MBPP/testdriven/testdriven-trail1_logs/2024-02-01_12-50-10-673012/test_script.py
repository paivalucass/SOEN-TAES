def rectangle_area(l, b):
    """
    Write a function to find the area of a rectangle.
    :param l: length of the rectangle
    :param b: breadth of the rectangle
    :return: area of the rectangle
    """
    if not isinstance(l, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid input: non-numeric value"
    elif l < 0 or b < 0:
        return "Invalid input: negative number"
    else:
        return l * b

# Test cases
assert rectangle_area(10, 20) == 200
assert rectangle_area('abc', 20) == "Invalid input: non-numeric value"
assert rectangle_area(-10, 20) == "Invalid input: negative number"
assert rectangle_area(0, 20) == 0
assert rectangle_area(1000000, 1000000) == 1000000000000
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()