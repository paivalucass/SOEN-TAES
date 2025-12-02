import math

def multiply_num(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result / len(numbers)

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(multiply_num((8, 2, 3, -1, 7)), -67.2, delta=0.001)

if __name__ == '__main__':
    unittest.main()