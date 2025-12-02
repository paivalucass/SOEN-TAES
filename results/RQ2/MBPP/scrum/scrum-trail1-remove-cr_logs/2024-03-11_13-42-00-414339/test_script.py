def perfect_squares(a, b):
    perfect_squares_list = []
    for i in range(a, b+1):
        if (int(i ** 0.5)) ** 2 == i:
            perfect_squares_list.append(i)
    return perfect_squares_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()