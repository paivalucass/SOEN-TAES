def find_sum(arr):
    if not isinstance(arr, list):
        raise ValueError("Input is not a list")
    
    element_count = {}
    sum_of_non_repeated = 0

    for element in arr:
        if element_count.get(element) is None:
            element_count[element] = 1
        else:
            element_count[element] += 1

    for element, count in element_count.items():
        if count == 1:
            sum_of_non_repeated += element

    return sum_of_non_repeated
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()