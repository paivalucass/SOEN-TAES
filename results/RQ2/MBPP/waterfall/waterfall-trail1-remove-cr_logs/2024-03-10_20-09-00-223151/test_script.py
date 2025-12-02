def empty_list(length):
    try:
        assert isinstance(length, int) and length > 0, "Input parameter must be a positive integer"
        return [{} for _ in range(length)]
    except ValueError:
        raise ValueError("Invalid input, length must be a positive integer")
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()