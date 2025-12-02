def word_len(s):
    """
    This function checks if the length of the input word is odd.
    
    Args:
    s : str - Input word
    
    Returns:
    bool - True if length is odd, False if length is even
    """
    if len(s) % 2 == 0:
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(word_len('Hadoop'), False)

if __name__ == '__main__':
    unittest.main()