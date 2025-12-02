def find_sum(arr):
    non_repeated_elements = []
    for element in set(arr):
        if arr.count(element) == 1:
            non_repeated_elements.append(element)
    return sum(non_repeated_elements)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()