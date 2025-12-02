def list_to_float(test_list):
    try:
        assert isinstance(test_list, list), "Input must be a list of lists"
        result = [tuple(float(x) for x in sublist) for sublist in test_list]
        return result
    except ValueError:
        return "Error handling for non-numeric strings"
    except AssertionError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_float([( "3", "4"), ( "1", "26.45"), ( "7.32", "8"), ( "4", "8")]), [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)])

if __name__ == '__main__':
    unittest.main()