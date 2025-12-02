def median_trapezium(base1, base2, height):
    if base1 <= 0 or base2 <= 0 or height <= 0:
        return "Invalid input"
    
    if not isinstance(base1, (int, float)) or not isinstance(base2, (int, float)) or not isinstance(height, (int, float)):
        return "Invalid input"

    if base1 > base2:
        return "Invalid input"

    median = (base1 + base2) / 2
    return round(median, 2) if isinstance(median, float) else int(median)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()