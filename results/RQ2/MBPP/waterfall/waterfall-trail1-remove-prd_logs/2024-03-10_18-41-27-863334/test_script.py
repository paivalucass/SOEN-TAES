def sort_sublists(list1):
    if not isinstance(list1, list):
        raise ValueError("Input must be a list of sublists")
    
    for sublist in list1:
        if not isinstance(sublist, list):
            raise ValueError("Input must be a list of sublists")
    
    return [sorted(sublist) for sublist in list1]
import unittest

class Test(unittest.TestCase):
    def test_sort_sublists(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()