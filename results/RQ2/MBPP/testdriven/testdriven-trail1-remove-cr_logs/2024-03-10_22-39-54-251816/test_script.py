def min_val(input_list):
    try:
        return min([x for x in input_list if isinstance(x, (int, float))])
    except ValueError:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()