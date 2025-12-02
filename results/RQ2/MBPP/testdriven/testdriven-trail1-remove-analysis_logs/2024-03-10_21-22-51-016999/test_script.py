def sort_sublists(list1):
    for sublist in list1:
        if not all(isinstance(item, str) for item in sublist):
            raise ValueError("Input list should only contain sublists of strings")
    sorted_list = [sorted(sublist) for sublist in list1]
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()