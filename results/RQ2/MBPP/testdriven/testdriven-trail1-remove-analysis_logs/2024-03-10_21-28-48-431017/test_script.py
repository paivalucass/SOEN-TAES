def unique_sublists(list1):
    from collections import defaultdict
    result = defaultdict(int)
    for sub_list in list1:
        sub_tuple = tuple(sub_list)
        result[sub_tuple] += 1
    return result

# Test cases
print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))  # Output should be {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
import unittest

class Test(unittest.TestCase):
    def test_unique_sublists(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()