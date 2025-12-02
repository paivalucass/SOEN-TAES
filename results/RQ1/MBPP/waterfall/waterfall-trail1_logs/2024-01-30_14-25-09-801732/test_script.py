def count_element_in_list(list1, x):
    count = 0  # Initialize the counter

    def count_element_helper(sublist):
        nonlocal count
        if isinstance(sublist, list):
            for item in sublist:
                count_element_helper(item)
        else:
            if sublist == x:
                count += 1

    for sublist in list1:
        count_element_helper(sublist)

    return count  # Return the final count of sublists containing the specified element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1), 3)

if __name__ == '__main__':
    unittest.main()