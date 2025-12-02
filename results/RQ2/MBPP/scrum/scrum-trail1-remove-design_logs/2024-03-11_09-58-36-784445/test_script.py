def dif_Square(n):
    for i in range(1, n):
        if i*i - (i-1)*(i-1) == n:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()