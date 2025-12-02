def max_product(arr):
    if len(arr) < 2 or not all(isinstance(x, (int, float)) for x in arr):
        return None
    
    max_pair = (arr[0], arr[1])
    max_val = arr[0] * arr[1]
    
    for i in range(len(arr) - 1):
        product = arr[i] * arr[i+1]
        if product > max_val:
            max_val = product
            max_pair = (arr[i], arr[i+1])
    
    return max_pair

# Test cases
assert max_product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)  # should return (7, 8)
assert max_product([5, -10, 2, 8, 10]) == (-10, 2)  # should return (-10, 2)
assert max_product([]) == None  # should return None
assert max_product([1, 'a', 3, 4]) == None  # should return None (non-numeric value present)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7,8))

if __name__ == '__main__':
    unittest.main()