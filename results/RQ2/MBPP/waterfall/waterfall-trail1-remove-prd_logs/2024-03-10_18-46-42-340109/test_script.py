def find_Index(n): 
    def is_triangular(num):
        x = (8*num + 1)**0.5
        return x.is_integer()

    def triangular_number(digits):
        return int((0.5 * digits) * (digits + 1))

    if n < 1:
        return "Invalid input"

    index = 1
    while True:
        num = triangular_number(index)
        if len(str(num)) == n and is_triangular(num):
            return index
        index += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()