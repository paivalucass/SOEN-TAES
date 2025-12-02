def perfect_squares(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Input parameters must be valid integers")
    
    if a < 0 or b < 0:
        raise ValueError("Input parameters must be non-negative numbers")
    
    result = []
    for num in range(a, b+1):
        if (num ** 0.5).is_integer():
            result.append(num)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()