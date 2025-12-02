def split(input_list):
    if not isinstance(input_list, list):
        return "Error: Input is not a list"
    else:
        return [x for x in input_list if x % 2 != 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5,6]), [1,3,5])

if __name__ == '__main__':
    unittest.main()