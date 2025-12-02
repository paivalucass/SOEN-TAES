def smallest_num(xs):
    if not xs:
        return "List is empty"
    if not all(isinstance(x, (int, float)) for x in xs):
        return "List contains non-numeric inputs"
    
    return min(xs)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()