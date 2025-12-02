def remove_nested(test_tup):
    result_list = []
    for item in test_tup:
        if not isinstance(item, tuple):
            result_list.append(item)
        else:
            result_list.extend(remove_nested(item))
    return tuple(result_list)
import unittest

class Test(unittest.TestCase):
    def test_remove_nested(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()