def count_Set_Bits(n):
    # Write a python function to count the number of set bits (binary digits with value 1) in a given number.
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

assert count_Set_Bits(2) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Set_Bits(2), 1)

if __name__ == '__main__':
    unittest.main()