def empty_dit(list1):
    if not list1:
        return True
    for item in list1:
        if not isinstance(item, dict) or item:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()