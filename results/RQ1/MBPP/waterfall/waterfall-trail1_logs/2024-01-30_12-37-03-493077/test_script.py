def is_Sum_Of_Powers_Of_Two(n):
    if not isinstance(n, int) or n <= 0:
        return False
    return (n & (n - 1)) != 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()