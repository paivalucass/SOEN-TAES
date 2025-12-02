def max_product(arr):
    if not arr:
        return 0
    
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]
    
    for num in arr[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        temp_max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        max_prod = temp_max_prod
        
        result = max(result, max_prod)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()