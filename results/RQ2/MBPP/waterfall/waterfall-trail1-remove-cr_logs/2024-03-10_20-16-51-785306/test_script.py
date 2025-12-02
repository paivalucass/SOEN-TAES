def extract_index_list(l1, l2, l3):
    if not all(isinstance(i, list) for i in [l1, l2, l3]):
        raise ValueError("Input parameters must be lists")
    
    if len(set(map(len, [l1, l2, l3]))) != 1:
        raise ValueError("Input lists must be of equal length")

    result = [l1[i] for i in range(len(l1)) if l1[i] == l2[i] == l3[i]]
    
    if not result:
        return "No common elements found"
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_extract_index_list(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()