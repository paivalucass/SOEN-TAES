def remove_parenthesis(items):
    result = []

    for string in items:
        modified_string = ""
        inside_parenthesis = False

        for char in string:
            if char == "(":
                inside_parenthesis = True
            elif char == ")":
                inside_parenthesis = False
            elif not inside_parenthesis:
                modified_string += char

        result.append(modified_string.strip())

    return result
import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis(["python (chrome)"]), ["python"])

if __name__ == '__main__':
    unittest.main()