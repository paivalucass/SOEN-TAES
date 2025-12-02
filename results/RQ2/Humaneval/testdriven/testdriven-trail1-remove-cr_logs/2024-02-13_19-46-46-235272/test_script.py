def triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return -1
    
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return round(area, 2)

import unittest

class Test(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)
        self.assertEqual(triangle_area(1, 2, 10), -1)

if __name__ == '__main__':
    unittest.main()