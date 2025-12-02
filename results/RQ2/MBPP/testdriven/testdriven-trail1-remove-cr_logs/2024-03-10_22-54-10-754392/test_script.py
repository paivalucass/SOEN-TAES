def new_tuple(test_list, test_str):
    new_tuple = tuple(test_list) + (test_str,)
    return new_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()