def extract_index_list(l1, l2, l3):
    if len(l1) != len(l2) or len(l1) != len(l3):
        return []

    result = [el1 for el1, el2, el3 in zip(l1, l2, l3) if el1 == el2 == el3]
    return result

try:
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    assert extract_index_list([1, 2, 3],[4, 5, 6],[7, 8, 9])==[]
    assert extract_index_list([1, 2, 3, 4, 5],[1, 2, 3, 4],[1, 2, 3])==[1, 2, 3]
    assert extract_index_list([1, 2, 3],['a', 'b', 'c'],[True, False, True])=="Error: Invalid input data types"
except Exception as e:
    print(e)
import unittest

class Test(unittest.TestCase):
    def test_extract_index_list(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()