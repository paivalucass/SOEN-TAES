def compare_one(a, b):
    if type(a) != type(b):
        return None
    if type(a) == str:
        a = a.replace(",", ".")
        b = b.replace(",", ".")
    if a == b:
        return None
    return max(a, b)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
    def test2(self):
        self.assertEqual(compare_one(1, "2,3"), "2,3")
    def test3(self):
        self.assertEqual(compare_one("5,1", "6"), "6")
    def test4(self):
        self.assertEqual(compare_one("1", 1), None)

if __name__ == '__main__':
    unittest.main()