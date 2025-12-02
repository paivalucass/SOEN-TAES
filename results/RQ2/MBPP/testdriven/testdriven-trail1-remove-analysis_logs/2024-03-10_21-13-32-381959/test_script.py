def next_Perfect_Square(N):
    import math
    
    if not isinstance(N, int) or N < 0:
        return "Invalid input: Please provide a non-negative integer"
    
    square_root = math.sqrt(N)
    next_square = math.ceil(square_root)
    
    return next_square ** 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()