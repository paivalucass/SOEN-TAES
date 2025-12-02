def unique_sublists(list1):
    '''
    Write a function to count the number of lists within a list. 
    The function should return a dictionary, where every list is turned to a tuple, 
    and the value of the tuple is the number of its occurrences.
    '''
    sublist_count = {}
    for sublist in list1:
        if isinstance(sublist, list):
            tuple_sublist = tuple(sublist)
            if tuple_sublist in sublist_count:
                sublist_count[tuple_sublist] += 1
            else:
                sublist_count[tuple_sublist] = 1
    return sublist_count

assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()