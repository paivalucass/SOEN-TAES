def is_sublist(l, s):
    """
    This function checks if list s is a sublist of list l.
    
    Args:
    l (list): The main list
    s (list): The sublist to check
    
    Returns:
    bool: True if s is a sublist of l, False otherwise
    """
    if not isinstance(l, list) or not isinstance(s, list):
        raise TypeError("Input parameters must be lists")

    return all(item in l for item in s) if s else False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sublist([2,4,3,5,7], [3,7]), False)

if __name__ == '__main__':
    unittest.main()