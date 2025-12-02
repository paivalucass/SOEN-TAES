def set_left_most_unset_bit(n):
    x = n
    x |= (x+1)
    x |= (x+1)
    return x
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()