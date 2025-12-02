def input_validation(lst):
    if not isinstance(lst, list) or not all(isinstance(item, str) for item in lst):
        return False
    return True

def total_match(lst1, lst2):
    if not input_validation(lst1):
        return "Error: Input is not a list or contains non-string elements"
    if not input_validation(lst2):
        return "Error: Input is not a list or contains non-string elements"
    
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)

    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst2 < total_chars_lst1:
        return lst2
    else:
        return lst1  # If the two lists have the same number of characters, return the first list.
import unittest

class Test(unittest.TestCase):
    def test_total_match(self):
        self.assertEqual(total_match([], []), [])
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

if __name__ == '__main__':
    unittest.main()