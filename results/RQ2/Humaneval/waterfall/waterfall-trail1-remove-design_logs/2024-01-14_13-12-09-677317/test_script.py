def total_match(lst1, lst2):
    matching_elements = [word for word in lst1 if word.lower() in [x.lower() for x in lst2]]
    if sum(len(word) for word in lst1) < sum(len(word) for word in lst2):
        return lst1
    else:
        return matching_elements
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