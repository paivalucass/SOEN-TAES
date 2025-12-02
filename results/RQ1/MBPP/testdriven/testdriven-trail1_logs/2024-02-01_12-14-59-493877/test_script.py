def odd_values_string(input_string):
    '''This function removes the characters which have odd index values of a given string.'''
    modified_string = ''.join([input_string[i] for i in range(len(input_string)) if i % 2 == 0])
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()