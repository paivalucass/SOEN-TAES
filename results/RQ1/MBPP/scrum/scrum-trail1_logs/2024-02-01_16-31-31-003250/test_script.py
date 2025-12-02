def remove_parenthesis(items):
  modified_items = []
  for item in items:
    if '(' in item and ')' in item:
      start_index = item.index('(')
      end_index = item.index(')')
      modified_item = item[:start_index] + item[end_index+1:]
      modified_items.append(modified_item)
    else:
      modified_items.append(item)
  return modified_items
import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis(["python (chrome)"]), "python")

if __name__ == '__main__':
    unittest.main()