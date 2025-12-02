import math

def multiply_num(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Input must be a list of numbers")

    product = 1
    for num in numbers:
        product *= num

    result = product / len(numbers)
    return result
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()