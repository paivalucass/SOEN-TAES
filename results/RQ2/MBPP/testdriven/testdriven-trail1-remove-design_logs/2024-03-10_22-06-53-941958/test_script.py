def min_val(listval):
    numeric_list = [x for x in listval if isinstance(x, (int, float))]

    if len(numeric_list) == 0:
        return "Error: Input list is empty"
    else:
        return min(numeric_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()