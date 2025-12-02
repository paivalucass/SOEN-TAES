def perfect_squares(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input numbers must be valid integers")
    
    if a > b:
        a, b = b, a

    result = [x*x for x in range(int(a**0.5), int(b**0.5) + 1)]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1, 30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()