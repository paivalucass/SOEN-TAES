def extract_index_list(l1, l2, l3):
    if not l1 or not l2 or not l3 or len(l1) != len(l2) or len(l1) != len(l3):
        return []

    common_elements = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            common_elements.append(l1[i])
    return common_elements

# Testing with input lists of different lengths
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
assert extract_index_list([1, 2, 3, 4],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[]
assert extract_index_list([],[],[])==[]
import unittest

class Test(unittest.TestCase):
    def test_common_elements(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()