def dif_Square(n):
    '''Write a python function to check whether the given number can be represented as the difference of two squares or not'''
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        return False

    for i in range(int(n**0.5) + 1):
        if n - i*i == int(n - i*i):
            return True

    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()