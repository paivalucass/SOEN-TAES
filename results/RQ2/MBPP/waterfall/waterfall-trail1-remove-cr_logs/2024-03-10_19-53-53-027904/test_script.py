def search(arr):
    # Write a python function to find the element that appears only once in a sorted array
    for i in range(len(arr)):
        if i == 0 and arr[i] != arr[i+1]:
            return arr[i]
        elif i == len(arr)-1 and arr[i] != arr[i-1]:
            return arr[i]
        elif arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]
    return None

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()