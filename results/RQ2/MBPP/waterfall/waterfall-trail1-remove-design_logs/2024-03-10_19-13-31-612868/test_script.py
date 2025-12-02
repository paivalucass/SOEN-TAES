def add_string(list_, string):
    if not list_ or not string:
        raise ValueError("Input list_ and string should not be empty or null")

    return [string.format(x) for x in list_]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_string([1,2,3,4],'temp{0}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()