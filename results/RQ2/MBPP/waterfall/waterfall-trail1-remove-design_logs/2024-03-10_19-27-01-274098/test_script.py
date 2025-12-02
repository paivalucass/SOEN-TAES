def new_tuple(test_list, test_str):
    return tuple(test_list) + (test_str,)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()