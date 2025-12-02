def flatten_list(list1):
    return [item for sublist in list1 for item in (flatten_list(sublist) if isinstance(sublist, list) else [sublist])]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]), 
                         [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

if __name__ == '__main__':
    unittest.main()