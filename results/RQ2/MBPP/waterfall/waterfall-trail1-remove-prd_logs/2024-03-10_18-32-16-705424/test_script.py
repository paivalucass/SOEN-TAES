def intersection_array(array_nums1, array_nums2):
    hash_map = {}
    result = []
    for num in array_nums1:
        hash_map[num] = 1
    for num in array_nums2:
        if num in hash_map and num not in result:
            result.append(num)
    return result

assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]

# Add more test cases to ensure the functionality and correctness of the intersection_array function
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9] # Original assertion
assert intersection_array([1, 2, 3, 4, 5],[6, 7, 8, 9, 10])==[] # Test case for arrays with no intersection
assert intersection_array([1, 2, 3],[1, 2, 3])==[1, 2, 3] # Test case for arrays with all elements in common
assert intersection_array([],[1, 2, 3])==[] # Test case for empty array 1
assert intersection_array([1, 2, 3],[])==[] # Test case for empty array 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]), [1, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()