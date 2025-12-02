def sum_Of_Subarray_Prod(arr):
    result = 0
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            result += product
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Of_Subarray_Prod([1,2,3]), 20)

if __name__ == '__main__':
    unittest.main()