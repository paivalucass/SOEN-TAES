def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return True
    power = 1
    while power <= n:
        power *= 2
    power //= 2
    return is_Sum_Of_Powers_Of_Two(n - power)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()