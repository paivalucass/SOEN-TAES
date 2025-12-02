def sample_nam(sample_names):
    total_length_of_names = 0
    for name in sample_names:
        if not name[0].islower():
            total_length_of_names += len(name)
    return total_length_of_names
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()