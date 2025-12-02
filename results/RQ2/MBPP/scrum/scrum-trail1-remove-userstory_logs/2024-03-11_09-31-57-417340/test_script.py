def find_sum(arr):
    element_count = {}
    non_repeated_elements = set()
    for element in arr:
        if element_count.get(element):
            element_count[element] += 1
        else:
            element_count[element] = 1
            non_repeated_elements.add(element)
    
    sum_of_non_repeated_elements = sum(non_repeated_elements)
    return sum_of_non_repeated_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()