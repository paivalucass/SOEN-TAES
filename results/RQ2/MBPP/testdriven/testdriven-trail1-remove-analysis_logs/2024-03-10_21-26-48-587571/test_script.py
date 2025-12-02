def reverse_Array_Upto_K(input, k):
    if len(input) == 0 or k <= 0 or k > len(input):
        return input
    else:
        reversed_array = []
        for i in range(k-1,-1,-1):
            reversed_array.append(input[i])
        return reversed_array + input[k:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4), [4, 3, 2, 1, 5, 6])

if __name__ == '__main__':
    unittest.main()