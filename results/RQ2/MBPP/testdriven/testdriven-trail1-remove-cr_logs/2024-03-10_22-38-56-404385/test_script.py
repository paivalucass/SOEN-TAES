def convert_list_dictionary(l1, l2, l3):
    result = []
    if len(l1) != len(l2) or len(l1) != len(l3) or len(l2) != len(l3):
        return "Error: Input lists should have the same length"
    elif len(l1) == 0:
        return "Error: Input lists should not be empty"
    else:
        for i in range(len(l1)):
            if l1.count(l1[i]) > 1:
                return "Error: Student IDs should be unique"
            else:
                nested_dict = {l1[i]: {l2[i]: l3[i]}}
                result.append(nested_dict)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92]), [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}])

if __name__ == '__main__':
    unittest.main()