def combinations_list(list1):
   '''Write a function to find all possible combinations of the elements of a given list.'''
   if not list1:
       return [[]]
   result = []
   for i in range(1 << len(list1)):
       temp = []
       for j in range(len(list1)):
           if i & (1 << j):
               temp.append(list1[j])
       result.append(temp)
   return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_list(['orange', 'red', 'green', 'blue']), [[], ['orange'], ['red'], ['orange', 'red'], ['green'], ['orange', 'green'], ['red', 'green'], ['orange', 'red', 'green'], ['blue'], ['orange', 'blue'], ['red', 'blue'], ['orange', 'red', 'blue'], ['green', 'blue'], ['orange', 'green', 'blue'], ['red', 'green', 'blue'], ['orange', 'red', 'green', 'blue']])

if __name__ == '__main__':
    unittest.main()