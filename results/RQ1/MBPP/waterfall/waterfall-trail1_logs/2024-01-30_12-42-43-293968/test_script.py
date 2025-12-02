def count_Set_Bits(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid Input"

    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Set_Bits(2), 1)

if __name__ == '__main__':
    unittest.main()