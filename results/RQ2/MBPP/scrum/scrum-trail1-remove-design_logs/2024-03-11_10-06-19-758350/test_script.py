def search(arr):
    i = 0
    while i < len(arr):
        if i == len(arr) - 1 or arr[i] != arr[i+1]:
            return arr[i]
        i += 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()