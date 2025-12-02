def perfect_squares(a, b):
    squares = [i*i for i in range(int(a**0.5), int(b**0.5)+1)]
    return squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()