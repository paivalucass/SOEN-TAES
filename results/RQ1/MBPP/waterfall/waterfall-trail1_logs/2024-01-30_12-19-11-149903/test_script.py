def remove_dirty_chars(string1, string2):
    """
    This function removes characters from string1 that are present in string2.
    Args:
    string1: Input string from which characters need to be removed
    string2: String containing characters to be removed from string1
    Returns:
    result: String after removing characters present in string2
    """
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise ValueError("Input should be a string")

    result = ''.join([char for char in string1 if char not in string2])
    return result

def str_to_list(string):
    """
    This function converts the input string into a list.
    Args:
    string: Input string to be converted into a list
    Returns:
    char_list: List containing individual characters of the input string
    """
    if not isinstance(string, str):
        raise ValueError("Input should be a string")

    char_list = list(string)
    return char_list

# Test Cases:
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars('probasscurve', 'pros'), 'bacuve')

if __name__ == '__main__':
    unittest.main()