def dif_Square(n):
    def is_difference_of_squares(num):
        if num < 0:
            return False
        elif num == 0:
            return True
        else:
            for i in range(1, int(num**0.5) + 1):
                if (num - i**2)**0.5 == int((num - i**2)**0.5):
                    return True
            return False
    
    return is_difference_of_squares(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()