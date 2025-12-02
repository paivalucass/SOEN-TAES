def find_sum(arr):
    unique_elements = set(arr)
    sum = 0
    for element in unique_elements:
        sum += element
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()