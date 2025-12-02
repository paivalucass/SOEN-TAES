def remove_nested(test_tup):
    result = []
    for item in test_tup:
        if isinstance(item, tuple):
            result.extend(remove_nested(item))
        else:
            result.append(item)
    return tuple([item for item in result if not isinstance(item, tuple)])

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()