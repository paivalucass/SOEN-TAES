def empty_list(length):
    if not isinstance(length, int) or length <= 0:
        raise AssertionError
    return [{} for _ in range(length)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()