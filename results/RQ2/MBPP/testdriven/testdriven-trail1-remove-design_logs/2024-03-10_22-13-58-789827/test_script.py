def remove_kth_element(list1, k):
    '''
    Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
    assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    '''

    # Check if the list is empty
    if not list1:
        return []

    # Check if k value is out of bounds
    if k <= 0 or k > len(list1):
        return "Error: k value out of bounds"

    # Check if input list contains elements of different data types
    if len(set(map(type, list1))) > 1:
        return "Error: input list contains elements of different data types"

    # Remove the k'th element from the list
    else:
        del list1[k-1]
        return list1
import unittest

class Test(unittest.TestCase):
    def test_remove_kth_element(self):
        self.assertEqual(remove_kth_element([1,1,2,3,4,4,5,1], 3), [1, 1, 3, 4, 4, 5, 1])

if __name__ == '__main__':
    unittest.main()