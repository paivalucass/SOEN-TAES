def rectangle_area(length, breadth):
    if not isinstance(length, int) or not isinstance(breadth, int) or length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth should be positive integers")

    if length == 0 or breadth == 0:
        return 0
    elif length == 1 or breadth == 1:
        return max(length, breadth)
    else:
        return length * breadth
import unittest

class Test(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()