def find_index_of_smallest_triangular_number(n):
    index = 1
    while True:
        triangular_number = index * (index + 1) // 2
        if len(str(triangular_number)) >= n:
            return index
        index += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()