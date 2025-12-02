def remove_nested(test_tup):
    new_list = []
    for item in test_tup:
        if isinstance(item, tuple):
            new_list.extend(item)
        else:
            new_list.append(item)
    return tuple([x for x in new_list if not isinstance(x, tuple)])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()