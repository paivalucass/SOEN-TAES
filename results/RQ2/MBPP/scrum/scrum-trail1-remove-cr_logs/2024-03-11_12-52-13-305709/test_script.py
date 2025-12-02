def count_Set_Bits(n):
    if not isinstance(n, int):
        return "Error: Input should be an integer"
    elif n < 0:
        return "Error: Input should be a non-negative integer"
    else:
        binary_representation = bin(n)
        count = binary_representation.count('1')
        return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Set_Bits(2), 1)

if __name__ == '__main__':
    unittest.main()