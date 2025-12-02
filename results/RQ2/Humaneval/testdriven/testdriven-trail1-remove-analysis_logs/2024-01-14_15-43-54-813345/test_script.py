def truncate_number(number: float) -> float:
    if number < 0:
        raise ValueError("Input number should be positive")
    
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(truncate_number(3.5), 0.5)

if __name__ == '__main__':
    unittest.main()