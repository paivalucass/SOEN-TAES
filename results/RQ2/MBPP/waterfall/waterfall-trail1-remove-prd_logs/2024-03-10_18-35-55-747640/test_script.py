def convert_list_dictionary(l1, l2, l3):
    if len(l1) != len(l2) or len(l1) != len(l3) or len(l2) != len(l3):
        return "Error: input lists are of different lengths"
    
    if not l1 or not l2 or not l3:
        return "Error: input lists are empty"

    nested_dict_list = []

    for i in range(len(l1)):
        if not isinstance(l1[i], str) or not isinstance(l2[i], str) or not isinstance(l3[i], int):
            return "Error: invalid input"

        if l1[i] in [x.keys() for x in nested_dict_list]:
            return "Error: duplicate student ID"

        nested_dict = {l1[i]: {l2[i]: l3[i]}}
        nested_dict_list.append(nested_dict)

    return nested_dict_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92]), [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}])

if __name__ == '__main__':
    unittest.main()