def tuple_str_int(test_str):
    try:
        if not isinstance(test_str, str):
            raise ValueError("Error: Input is not a string")

        if len(test_str) < 3:
            raise ValueError("Error: Input tuple string is empty")

        elements = test_str[1:-1].split(',')
        
        int_tuple = tuple(int(x) for x in elements)
        
        return int_tuple
    except ValueError as ve:
        return str(ve)
    except Exception:
        return "Error: Something went wrong"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()