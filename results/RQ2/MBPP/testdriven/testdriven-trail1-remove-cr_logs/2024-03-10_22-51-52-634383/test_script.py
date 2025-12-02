def extract_index_list(l1, l2, l3):
    common_elements = []
    if isinstance(l1, list) and isinstance(l2, list) and isinstance(l3, list):
        for i in range(min(len(l1), len(l2), len(l3))):
            if l1[i] == l2[i] == l3[i]:
                common_elements.append(l1[i])
        return common_elements
    else:
        raise ValueError("Input parameters must be lists")

# Test cases
print(extract_index_list([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7])) # [1, 7]
print(extract_index_list([], [], [])) # []
print(extract_index_list([1, 2, 3], [4, 5, 6], [7, 8, 9])) # []
print(extract_index_list([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [1, 1, 2, 3, 4, 5, 7])) # [1, 7]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()