def by_length(arr):
    result = []
    mapping = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    # Sort the integers between 1 and 9
    sorted_arr = [x for x in arr if 1 <= x <= 9]
    sorted_arr.sort()
    
    # Reverse the resulting array
    sorted_arr.reverse()
    
    # Replace each digit with its corresponding name
    for num in sorted_arr:
        result.append(mapping[num])
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(by_length([]), [])
    
    def test_valid_array(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
    
    def test_strange_numbers(self):
        self.assertEqual(by_length([1, -1, 55]), ["One"])

if __name__ == '__main__':
    unittest.main()