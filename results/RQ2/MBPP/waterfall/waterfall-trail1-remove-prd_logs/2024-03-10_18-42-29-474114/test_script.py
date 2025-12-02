def split_Arr(arr, index):
    if not isinstance(arr, list):
        raise TypeError("Input arr must be a list")
    if not isinstance(index, int) or index < 0 or index >= len(arr):
        raise ValueError("Input index must be a valid index within the range of the list")

    return arr[index:] + arr[:index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()