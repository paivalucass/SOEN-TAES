def right_insertion(array, element):
    index = 0
    while index < len(array) and array[index] < element:
        index += 1
    return index

# Test the function with different inputs
print(right_insertion([1, 2, 4, 5], 6))  # Output: 4
print(right_insertion([5, 4, 2, 1], 3))  # Output: 2
print(right_insertion(['a', 'b', 'd', 'e'], 'c'))  # Output: 2
print(right_insertion([], 1))  # Output: 0
print(right_insertion([3], 2))  # Output: 0
import unittest

class Test(unittest.TestCase):
    def test_right_insertion(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()