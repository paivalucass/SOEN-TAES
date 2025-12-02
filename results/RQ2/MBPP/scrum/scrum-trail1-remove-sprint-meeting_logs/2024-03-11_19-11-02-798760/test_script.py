def find_sum(arr):
    unique_elements = set(arr)  
    sum_of_unique_elements = sum(unique_elements)  
    return sum_of_unique_elements  

assert find_sum([1,2,3,1,1,4,5,6]) == 21  
assert find_sum([]) == 0  
assert find_sum([1,1,1,1,1]) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()