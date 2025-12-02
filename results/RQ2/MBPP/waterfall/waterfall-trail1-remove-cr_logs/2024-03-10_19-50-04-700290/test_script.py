def remove_dirty_chars(string1, string2):
    '''
    Write a function to remove characters from the first string which are present in the second string.
    Args:
    string1: The first string
    string2: The second string
    Returns:
    A new string with characters from string1 that are not present in string2
    '''
    if string1 is None:
        return 'None'
    common_chars = set(string2)
    result = ''.join(char for char in string1 if char not in common_chars)
    return result

assert remove_dirty_chars("", "") == ""
assert remove_dirty_chars("abc$def", "abc") == "$def"
assert remove_dirty_chars(None, "abc") == "None"
assert remove_dirty_chars("xyz", "abc") == "xyz"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()