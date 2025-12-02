from typing import Union

def right_angle_triangle(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[bool, str]:
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid Input"
    sides = [a, b, c]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_right_angle_triangle(self):
        self.assertEqual(right_angle_triangle(3, 4, 5), True)
        self.assertEqual(right_angle_triangle(1, 2, 3), False)

if __name__ == '__main__':
    unittest.main()