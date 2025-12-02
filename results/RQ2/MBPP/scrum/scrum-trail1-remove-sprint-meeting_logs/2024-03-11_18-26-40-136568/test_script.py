def check_type(test_tuple):
    if len(test_tuple) == 0:
        raise ValueError("Input tuple is empty")
    
    expected_type = type(test_tuple[0])

    for element in test_tuple:
        if type(element) != expected_type:
            return False

    return True
import unittest

class Test(unittest.TestCase):
    def test_check_type(self):
        self.assertTrue(check_type((5, 6, 7, 3, 5, 6)))
        self.assertFalse(check_type(('a', 'b', 5, 6)))

if __name__ == '__main__':
    unittest.main()