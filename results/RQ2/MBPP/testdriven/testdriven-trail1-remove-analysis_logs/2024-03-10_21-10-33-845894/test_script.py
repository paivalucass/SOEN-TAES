def empty_dict(list1):
    return all(not bool(dictionary) for dictionary in list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()