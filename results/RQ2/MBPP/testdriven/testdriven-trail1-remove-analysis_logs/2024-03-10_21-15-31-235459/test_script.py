def sequential_search(arr, element):
    if arr is None or len(arr) == 0:
        raise ValueError("Input array is empty or null")  # raise an exception for empty or null input array

    for index, el in enumerate(arr):
        if el == element:
            return (True, index)  # return a tuple with True and the index position if the element is found

    return (False, -1)  # return a tuple with False and -1 if the element is not found

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19], 31), (True, 3))

if __name__ == '__main__':
    unittest.main()