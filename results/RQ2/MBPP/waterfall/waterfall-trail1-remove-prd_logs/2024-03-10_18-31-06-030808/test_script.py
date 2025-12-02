def check_type(test_tuple):
    try:
        if len(test_tuple) < 2:
            return "Error: Input tuple must have at least two elements"
        else:
            first_type = type(test_tuple[0])
            for element in test_tuple:
                if type(element) != first_type:
                    return "Error: All elements in the tuple must have the same type"
            return True
    except:
        return "Error: Invalid input tuple"
import unittest

class Test(unittest.TestCase):
    def test_check_type(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()