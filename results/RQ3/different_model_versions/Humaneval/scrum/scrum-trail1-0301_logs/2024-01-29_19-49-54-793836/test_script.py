def strlen(string: str) -> int:
    """
    Return length of given string, array, or object

    :param string: input string, array, or object
    :type string: str, list, dict
    :return: length of input
    :rtype: int
    :raise TypeError: when invalid input type is provided
    """
    if type(string) == str:
        return len(string)
    elif type(string) == list or type(string) == dict:
        return len(str(string))
    else:
        raise TypeError("Invalid input type. Please provide a string, array, or object.")
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_string_with_characters(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()