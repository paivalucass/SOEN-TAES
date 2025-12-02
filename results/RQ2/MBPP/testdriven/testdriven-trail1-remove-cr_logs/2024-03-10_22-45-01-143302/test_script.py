def sort_sublists(list1):
    if not list1:
        return []

    def sort_sublist(sublist):
        string_elements = [element for element in sublist if isinstance(element, str)]
        if len(string_elements) != len(sublist):
            return f"Error: Invalid input - List contains non-string elements of type: {type(sublist[0]).__name__}"
        sorted_sublist = sorted(sublist, key=lambda x: (isinstance(x, str), x))
        return sorted_sublist

    result = [sort_sublist(sublist) for sublist in list1]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()