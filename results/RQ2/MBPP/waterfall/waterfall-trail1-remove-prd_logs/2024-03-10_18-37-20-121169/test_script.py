def find_max_string(input_list: list) -> list:
    if not input_list:
        return ["Input list is empty"]
    
    if not all(isinstance(x, str) for x in input_list):
        return ["Input list should contain only strings"]
    
    max_length = 0
    max_elements = []
    
    for element in input_list:
        if len(element) > max_length:
            max_length = len(element)
            max_elements = [element]
        elif len(element) == max_length:
            max_elements.append(element)
    
    return max_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()