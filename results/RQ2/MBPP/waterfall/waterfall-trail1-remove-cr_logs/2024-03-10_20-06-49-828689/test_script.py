def rectangle_area(length: int, breadth: int) -> int:
    if length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth should be positive numbers")

    area = length * breadth
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()