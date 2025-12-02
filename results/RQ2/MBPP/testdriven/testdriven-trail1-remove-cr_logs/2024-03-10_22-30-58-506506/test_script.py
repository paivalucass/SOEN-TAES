def empty_dict(list1):
    return all(not d for d in list1)
import unittest

class Test(unittest.TestCase):
    def test_empty_dit(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()