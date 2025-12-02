def sort_sublists(list1):
    for sublist in list1:
        if not all(isinstance(item, str) for item in sublist):
            return "Error: Input data is not a list of strings"
        sublist.sort()
    return list1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()