def add_string(list_, string):
    if list_ is None:
        return "Error: Input list is None"
    if string is None:
        return "Error: Format string is not provided"
    
    formatted_list = [string.format(element) for element in list_]
    
    return formatted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_string([1,2,3,4],'temp{0}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()