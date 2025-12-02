def empty_list(length):
    return [{} for _ in range(length)]
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(5), [{}, {}, {}, {}, {}])

if __name__ == '__main__':
    unittest.main()