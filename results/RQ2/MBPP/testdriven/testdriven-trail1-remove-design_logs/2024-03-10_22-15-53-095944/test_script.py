def reverse_Array_Upto_K(arr, k):
    '''This function takes an array and reverses its elements up to a given position.'''
    if not isinstance(arr, list):
        return "Invalid input"

    if k < 1 or k > len(arr):
        return arr

    return arr[:k][::-1] + arr[k:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4), [4, 3, 2, 1, 5, 6])

if __name__ == '__main__':
    unittest.main()