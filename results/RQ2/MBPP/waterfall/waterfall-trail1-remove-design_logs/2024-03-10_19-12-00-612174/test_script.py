def check_element(lst, element):
    if all(item == element for item in lst):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_check_element(self):
        self.assertEqual(check_element(["green", "orange", "black", "white"], 'blue'), False)

if __name__ == '__main__':
    unittest.main()