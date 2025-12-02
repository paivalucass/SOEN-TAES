def triangle_area(a, b, c):
    def validate_input(a, b, c):
        if all(isinstance(side, (int, float)) for side in [a, b, c]):
            if all(side > 0 for side in [a, b, c]):
                return True
        return False
    
    def calculate_area(a, b, c):
        semi_perimeter = (a + b + c) / 2
        area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
        return round(area, 2) if area > 0 else -1
    
    if validate_input(a, b, c):
        if a + b > c and b + c > a and a + c > b:
            return calculate_area(a, b, c)
    
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)
        self.assertEqual(triangle_area(1, 2, 10), -1)

if __name__ == '__main__':
    unittest.main()