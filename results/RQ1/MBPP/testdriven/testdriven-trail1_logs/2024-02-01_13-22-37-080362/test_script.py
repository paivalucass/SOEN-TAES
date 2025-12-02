def min_k(test_list, K):
    # Write a function to find minimum k records from tuple list
    # Implement a sorting algorithm to sort the tuple list based on the second element of each tuple
    # Return the minimum K records

    test_list.sort(key=lambda x: x[1])
    return test_list[:K]
import unittest

class Test(unittest.TestCase):
    def test_min_k(self):
        self.assertEqual(min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2), [('Akash', 2), ('Akshat', 4)])

if __name__ == '__main__':
    unittest.main()