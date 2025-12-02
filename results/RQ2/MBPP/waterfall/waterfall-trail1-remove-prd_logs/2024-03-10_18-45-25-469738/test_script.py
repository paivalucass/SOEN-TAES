def sample_nam(sample_names):
    valid_names = [name for name in sample_names if not name[0].islower()]
    total_length = sum(len(name) for name in valid_names)
    return total_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()