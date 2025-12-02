def dif_Square(n):
    if n < 0 or not isinstance(n, int):
        return "Invalid Input"
    elif n == 0:
        return True
    else:
        for i in range(int(n**0.5) + 1):
            if n - i*i == 0 or n - i*i == i*i:
                return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()