def dif_Square(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid Input"
    else:
        for i in range(1, int(n**0.5) + 1):
            if n - i*i == int((n - i*i)**0.5)**2:
                return True
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()