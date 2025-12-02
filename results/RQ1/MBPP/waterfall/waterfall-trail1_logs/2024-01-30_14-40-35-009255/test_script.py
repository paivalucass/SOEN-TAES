def empty_list(length):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer")

    empty_dict_list = [{} for _ in range(length)]
    return empty_dict_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()