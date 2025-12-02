def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [ smallest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """

    # Input validation to check if the input is a list of integers
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return []

    # Find the even values in the array
    even_values = [i for i in arr if i % 2 == 0]

    # If there are no even values, return empty list
    if len(even_values) == 0:
        return []

    # Find the smallest even value
    smallest_even_value = min(even_values)

    # Find the index of the smallest even value
    smallest_even_index = arr.index(smallest_even_value)

    # Return the smallest even value and its index
    return [smallest_even_value, smallest_even_index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])
        self.assertEqual(pluck([1,2,3]), [2, 1])
        self.assertEqual(pluck([]), [])
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()