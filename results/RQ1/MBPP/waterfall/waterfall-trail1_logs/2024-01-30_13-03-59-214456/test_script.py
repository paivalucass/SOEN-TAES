def add_string(list_, string):
    if all(isinstance(element, int) for element in list_):
        modified_list = [string.format(element) for element in list_]
        return modified_list
    else:
        return []

assert add_string([1,2,3,4],'temp{0}') == ['temp1', 'temp2', 'temp3', 'temp4']
import unittest

class Test(unittest.TestCase):
    def test_add_string(self):
        self.assertEqual(add_string([1,2,3,4],'temp{0}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()