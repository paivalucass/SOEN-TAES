def remove_whitespaces(text1: str) -> str:
    '''
    This function removes all whitespaces from the given string.
    It handles cases where the input is not a string and adds comments to explain the purpose of the function.
    '''
    if not isinstance(text1, str):
        raise TypeError("Input must be a string")

    return ''.join(text1.split())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_whitespaces(' Google    Flutter '), 'GoogleFlutter')

if __name__ == '__main__':
    unittest.main()