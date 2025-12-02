def reverse_Array_Upto_K(input, k):
    if not input:
        return []

    if k < 0 or k >= len(input):
        raise OutOfRangeError("Position 'k' is out of range")

    return input[:k][::-1] + input[k:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4), [4, 3, 2, 1, 5, 6])

if __name__ == '__main__':
    unittest.main()