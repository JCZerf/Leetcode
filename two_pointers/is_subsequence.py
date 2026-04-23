
import unittest


def is_subsequence(string_s, string_t):
    pos = 0
    if not string_s:
        return True
    for char in string_t:
        if char == string_s[pos]:
            pos += 1
            if pos == len(string_s):
                return True
    return False        

class IsSubsequence(unittest.TestCase):
    def  test_one(self):
        resultado = is_subsequence("abc", "ahbgdc")
        esperado = True
        self.assertEqual(resultado, esperado)
    def  test_two(self):
        resultado = is_subsequence("axc", "ahbgdc")
        esperado = False
        self.assertEqual(resultado, esperado)    

if __name__ == '__main__':
    unittest.main()