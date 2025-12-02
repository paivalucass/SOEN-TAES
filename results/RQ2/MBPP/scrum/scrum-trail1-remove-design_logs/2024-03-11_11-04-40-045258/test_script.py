def remove_parenthesis(items):
    result = []
    for item in items:
        index = item.find('(')
        if index != -1:
            result.append(item[:index].strip())
        else:
            result.append(item)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_parenthesis(["python (chrome)"]), "python")

if __name__ == '__main__':
    unittest.main()