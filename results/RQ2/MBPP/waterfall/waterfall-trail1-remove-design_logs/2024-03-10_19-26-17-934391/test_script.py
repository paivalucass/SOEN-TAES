def unique_sublists(list1):
    unique_lists = {}
    for sublist in list1:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in unique_lists:
            unique_lists[sublist_tuple] += 1
        else:
            unique_lists[sublist_tuple] = 1
    return unique_lists

# Test cases
print(unique_sublists([[1, 2], [3, 4], [1, 2]]))  # Expected output: {(1, 2): 2, (3, 4): 1}
print(unique_sublists([]))  # Expected output: {}
print(unique_sublists([[1, 2]]))  # Expected output: {(1, 2): 1}
print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))  # Expected output: {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
import unittest

class Test(unittest.TestCase):
    def test_unique_sublists(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()