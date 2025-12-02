def exchange(lst1, lst2):
    lst1.sort()
    lst2.sort()
    
    total_sum = sum(lst1) + sum(lst2)

    if total_sum % 2 == 0:
        return "YES"
    else:
        return "NO"
import unittest

class Test(unittest.TestCase):
    def test_exchange(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()