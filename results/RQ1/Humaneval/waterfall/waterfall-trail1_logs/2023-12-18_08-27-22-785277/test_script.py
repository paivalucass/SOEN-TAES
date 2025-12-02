def add_elements(arr, k):
    if len(arr) == 0 or k == 0:
        return "Error: Input array is empty or k is 0"
    elif k > len(arr):
        return "Error: k is greater than array length"
    else:
        sum_of_elements = sum([x for x in arr[:k] if x < 100])
        return sum_of_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_elements([111,21,3,4000,5,6,7,8,9], 4), 24)

if __name__ == '__main__':
    unittest.main()