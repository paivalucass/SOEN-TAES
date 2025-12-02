def find_Rotations(input_string): 
    if not input_string:
        return "Invalid input"
    length = len(input_string)
    for i in range(1, length + 1):
        if input_string[:i] * (length // i) + input_string[:length % i] == input_string:
            return i
    return length

assert find_Rotations("aaaa") == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()