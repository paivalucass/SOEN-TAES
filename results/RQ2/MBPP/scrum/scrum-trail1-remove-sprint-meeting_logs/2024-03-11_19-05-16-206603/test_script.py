def find_Index(n):
    index = 1
    triangular_number = 1
    while len(str(triangular_number)) < n:
        index += 1
        triangular_number += index
    return index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()