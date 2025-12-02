def remove_nested(test_tup):
    flat_list = []
    for item in test_tup:
        if isinstance(item, tuple):
            flat_list.extend(item)
        else:
            flat_list.append(item)
    return tuple([item for item in flat_list if not isinstance(item, tuple)])
import unittest

class Test(unittest.TestCase):
    def test_remove_nested(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()