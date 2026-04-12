import math
import unittest


def divisor_of_string(str1, str2):
    if str1 + str2 == str2 + str1:
        mdc = math.gcd(len(str1), len(str2))
        return str1[:mdc]
    return ''         


class GreatestCommonDivisor(unittest.TestCase):
    def test_one(self):
        resultado = divisor_of_string('ABCABC', 'ABC')
        esperado = 'ABC'
        self.assertEqual(resultado, esperado)
    def test_two(self):
        resultado = divisor_of_string('ABABAB', 'ABAB')
        esperado = 'AB'
        self.assertEqual(resultado, esperado)
    def test_tree(self):
        resultado = divisor_of_string('LEET', 'CODE')
        esperado = ''
        self.assertEqual(resultado, esperado)
    def test_four(self):
        resultado = divisor_of_string('AAAAAB', 'AAA')
        esperado = ''
        self.assertEqual(resultado, esperado) 
        
    def test_five_letras_repetidas(self):
        resultado = divisor_of_string('AABAAB', 'AAB')
        esperado = 'AAB'
        self.assertEqual(resultado, esperado)

    def test_six_tamanhos_que_nao_fecham(self):
        resultado = divisor_of_string('ABA', 'AB')
        esperado = ''
        self.assertEqual(resultado, esperado)       

if __name__ == '__main__':
    unittest.main()