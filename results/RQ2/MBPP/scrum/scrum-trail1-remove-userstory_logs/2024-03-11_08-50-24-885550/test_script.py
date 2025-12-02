def square_perimeter(a: float) -> float:
    try:
        perimeter = 4 * float(a)
        return perimeter
    except ValueError:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()