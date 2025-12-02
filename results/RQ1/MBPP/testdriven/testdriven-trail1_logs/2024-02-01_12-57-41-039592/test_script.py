def sort_sublists(list1):
    """
    Write a function to sort each sublist of strings in a given list of lists.
    assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    """
    
    if not isinstance(list1, list):
        raise ValueError("Input is not a list of sublists")

    sorted_list = [sorted(sublist) for sublist in list1]
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()