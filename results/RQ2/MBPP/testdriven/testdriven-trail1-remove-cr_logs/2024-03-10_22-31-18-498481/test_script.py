def search(arr):
    for i in range(0, len(arr), 2):
        if i == len(arr)-1 or arr[i] != arr[i+1]:
            return arr[i]
    return None

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()