def list_to_float(test_list):
    try:
        new_list = [(float(elem[0]), float(elem[1])) for elem in test_list]
        return new_list
    except (ValueError, TypeError) as e:
        return "Invalid input: " + str(e)
    except Exception as e:
        return "An error occurred: " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_float([( "3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]), [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)])

if __name__ == '__main__':
    unittest.main()