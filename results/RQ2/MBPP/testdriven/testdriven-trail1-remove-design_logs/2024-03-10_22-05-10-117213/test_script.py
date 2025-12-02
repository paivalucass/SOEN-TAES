def start_with_p(words):
    '''Write a function to return two words from a list of words starting with letter 'p'.
    assert start_with_p(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')'''
    
    result = []
    for word in words:
        word_list = word.split()
        for w in word_list:
            if w.lower().startswith('p'):
                result.append(w)
    
    return tuple(result[:2]) if len(result) >= 2 else tuple(result) if len(result) >= 1 else ()
import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()