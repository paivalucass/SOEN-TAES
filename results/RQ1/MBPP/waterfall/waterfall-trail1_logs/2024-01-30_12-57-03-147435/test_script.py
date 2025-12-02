def check_element(input_list, element):
    """
    Function to check whether all items in the list are equal to the given element.

    Args:
        input_list: input list in the form of an array
        element: single value to be checked for equality

    Returns:
        bool: True if all items in the list are equal to the given element, False otherwise
    """
    if not input_list:
        raise ValueError("Input list cannot be empty")

    return all(item == element for item in input_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_element(["green", "orange", "black", "white"], 'blue'), False)

if __name__ == '__main__':
    unittest.main()