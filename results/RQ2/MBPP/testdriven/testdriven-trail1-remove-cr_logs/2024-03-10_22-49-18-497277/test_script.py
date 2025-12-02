def sample_nam(sample_names):
    '''Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16'''
    def remove_lower_case_names(names):
        if not isinstance(names, list):
            raise TypeError("Input must be a list of names")
        modified_names = [name for name in names if not name[0].islower()]
        return modified_names

    def sum_name_length(names):
        if not isinstance(names, list):
            raise TypeError("Input must be a list of names")
        sum_length = sum(len(name) for name in names)
        return sum_length

    modified_names = remove_lower_case_names(sample_names)
    result = sum_name_length(modified_names)
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()