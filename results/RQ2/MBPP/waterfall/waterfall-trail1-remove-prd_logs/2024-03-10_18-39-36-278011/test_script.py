def rectangle_area(length, breadth):
    if length < 0:
        return "Error: Negative input for length"
    elif breadth < 0:
        return "Error: Negative input for breadth"
    elif length == 0 or breadth == 0:
        return 0
    elif length > 1000000000 or breadth > 1000000000:
        return "Error: Maximum input for length and breadth"
    elif not isinstance(length, (int, float)) or not isinstance(breadth, (int, float)):
        return "Error: Non-numeric input for length and breadth"
    elif isinstance(length, float) or isinstance(breadth, float):
        return "Error: Decimal input for length and breadth"
    
    return length * breadth

# Test cases
assert rectangle_area(4, 5) == 20
assert rectangle_area(0, 5) == 0
assert rectangle_area(4, -5) == "Error: Negative input for breadth"
assert rectangle_area(-4, 5) == "Error: Negative input for length"
assert rectangle_area(-4, -5) == "Error: Negative input for length"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()