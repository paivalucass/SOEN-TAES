def next_Perfect_Square(N):
    import math
    
    if type(N) != int or N <= 0:
        return "Error"
    
    return (math.isqrt(N) + 1) ** 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()