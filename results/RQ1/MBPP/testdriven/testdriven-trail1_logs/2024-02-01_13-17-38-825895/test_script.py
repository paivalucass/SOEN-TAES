def sum_Of_Subarray_Prod(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            product = 1
            for k in range(i, j+1):
                product *= arr[k]
            result += product
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Of_Subarray_Prod([1,2,3]), 20)

if __name__ == '__main__':
    unittest.main()