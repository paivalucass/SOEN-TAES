def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    first_type = type(test_tuple[0])
    for item in test_tuple:
        if type(item) != first_type:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()