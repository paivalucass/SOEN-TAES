def compare_one(a, b):
    try:
        a = float(a.replace(',', '.')) if isinstance(a, str) else float(a)
        b = float(b.replace(',', '.')) if isinstance(b, str) else float(b)

        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None

    except ValueError:
        return None

    except TypeError:
        return None
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