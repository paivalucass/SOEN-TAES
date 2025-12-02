def find_Index(n):
    index = 1
    num = 1
    while True:
        if len(str(num)) >= n:
            if len(str(num)) == n:
                return index
            else:
                return -1
        index += 1
        num = (index * (index + 1)) // 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()