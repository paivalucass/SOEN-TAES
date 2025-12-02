def len_log(list1):
    if not list1:
        raise ValueError("Input list should not be empty")
    
    for element in list1:
        if not isinstance(element, str):
            raise ValueError("Input list should only contain strings")

    valid_words = [word for word in list1 if word.isalpha()]
    if not valid_words:
        raise ValueError("Input list should contain at least one valid word")
    
    max_length = max(len(word) for word in valid_words)
    return max_length

# Test cases
try:
    len_log([])
except ValueError:
    print("ValueError handled correctly for empty input list")

try:
    len_log(['apple', 5, 'banana'])
except ValueError:
    print("ValueError handled correctly for non-string elements in the input list")

assert len_log(['apple', 'pear', 'kiwi', 'mango']) == 5

assert len_log(['apple', 'pear', 'kiwi', 'mango', 'grape']) == 5

# Additional test cases
assert len_log(['python', 'PHP', 'bigdata']) == 7
assert len_log(['apple']) == 5
assert len_log(['apple', 'banana', 'orange']) == 6
assert len_log(['apple', '12345', '@#%$^&']) == 5
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python", "PHP", "bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()