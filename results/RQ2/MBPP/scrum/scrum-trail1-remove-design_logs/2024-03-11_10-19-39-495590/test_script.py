def insert_element(lst, element):
    new_lst = []
    for item in lst:
        new_lst.append(element)
        new_lst.append(item)
    return new_lst
import unittest

class Test(unittest.TestCase):
    def test_insert_element(self):
        self.assertEqual(insert_element(['Red', 'Green', 'Black'], 'c'), ['c', 'Red', 'c', 'Green', 'c', 'Black'])

if __name__ == '__main__':
    unittest.main()