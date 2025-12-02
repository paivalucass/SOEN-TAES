def sum_Of_Subarray_Prod(arr):
    if not isinstance(arr, list):
        return "Invalid input"
    
    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    def sum_of_products(arr):
        total_sum = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                sublist = arr[i:j+1]
                product = product_of_sublist(sublist)
                total_sum += product
        return total_sum

    return sum_of_products(arr)
import unittest

class Test(unittest.TestCase):
    def test_sum_Of_Subarray_Prod(self):
        self.assertEqual(sum_Of_Subarray_Prod([1,2,3]), 20)

if __name__ == '__main__':
    unittest.main()