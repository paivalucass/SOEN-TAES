def tuple_str_int(test_str):
    try:
        result = eval(test_str)
        if isinstance(result, tuple) and all(isinstance(item, int) for item in result):
            return result
        else:
            raise ValueError
    except (SyntaxError, ValueError, TypeError):
        return "Error or Exception"
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()