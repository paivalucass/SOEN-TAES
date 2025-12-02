def multiply_num(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    result = 1
    has_zero = False
    for num in numbers:
        if num == 0:
            has_zero = True
        result *= num
    
    if has_zero:
        return 0
    
    return result / len(numbers)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()