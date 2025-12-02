def find_Index(n):
    i = 1
    while True:
        triangular_number = (i * (i + 1)) / 2
        if len(str(int(triangular_number))) == n:
            return i
        i += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()