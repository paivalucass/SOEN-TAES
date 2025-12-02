def concatenate_tuple(input_tuple, delimiter='-'):
    if not input_tuple:
        return ''
    if not isinstance(delimiter, str):
        raise ValueError("Delimiter must be a string")

    concatenated_string = ''
    for element in input_tuple:
        if not isinstance(element, str):
            element = str(element)
        concatenated_string += element + delimiter
    
    return concatenated_string[:-1]
import unittest

class Test(unittest.TestCase):
    def test_concatenate_tuple(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()