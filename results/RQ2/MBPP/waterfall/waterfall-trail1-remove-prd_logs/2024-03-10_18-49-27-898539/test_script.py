def new_tuple(input_list, input_string):
    return tuple(input_list + [input_string])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(new_tuple(["WEB", "is"], "best"), ('WEB', 'is', 'best'))

if __name__ == '__main__':
    unittest.main()