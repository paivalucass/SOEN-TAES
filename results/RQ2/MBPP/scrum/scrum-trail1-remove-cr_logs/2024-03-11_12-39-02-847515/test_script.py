from typing import List

def multiply_num(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Error: Empty input list")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("Error: Non-numeric input")
    
    product = 1
    for num in numbers:
        product *= num
    
    result = product / len(numbers)
    
    return round(result, 1)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()