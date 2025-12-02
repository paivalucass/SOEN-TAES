def anti_shuffle(s):
    if not isinstance(s, str) or not s:
        return "Invalid input"
    
    words = s.split(" ")
    ordered_words = ["".join(sorted(word)) for word in words]
    ordered_string = " ".join(ordered_words)
    return ordered_string
import unittest

class Test(unittest.TestCase):
    def test_anti_shuffle(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()