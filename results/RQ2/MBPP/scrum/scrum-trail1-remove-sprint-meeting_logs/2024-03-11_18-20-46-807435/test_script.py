def empty_dit(list1):
    for dictionary in list1:
        if len(dictionary) > 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()