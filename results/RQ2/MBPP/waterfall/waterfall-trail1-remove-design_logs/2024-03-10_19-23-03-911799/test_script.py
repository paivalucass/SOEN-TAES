def sample_nam(sample_names):
    if not isinstance(sample_names, list):
        raise ValueError("Input must be a list")
    
    total_length = 0
    for name in sample_names:
        if isinstance(name, str) and name[0].isupper():
            total_length += len(name)
    return total_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()