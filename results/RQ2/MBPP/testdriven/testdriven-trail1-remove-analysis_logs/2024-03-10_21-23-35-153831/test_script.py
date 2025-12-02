def split_Arr(arr, split_index):
    '''
    Write a python function to split a list at the nth element and add the first part to the end.
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    '''
    if not arr:
        return arr
    if split_index < 0 or split_index >= len(arr):
        return arr
    return arr[split_index:] + arr[:split_index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()