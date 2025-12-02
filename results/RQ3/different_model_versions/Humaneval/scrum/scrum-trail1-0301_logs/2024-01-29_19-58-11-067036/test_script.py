def total_match(lst1: list[str], lst2: list[str]) -> list[str]:
    """
    Accepts two lists of strings and returns the list that has
    a total number of characters in the all strings of the list less than the other list.

    If the two lists have the same number of chars, return the first list.
    """

    # check if input parameters are lists of strings
    if not all(isinstance(lst, list) and all(isinstance(s, str) for s in lst) for lst in (lst1, lst2)):
        raise TypeError("Input parameters must be lists of strings")

    # sub-function to calculate the total number of characters in a list of strings
    def total_chars(lst):
        return sum(map(len, lst))

    # compare the total number of characters in both lists and return the appropriate list
    if total_chars(lst1) <= total_chars(lst2):
        return lst1
    else:
        return lst2
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(total_match([], []), [])
        
    def test2(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])
        
    def test3(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])
        
    def test4(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])
        
    def test5(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

if __name__ == '__main__':
    unittest.main()