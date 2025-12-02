def square_perimeter(a):
    if type(a) != int or a <= 0:
        raise ValueError("Input must be a positive integer")

    return a * 4
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()