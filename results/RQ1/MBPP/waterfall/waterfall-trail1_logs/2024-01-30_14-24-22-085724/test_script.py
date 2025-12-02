def concatenate_tuple(test_tup, delimiter='-'):
    if not test_tup:
        return "Input tuple is empty"

    if not all(isinstance(element, str) for element in test_tup):
        test_tup = [str(i) for i in test_tup]

    concatenated_string = delimiter.join(test_tup)
    return concatenated_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()