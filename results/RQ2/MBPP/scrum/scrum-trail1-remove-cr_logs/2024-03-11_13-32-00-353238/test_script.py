def sort_sublists(list1):
    def sort_single_sublist(sublist):
        return sorted(sublist)
    
    def iterate_and_sort(list_of_lists):
        return [sort_single_sublist(sublist) for sublist in list_of_lists]

    return iterate_and_sort(list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()