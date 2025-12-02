def is_Power_Of_Two(x):
    if x <= 0:
        return False
    else:
        return (x & (x - 1)) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Power_Of_Two(13, 9), True)

if __name__ == '__main__':
    unittest.main()