def empty_dit(list1):
    return all(not bool(d) for d in list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()