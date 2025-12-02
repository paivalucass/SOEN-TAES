def string_sequence(n: int) -> str:
    if not isinstance(n, int):
        return "Invalid input"
    if n < 0:
        return "Invalid input"
    
    result = "0"
    for i in range(1, n+1):
        result += " " + str(i)
    return result
import unittest

class Test(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()