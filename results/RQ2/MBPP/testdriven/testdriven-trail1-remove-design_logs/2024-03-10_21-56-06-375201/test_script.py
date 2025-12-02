def recursive_list_sum(data_list):
    """
    Write a function to flatten a list and sum all of its elements.
    """
    if not data_list:
        return 0
    total = 0
    for element in data_list:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        elif isinstance(element, int):
            total += element
        else:
            return "Error: Non-integer element in the list"
    return total
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], [5, 6]]), 21)

if __name__ == '__main__':
    unittest.main()