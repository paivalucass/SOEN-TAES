def extract_index_list(*lists):
    '''We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.'''
    if len(set(len(lst) for lst in lists)) != 1:
        return []  # Return empty list if input lists have different lengths

    common_elements = []
    for i in range(len(lists[0])):
        if all(lst[i] == lists[0][i] for lst in lists):
            common_elements.append(lists[0][i])
    return common_elements

assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]) == [1, 7]  # Add more test cases for edge scenarios as suggested by the Tester role.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()