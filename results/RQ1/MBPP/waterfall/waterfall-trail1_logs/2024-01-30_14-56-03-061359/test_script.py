def remove_parenthesis(items):
    result = []
    for item in items:
        new_item = ''
        inside_paren = False
        for char in item:
            if char == '(': 
                inside_paren = True
            elif char == ')': 
                inside_paren = False
            elif not inside_paren:
                new_item += char
        result.append(new_item.strip())
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_parenthesis(["python (chrome)"]), "python")

if __name__ == '__main__':
    unittest.main()