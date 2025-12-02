def sequential_search(dlist, item):
    for index, value in enumerate(dlist):
        if value == item:
            return (True, index)
    return (False, -1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19], 31), (True, 3))

if __name__ == '__main__':
    unittest.main()