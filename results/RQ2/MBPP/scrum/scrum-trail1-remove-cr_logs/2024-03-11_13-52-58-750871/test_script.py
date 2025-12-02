def sample_nam(sample_names):
    if not all(isinstance(name, str) for name in sample_names):
        raise ValueError("Input should be a list of strings")

    filtered_names = [name for name in sample_names if name[0].isupper()]

    return sum(len(name) for name in filtered_names)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()