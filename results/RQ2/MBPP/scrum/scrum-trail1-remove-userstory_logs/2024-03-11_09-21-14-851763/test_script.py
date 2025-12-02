def triangle_area(r):
    try:
        if not isinstance(r, (int, float)):
            return "Invalid Input"
        if r < 0:
            return None
        else:
            area = (r ** 2) / 2
            return area
    except ValueError:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5), 12.5)
        self.assertEqual(triangle_area(0), 0)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()