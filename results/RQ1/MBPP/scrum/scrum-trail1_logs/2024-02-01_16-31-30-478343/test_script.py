def sample_nam(sample_names):
    try:
        if not isinstance(sample_names, list):
            raise TypeError("Input should be a list of names")
        # Filter out names that start with a lowercase letter
        filtered_names = [name for name in sample_names if not name[0].islower()]
        # Calculate the length of the remaining names and sum them up
        total_length = sum(len(name) for name in filtered_names)
        return total_length
    except TypeError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()