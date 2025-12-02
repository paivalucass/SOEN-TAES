def truncate_number(number: float) -> float:
    decimal_part = abs(number) % 1
    return round(decimal_part, 4) if isinstance(number, (int, float)) else "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(truncate_number(3.5), 0.5)

if __name__ == '__main__':
    unittest.main()