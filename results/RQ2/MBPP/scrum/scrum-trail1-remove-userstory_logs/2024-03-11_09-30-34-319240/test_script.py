def is_Power_Of_Two(x):
    return (x & (x - 1)) == 0
import unittest

class Test(unittest.TestCase):
    def test_is_Power_Of_Two(self):
        self.assertEqual(is_Power_Of_Two(13), False)

if __name__ == '__main__':
    unittest.main()