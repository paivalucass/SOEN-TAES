def tuple_str_int(test_str):
    try:
        # code to convert tuple string to integer tuple
        integer_tuple = tuple(map(int, test_str.strip('()').split(',')))
        return integer_tuple
    except ValueError:
        return "Invalid input"
    except Exception as e:
        return "Error: Invalid input format"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()