def list_to_float(test_list):
    new_list = []
    for sub_list in test_list:
        temp = [float(item) if item.replace('.', '', 1).isdigit() else None for item in sub_list]
        new_list.append(tuple(temp))
    return new_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]), [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)])

if __name__ == '__main__':
    unittest.main()