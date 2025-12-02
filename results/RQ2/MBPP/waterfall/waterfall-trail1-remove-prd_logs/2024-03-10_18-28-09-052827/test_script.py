def multiply_num(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty")
    if 0 in numbers:
        raise ValueError("List contains zero")
    
    product = 1
    for num in numbers:
        product *= num
    
    try:
        return product / len(numbers)
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()