def check_element(lst, element):
    return all(item == element for item in lst) if lst else False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_element(["green", "orange", "black", "white"], 'blue'), False)

if __name__ == '__main__':
    unittest.main()