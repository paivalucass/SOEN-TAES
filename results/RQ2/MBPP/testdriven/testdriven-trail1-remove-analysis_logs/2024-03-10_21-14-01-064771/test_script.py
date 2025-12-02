def insert_element(lst, element):
    if not isinstance(lst, list):
        return "Error: Invalid input"
    result = []
    for item in lst:
        result.append(element)
        result.append(item)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(insert_element(['Red', 'Green', 'Black'], 'c'), ['c', 'Red', 'c', 'Green', 'c', 'Black'])

if __name__ == '__main__':
    unittest.main()