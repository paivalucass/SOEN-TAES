def sum_even_and_even_index(arr):
    if not isinstance(arr, list):
        return "Input is not a list"
    
    sum_even_index = 0
    
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            sum_even_index += arr[i]
    
    return sum_even_index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_even_and_even_index([5, 6, 12, 1, 18, 8]), 30)

if __name__ == '__main__':
    unittest.main()