def insert_element(lst, element):
    if not lst:
        return "Error: Input list is empty."

    if element is None:
        return "Error: Element not provided."

    if not isinstance(element, str):
        return "Error: Element should be a string."

    result = []
    for item in lst:
        result.append(element)
        result.append(item)

    return result

# Test the function
assert insert_element([], 'c') == "Error: Input list is empty."
assert insert_element(['Red', 'Green', 'Black'], None) == "Error: Element not provided."
assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
import unittest

class Test(unittest.TestCase):
    def test_insert_element(self):
        self.assertEqual(insert_element(['Red', 'Green', 'Black'], 'c'), ['c', 'Red', 'c', 'Green', 'c', 'Black'])

if __name__ == '__main__':
    unittest.main()