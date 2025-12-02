def median_trapezium(base1, base2, height):
    if not all(isinstance(i, (int, float)) for i in [base1, base2, height]):
        return "Error: Invalid input data type"

    if base1 < 0 or base2 < 0:
        return "Error: Invalid base value"

    if height < 0:
        return "Error: Invalid height value"

    if base1 == base2:
        return "Error: Bases cannot be equal"

    median = (base1 + base2) / 2
    return median
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()