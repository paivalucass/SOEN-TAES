def sum_Of_Subarray_Prod(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if len(arr) == 0:
        return 0

    result = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sublist = arr[i:j+1]
            result += calculate_product(sublist)

    return result


def calculate_product(sublist):
    prod = 1
    for num in sublist:
        prod *= num
    return prod
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Of_Subarray_Prod([1,2,3]), 20)

if __name__ == '__main__':
    unittest.main()