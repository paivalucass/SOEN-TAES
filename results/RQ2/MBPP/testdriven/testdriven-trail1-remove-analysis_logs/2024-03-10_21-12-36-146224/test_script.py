def check_type(test_tuple):
    if all(type(element) == type(test_tuple[0]) for element in test_tuple):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()