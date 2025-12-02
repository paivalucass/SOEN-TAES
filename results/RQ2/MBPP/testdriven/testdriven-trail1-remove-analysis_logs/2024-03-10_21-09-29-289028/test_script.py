def find_substring(str_list, sub_str):
    """
    Function to check if a string is present as a substring in a given list of string values.
    
    Args:
    str_list (list): List of string values
    sub_str (str): Substring to search for
    
    Returns:
    bool: True if substring is found in any string in the list, False otherwise
    """
    # Input validation for empty string list and empty substring
    if not str_list or not sub_str:
        return False
    
    # Check for empty strings in str_list
    if any(not s for s in str_list):
        return False
    
    # Check for substring in str_list
    if any(sub_str in s for s in str_list):
        return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ack"), True)

if __name__ == '__main__':
    unittest.main()