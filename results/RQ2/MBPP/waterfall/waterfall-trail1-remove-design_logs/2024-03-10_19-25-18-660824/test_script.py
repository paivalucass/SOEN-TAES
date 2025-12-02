def unique_sublists(list1):
    unique_dict = {}
    for sub_list in list1:
        sub_tuple = tuple(sub_list)
        if sub_tuple in unique_dict:
            unique_dict[sub_tuple] += 1
        else:
            unique_dict[sub_tuple] = 1
    return unique_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()