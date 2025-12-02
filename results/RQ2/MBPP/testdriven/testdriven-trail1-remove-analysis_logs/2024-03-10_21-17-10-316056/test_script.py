def add_string(list_, string):
    modified_list = [string.format(x) for x in list_]
    return modified_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_string([1,2,3,4],'temp{0}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()