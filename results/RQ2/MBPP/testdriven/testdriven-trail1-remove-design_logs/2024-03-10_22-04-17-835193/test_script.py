def check_element(list, element):
    for item in list:
        if item == element:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test_check_element(self):
        self.assertEqual(check_element(["green", "orange", "black", "white"], 'blue'), False)

if __name__ == '__main__':
    unittest.main()