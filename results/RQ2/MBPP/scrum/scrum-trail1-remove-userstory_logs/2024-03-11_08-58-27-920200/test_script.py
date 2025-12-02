def check_type(test_tuple):
    if not isinstance(test_tuple, tuple):
        return "Error"

    if len(test_tuple) < 2:
        return True

    type_set = {type(i) for i in test_tuple}
    return len(type_set) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()