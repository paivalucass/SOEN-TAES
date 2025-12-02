import math

def multiply_num(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list of numbers')
    if len(numbers) == 0:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result / len(numbers)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()