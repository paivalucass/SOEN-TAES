def dif_Square(n):
    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        return False
    if n == 0:
        return True
    for i in range(1, int(n**0.5) + 1):
        m = n - i*i
        if (int(m**0.5))**2 == m:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()