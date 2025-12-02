def min_val(listval):
    num_list = [i for i in listval if isinstance(i, int)]
    if not num_list:
        return None
    return min(num_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()