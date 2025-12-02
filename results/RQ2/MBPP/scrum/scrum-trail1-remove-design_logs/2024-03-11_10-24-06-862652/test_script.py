def check_element(lst, element):
    if not lst:
        return False
    for item in lst:
        if item != element:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_check_element(self):
        self.assertEqual(check_element(["green", "orange", "black", "white"], 'blue'), False)

if __name__ == '__main__':
    unittest.main()