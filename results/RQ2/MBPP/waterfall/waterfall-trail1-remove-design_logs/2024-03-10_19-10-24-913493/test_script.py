def insert_element(lst, element):
    new_list = []
    for item in lst:
        new_list.append(element)
        new_list.append(item)
    return new_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(insert_element(['Red', 'Green', 'Black'], 'c'), ['c', 'Red', 'c', 'Green', 'c', 'Black'])

if __name__ == '__main__':
    unittest.main()