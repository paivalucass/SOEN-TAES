def sum_even_and_even_index(arr):
    try:
        if not all(isinstance(x, int) for x in arr):
            raise TypeError("Input list must only contain integers")
        
        if len(arr) == 0:
            return 0
        
        even_sum = sum(arr[i] for i in range(len(arr)) if i % 2 == 0 and arr[i] % 2 == 0)
        
        return even_sum
    except TypeError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_even_and_even_index([5, 6, 12, 1, 18, 8]), 30)

if __name__ == '__main__':
    unittest.main()