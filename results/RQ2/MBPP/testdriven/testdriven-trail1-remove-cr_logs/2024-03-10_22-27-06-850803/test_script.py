def is_Power_Of_Two (x):
    return x > 0 and (x & (x - 1)) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Power_Of_Two(16), True)

if __name__ == '__main__':
    unittest.main()