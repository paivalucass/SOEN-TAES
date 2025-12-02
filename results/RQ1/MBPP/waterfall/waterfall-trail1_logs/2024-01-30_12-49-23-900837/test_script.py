def insert_element(lst, element):
    result = []
    for item in lst:
        result.extend([element, item])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(insert_element(['Red', 'Green', 'Black'], 'c'), ['c', 'Red', 'c', 'Green', 'c', 'Black'])

if __name__ == '__main__':
    unittest.main()