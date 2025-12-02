def pair_xor_Sum(arr, n):
    '''Write a python function to find the sum of xor of all pairs of numbers in the given list.'''
    if not arr:
        return 0  # Return 0 if the input list is empty

    if n < 2:
        return 0  # Return 0 if the number of elements is less than 2

    xor_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += arr[i] ^ arr[j]  # Calculate the xor sum of all pairs of numbers

    return xor_sum

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_xor_Sum([5,9,7,6], 4), 47)

if __name__ == '__main__':
    unittest.main()