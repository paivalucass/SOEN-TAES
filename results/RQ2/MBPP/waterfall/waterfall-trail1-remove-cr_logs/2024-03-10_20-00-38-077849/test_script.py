def flatten_list(list1):
    flat_list = []
    for item in list1:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

if __name__ == '__main__':
    unittest.main()