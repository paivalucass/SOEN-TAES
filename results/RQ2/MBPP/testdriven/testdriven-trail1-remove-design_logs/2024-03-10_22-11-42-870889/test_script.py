def empty_list(length):
    '''
    Write a function to create a list of N empty dictionaries.
    assert empty_list(5)==[{},{},{},{},{}]
    '''
    if length <= 0:
        return "Error handling for non-positive integer inputs"
    elif length == 1:
        return [{}]
    else:
        return [{} for _ in range(length)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()