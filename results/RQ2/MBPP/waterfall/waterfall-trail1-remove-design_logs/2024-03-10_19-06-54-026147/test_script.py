def list_to_float(test_list):
    result = []
    for inner_list in test_list:
        try:
            converted_inner_list = [float(x) if x.replace('.', '', 1).isdigit() else x for x in inner_list]
            result.append(tuple(map(float, converted_inner_list)))
        except AttributeError:
            pass
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_float([( "3", "4"), ( "1", "26.45"), ( "7.32", "8"), ( "4", "8")]), [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)])

if __name__ == '__main__':
    unittest.main()