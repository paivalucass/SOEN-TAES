def concatenate_tuple(test_tup):
    result = ""
    for element in test_tup:
        if isinstance(element, str):
            result += element
        elif isinstance(element, int):
            result += str(element)
        if element != test_tup[-1]:
            result += "-"
    return result
import unittest

class Test(unittest.TestCase):
    def test_concatenate_tuple(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()