def convert(numbers):
    import cmath
    if isinstance(numbers, list):
        return [cmath.polar(num) for num in numbers]
    else:
        return cmath.polar(numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()