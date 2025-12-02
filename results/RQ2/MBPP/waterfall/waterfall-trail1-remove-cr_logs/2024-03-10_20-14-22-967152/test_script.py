def reverse_Array_Upto_K(input, k):
    if not input:
        return "Input array is empty"
    if k < 0 or k > len(input):
        return "Invalid value for k"
    if k == 0 or k == len(input):
        return input
    else:
        return list(reversed(input[:k])) + input[k:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4), [4, 3, 2, 1, 5, 6])

if __name__ == '__main__':
    unittest.main()