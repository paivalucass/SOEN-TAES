def tuple_str_int(test_str):
    try:
        result = eval(test_str)
        if isinstance(result, tuple):
            return result
        else:
            return "Error: Invalid input data"
    except NameError:
        return "Error: Invalid input data"
    except SyntaxError:
        return "Error: Invalid input data"
    except Exception as e:
        return "Error: " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()