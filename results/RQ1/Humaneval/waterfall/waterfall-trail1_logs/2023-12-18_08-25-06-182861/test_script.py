def exchange(lst1, lst2):
    if not lst1 or not lst2:
        return 'Invalid input: lists cannot be empty'

    lst1_even = all(num % 2 == 0 for num in lst1)
    lst2_even = all(num % 2 == 0 for num in lst2)

    if lst1_even:
        return 'YES'
    elif lst2_even:
        return 'YES'
    else:
        return 'NO'
import unittest

class Test(unittest.TestCase):
    def test_exchange(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()