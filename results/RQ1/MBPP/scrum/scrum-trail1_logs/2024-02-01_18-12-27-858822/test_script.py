def dif_Square(n):
    if n < 0:
        return False
    i = 0
    while i * i <= n:
        b = n + (i * i)
        a = int(b ** 0.5)
        if a * a == b:
            return True
        i += 1
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()