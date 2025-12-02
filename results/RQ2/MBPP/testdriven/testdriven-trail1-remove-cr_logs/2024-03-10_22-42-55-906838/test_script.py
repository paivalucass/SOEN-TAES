def rectangle_area(length, breadth):
    if not isinstance(length, int) or not isinstance(breadth, int) or length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth must be positive integers")
    
    area = length * breadth
    return area

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()