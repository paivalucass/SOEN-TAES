def dif_Square(n):
    for i in range(int(n**0.5)+1):
        if (n - i*i) >= 0 and ((n - i*i)**0.5).is_integer():
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()