def find_sum(arr):
    unique_elements_count = {}
    for element in arr:
        if element in unique_elements_count:
            unique_elements_count[element] += 1
        else:
            unique_elements_count[element] = 1
    return sum([key for key, value in unique_elements_count.items() if value == 1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()