def is_perfect_square(num):
    sqrt_num = int(num ** 0.5)
    return sqrt_num * sqrt_num == num

def find_difference_of_squares(n):
    for i in range(1, int(n**0.5) + 1):
        if is_perfect_square(n + i*i):
            return True
    return False

def dif_Square(n):
    if is_perfect_square(n):
        return True
    elif find_difference_of_squares(n):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()