def check_element(lst, element):
    if element is None or not lst or not all(item == element for item in lst):
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_element(["green", "orange", "black", "white"], 'blue'), False)

if __name__ == '__main__':
    unittest.main()