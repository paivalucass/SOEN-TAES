def rectangle_area(l, b):
    '''Write a function to find the area of a rectangle.'''
    if not isinstance(l, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid input"

    if l <= 0 or b <= 0:
        return "Invalid input"
    else:
        return l * b
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()