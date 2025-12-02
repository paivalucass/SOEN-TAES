def truncate_number(number: float) -> float:
    if type(number) != float or number <= 0:
        return "Error: Input should be a positive floating point number"
    decimal_part = number - int(number)
    return decimal_part
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(truncate_number(3.5), 0.5)

if __name__ == '__main__':
    unittest.main()