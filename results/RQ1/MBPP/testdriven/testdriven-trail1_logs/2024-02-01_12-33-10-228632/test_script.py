def set_left_most_unset_bit(num):
    mask = 1
    while (num & mask) != 0:
        mask = mask << 1
    return num + mask
import unittest

class Test(unittest.TestCase):
    def test_set_left_most_unset_bit(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()