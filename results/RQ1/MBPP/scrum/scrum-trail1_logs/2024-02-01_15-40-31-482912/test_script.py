def median_trapezium(base1, base2, height):
    if not all(isinstance(x, (int, float)) for x in [base1, base2, height]) or base1 <= 0 or base2 <= 0 or height <= 0:
        return "Error"

    median_length = (base1 + base2) / 2
    return median_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()