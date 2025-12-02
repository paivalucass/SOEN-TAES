def sort_sublists(list1):
    if not list1 or not all(isinstance(sublist, list) for sublist in list1):
        return "Input is empty or contains non-list elements"

    for sublist in list1:
        sublist.sort()

    return list1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()