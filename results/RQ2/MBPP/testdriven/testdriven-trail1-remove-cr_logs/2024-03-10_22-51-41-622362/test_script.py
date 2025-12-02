def min_k(test_list, K):
    if not isinstance(test_list, list) or not all(isinstance(t, tuple) and len(t) >= 2 and isinstance(t[1], (int, float)) for t in test_list):
        raise TypeError("Input tuple list should be a list of tuples with at least two elements and the second element should be a number")
    
    if not isinstance(K, int):
        raise TypeError("K should be an integer")

    if not test_list:
        raise ValueError("Tuple list is empty")
    
    if len(test_list) < K:
        raise ValueError("Tuple list has fewer than K records")
    
    second_elements = [t[1] for t in test_list]
    if len(second_elements) != len(set(second_elements)):
        raise ValueError("Tuple list has duplicate second elements")

    test_list.sort(key=lambda x: x[1])
    return test_list[:K]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2), [('Akash', 2), ('Akshat', 4)])

if __name__ == '__main__':
    unittest.main()