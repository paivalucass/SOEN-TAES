def highest_Power_of_2(n):
    if n <= 0:
        return 0
    else:
        return 2 ** (n.bit_length() - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()