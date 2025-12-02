def sequential_search(dlist, item):
    index = 0
    found = False
    while index < len(dlist) and not found:
        if dlist[index] == item:
            found = True
        else:
            index = index + 1
    if found:
        return (found, index)
    else:
        return (found, -1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19], 31), (True, 3))

if __name__ == '__main__':
    unittest.main()