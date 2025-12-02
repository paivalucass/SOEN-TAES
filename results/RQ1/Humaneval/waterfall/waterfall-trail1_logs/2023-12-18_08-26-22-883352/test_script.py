def select_words(s, n):
    result = []
    if not s or not isinstance(n, int) or n <= 0:
        return result
    
    vowels = "aeiouAEIOU"
    words = s.split()
    
    import re
    for word in words:
        consonant_count = len(re.findall(r'[^aeiouAEIOU]', word))
        if consonant_count == n:
            result.append(word)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
    
    def test2(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test3(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test4(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test5(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()