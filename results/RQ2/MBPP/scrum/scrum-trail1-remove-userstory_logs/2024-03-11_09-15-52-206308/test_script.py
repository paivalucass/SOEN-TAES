def sort_sublists(list1):
    if not isinstance(list1, list):
        raise TypeError("Input should be a list of lists")

    for sublist in list1:
        if not all(isinstance(item, str) for item in sublist):
            raise ValueError("Sublists should only contain strings")

    for sublist in list1:
        sublist.sort()

    return list1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()