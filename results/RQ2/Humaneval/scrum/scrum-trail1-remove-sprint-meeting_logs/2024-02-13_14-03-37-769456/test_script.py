def total_match(lst1, lst2):
    try:
        if not all(isinstance(x, str) for x in lst1) or not all(isinstance(x, str) for x in lst2):
            raise ValueError("Both inputs must be lists of strings")
    except:
        return "Error: Both inputs must be lists of strings"

    total_chars_lst1 = sum(len(x) for x in lst1)
    total_chars_lst2 = sum(len(x) for x in lst2)

    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst2 < total_chars_lst1:
        return lst2
    else:
        return lst1
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