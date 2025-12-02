def unique(l: list) -> list:
    return sorted(list(set(l)))
import unittest

class Test(unittest.TestCase):
    def test_unique_elements(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

if __name__ == '__main__':
    unittest.main()