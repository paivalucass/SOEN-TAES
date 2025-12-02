def perfect_squares(a, b):
    squares = []
    if a < 0:
        a = 0
    for i in range(int(a ** 0.5), int(b ** 0.5) + 1):
        squares.append(i ** 2)
    return [x for x in squares if a <= x <= b]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()