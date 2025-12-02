def rectangle_area(length, breadth):
    try:
        if length <= 0 or breadth <= 0:
            raise ValueError("Length and breadth must be positive numbers")
        area = length * breadth
        return area
    except TypeError:
        raise TypeError("Length and breadth must be numeric values")

# Test cases
assert rectangle_area(10, 20) == 200
try:
    rectangle_area(-10, 20)
except ValueError as ve:
    assert str(ve) == "Length and breadth must be positive numbers"
try:
    rectangle_area(10, "20")
except TypeError as te:
    assert str(te) == "Length and breadth must be numeric values"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()