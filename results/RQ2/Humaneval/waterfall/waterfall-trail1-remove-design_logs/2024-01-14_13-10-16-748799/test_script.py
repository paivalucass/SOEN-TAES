def common(l1: list, l2: list) -> list:
    return sorted(list(set(l1) & set(l2)))



# Testing the function with different types of input
print(common([1, 2, 3, 4], [3, 4, 5, 6])) # should return [3, 4]
print(common([1, 2, 3, 4], [])) # should return []
print(common([1, 2, 2, 3, 4], [2, 2, 3, 3, 5])) # should return [2, 3]
print(common([1, 2, 3, 4], ['a', 'b', 'c', 3])) # should return [3]

# Testing the function with very large input
import random
large_input1 = random.sample(range(1, 1000000), 10000)
large_input2 = random.sample(range(1, 1000000), 10000)
print(common(large_input1, large_input2)) # testing performance issues with large input
# End of the code.
import unittest

class Test(unittest.TestCase):
    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()