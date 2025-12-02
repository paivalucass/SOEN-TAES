def sequential_search(dlist, item):
    found = False
    index = -1
    for i in range(len(dlist)):
        if dlist[i] == item:
            found = True
            index = i
            break
    return (found, index)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19], 31), (True, 3))

if __name__ == '__main__':
    unittest.main()