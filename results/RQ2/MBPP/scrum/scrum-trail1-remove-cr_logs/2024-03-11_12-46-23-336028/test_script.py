def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    else:
        while n % 2 == 0:
            n = n / 2
        return n == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()