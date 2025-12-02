def sample_nam(sample_names):
    if not isinstance(sample_names, list) or len(sample_names) == 0:
        return "Error: Input should be a non-empty list"

    sum_length = 0
    for name in sample_names:
        if not name[0].islower():
            sum_length += len(name)

    return sum_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()