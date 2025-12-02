def unique_sublists(list1):
    unique_sublists_dict = {}
    if not isinstance(list1, list):
        raise TypeError("Input should be a list of lists")

    if len(list1) == 0:
        return unique_sublists_dict

    for sublist in list1:
        if not isinstance(sublist, list):
            raise TypeError("Input should be a list of lists")

        sublist_tuple = tuple(sublist)
        if sublist_tuple in unique_sublists_dict:
            unique_sublists_dict[sublist_tuple] += 1
        else:
            unique_sublists_dict[sublist_tuple] = 1

    return unique_sublists_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()