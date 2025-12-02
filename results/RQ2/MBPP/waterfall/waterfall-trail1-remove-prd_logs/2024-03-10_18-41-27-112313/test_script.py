def empty_list(length):
    if not isinstance(length, int) or length < 0:
        raise ValueError("Length should be a non-negative integer")

    result = [{} for _ in range(length)]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()