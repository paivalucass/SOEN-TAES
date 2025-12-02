def find_Index(n):
    num = 1
    while True:
        tri_num = (num * (num + 1)) // 2
        if len(str(tri_num)) >= n:
            return num
        num += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()