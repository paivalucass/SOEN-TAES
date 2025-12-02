def find_Index(n):
    index = 1
    triangle_num = 1
    while True:
        if len(str(triangle_num)) >= n:
            return index
        index += 1
        triangle_num += index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()