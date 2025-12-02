def remove_parenthesis(items):
    '''Write a function to remove the parenthesis and what is in between them from a string.'''
    result = []
    for item in items:
        if '(' in item:
            result.append(item[:item.find('(')].strip())
        else:
            result.append(item)
    return result
import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis("python (chrome)"), "python")

if __name__ == '__main__':
    unittest.main()