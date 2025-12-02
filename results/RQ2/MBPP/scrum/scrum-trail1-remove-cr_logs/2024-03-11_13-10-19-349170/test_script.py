def convert_list_dictionary(l1, l2, l3):
    if len(l1) != len(l2) or len(l1) != len(l3) or len(l2) != len(l3):
        raise ValueError("Input lists must have the same length")

    nested_dicts = [{l1[i]: {l2[i]: l3[i]}} for i in range(len(l1))]

    return nested_dicts
import unittest

class Test(unittest.TestCase):
    def test_convert_list_dictionary(self):
        self.assertEqual(convert_list_dictionary(["S001", "S002", "S003", "S004"], ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"], [85, 98, 89, 92]), [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}])

if __name__ == '__main__':
    unittest.main()