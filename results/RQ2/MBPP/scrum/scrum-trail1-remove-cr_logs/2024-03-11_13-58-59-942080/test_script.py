def extract_index_list(l1, l2, l3):
    if not all(isinstance(lst, list) for lst in [l1, l2, l3]):
        raise TypeError("All inputs must be lists")
    if any(len(lst) == 0 for lst in [l1, l2, l3]):
        raise ValueError("Input lists cannot be empty")
    if len(set(map(len, [l1, l2, l3]))) != 1:
        raise ValueError("Input lists must be of the same length")

    result = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            result.append(l1[i])
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()