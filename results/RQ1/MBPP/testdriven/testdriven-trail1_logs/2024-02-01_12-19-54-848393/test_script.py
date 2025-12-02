def insert_element(input_list, new_element):
    result = []
    for item in input_list:
        result.append(new_element)
        result.append(item)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(insert_element(['Red', 'Green', 'Black'], 'c'), ['c', 'Red', 'c', 'Green', 'c', 'Black'])

if __name__ == '__main__':
    unittest.main()