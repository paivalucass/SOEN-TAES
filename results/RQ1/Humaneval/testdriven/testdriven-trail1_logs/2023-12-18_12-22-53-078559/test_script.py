def unique(l: list) -> list:
    """
    Return sorted unique elements in a list
    :param l: input list
    :return: sorted list of unique elements
    """
    return sorted(list(set(l)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

if __name__ == '__main__':
    unittest.main()