def sort_sublists(list1):
    try:
        for sublist in list1:
            if not isinstance(sublist, list):
                raise TypeError("Input is not a list of lists.")
            for element in sublist:
                if not isinstance(element, str):
                    raise TypeError("Sublists contain non-string elements.")
        return [sorted(sublist) for sublist in list1]
    except TypeError as e:
        return e
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()