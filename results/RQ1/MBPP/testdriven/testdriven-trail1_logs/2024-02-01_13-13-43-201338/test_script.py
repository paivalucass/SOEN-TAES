def sample_nam(sample_names):
    '''
    Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    '''

    # Input validation
    if not all(isinstance(name, str) for name in sample_names):
        raise ValueError("Input must be a list of strings")

    # Remove names that start with a lowercase letter
    filtered_names = [name for name in sample_names if name[0].isupper()]

    # Sum the length of the filtered names
    total_length = sum(len(name) for name in filtered_names)

    return total_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()