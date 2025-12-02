def tuple_str_int(test_str):
    if not test_str:
        raise ValueError("Input string is empty")
    
    values = test_str[1:-1].split(',')
    
    try:
        int_tuple = tuple([int(value) for value in values])
        return int_tuple
    except ValueError:
        raise ValueError("Invalid input")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int('(7, 8, 9)'), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()