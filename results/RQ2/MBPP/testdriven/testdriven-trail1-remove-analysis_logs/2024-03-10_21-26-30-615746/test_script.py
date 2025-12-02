def sample_nam(sample_names):
    '''Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.'''
    
    # function to filter out names starting with a lowercase letter
    def filter_names(names):
        return [name for name in names if not name[0].islower()]

    # function to calculate the length of names
    def calculate_length(names):
        return sum(len(name) for name in names)

    # input validation
    if not isinstance(sample_names, list):
        return "Invalid input. Please provide a list of strings."

    # filtering out names starting with a lowercase letter
    filtered_names = filter_names(sample_names)

    # calculating the length of names
    length = calculate_length(filtered_names)

    return length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()