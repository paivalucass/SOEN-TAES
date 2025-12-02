def truncate_number(number: float) -> float:
    if not isinstance(number, float) or number <= 0:
        return "Error: Input must be a positive floating point number"
    return abs(number % 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(truncate_number(3.5), 0.5)

if __name__ == '__main__':
    unittest.main()