def sample_nam(sample_names):
    filtered_names = [name for name in sample_names if name[0].isupper()]
    total_length = sum(len(name) for name in filtered_names)
    return total_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()