def sample_nam(sample_names):
    try:
        if not isinstance(sample_names, list):
            raise TypeError("Input should be a list of names")

        valid_names = [name for name in sample_names if not name[0].islower()]
        sum_of_lengths = sum(len(name) for name in valid_names)

        return sum_of_lengths

    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']), 16)

if __name__ == '__main__':
    unittest.main()