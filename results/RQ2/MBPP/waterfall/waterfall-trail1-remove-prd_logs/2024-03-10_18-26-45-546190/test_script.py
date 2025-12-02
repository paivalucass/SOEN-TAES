def dif_Square(n):
    if n <= 0:
        return False
    for i in range(1, int(n**0.5) + 1):
        square = i * i
        if square > n:
            break
        if (n - square) ** 0.5 == int((n - square) ** 0.5):
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()