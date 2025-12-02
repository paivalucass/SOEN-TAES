def tuple_str_int(test_str):
    if test_str == "":
        return ()
    elif test_str.count(",") == 0:
        return (int(test_str.strip("()")),)
    else:
        try:
            return tuple(map(int, test_str.strip("()").split(",")))
        except ValueError:
            raise ValueError("Invalid characters in the input string")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int('(7, 8, 9)'), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()