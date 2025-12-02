def count_list(input_list):
    """
    Write a python function to count the number of lists in a given input list.
    :param input_list: list of elements
    :return: count of lists in the input list
    """
    list_count = 0  # Initializing the count of lists
    if not isinstance(input_list, list) or len(input_list) == 0:  # Checking if the input is a non-empty list
        return "Error: Input is not a non-empty list of lists"

    for item in input_list:  # Iterating through the items in the input list
        if isinstance(item, list):  # Checking if the item is a list
            list_count += 1  # Incrementing the count of lists

    return list_count  # Returning the count of lists in the input list

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]), 4)

if __name__ == '__main__':
    unittest.main()