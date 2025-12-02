def sum_even_and_even_index(arr):
    if not isinstance(arr, list):
        return "Error: Input is not a list"
    
    for element in arr:
        if not isinstance(element, int):
            return "Error: Elements in the list are not integers"
    
    sum_even = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            sum_even += arr[i]
    
    return sum_even
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_even_and_even_index([5, 6, 12, 1, 18, 8]), 30)

if __name__ == '__main__':
    unittest.main()