def all_unique(test_list):
    if not isinstance(test_list, list):
        return "Error"
    if len(test_list) < 2:
        return True
    unique_elements = set()
    for element in test_list:
        if element in unique_elements:
            return False
        unique_elements.add(element)
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()