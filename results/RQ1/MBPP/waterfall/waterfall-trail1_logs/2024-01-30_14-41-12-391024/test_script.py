def sort_sublists(list1):
    if not isinstance(list1, list):
        raise TypeError("Input must be a list")
    
    for sublist in list1:
        if not isinstance(sublist, list):
            raise TypeError("Each element in the input list must be a list")

    sorted_lists = []
    for sublist in list1:
        sorted_lists.append(sorted(sublist))
    return sorted_lists
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()