def sequential_search(dlist, item):
    if not isinstance(dlist, list) or not dlist:
        return (False, -1)

    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)

    return (False, -1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19], 31), (True, 3))
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19], 100), (False, -1))

if __name__ == '__main__':
    unittest.main()