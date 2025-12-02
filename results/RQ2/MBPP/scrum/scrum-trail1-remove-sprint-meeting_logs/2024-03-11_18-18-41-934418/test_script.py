def multiply_num(numbers):
    try:
        product = 1
        for num in numbers:
            product *= num
        average_product = product / len(numbers)
        return average_product
    except ZeroDivisionError:
        raise ZeroDivisionError("Input list cannot be empty")
    except TypeError:
        raise TypeError("Input list contains non-numeric values")
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()