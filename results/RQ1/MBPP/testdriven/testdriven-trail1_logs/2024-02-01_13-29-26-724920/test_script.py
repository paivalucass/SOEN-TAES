def tuple_str_int(test_str):
    # Write a function to convert tuple string to integer tuple.
    # assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    
    import re
    
    try:
        if test_str == '':
            return "Error Handling: 'Input should not be empty'"
        
        pattern = r"\d+"
        match = re.findall(pattern, test_str)
        
        if len(match) != 3:
            return "Error Handling: 'Input format should be (x, y, z)'"
        
        result = tuple(map(int, match))
        return result
    
    except ValueError:
        return "Error Handling: 'Input should contain only integer values'"
    
    except Exception as e:
        return "Error Handling: " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()