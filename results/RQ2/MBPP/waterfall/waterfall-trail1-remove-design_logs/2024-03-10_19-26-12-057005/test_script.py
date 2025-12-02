def find_sum(arr):
    unique_elements = Counter(arr)
    sum_of_unique_elements = sum([k for k, v in unique_elements.items() if v == 1])
    return sum_of_unique_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()