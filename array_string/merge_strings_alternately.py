#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.

#Primeiro eu pego a string que tem o maior tamanho para poder concaternar todas as letras
#Eu percorro letra a letra atribuindo o valor a uma váriavel
#Quando a próxima letra não existir eu não tento adicionar
#retorno o resultado da concatenação alternada

def alternate_string(word1, word2):
    result = []
    max_len = max(len(word1), len(word2))
    contador = 0
    while  max_len > contador:
        if contador < len(word1):
            result.append(word1[contador])
        if contador < len(word2):
            result.append(word2[contador])    
        contador += 1
    return ''.join(result)    

word1 = 'abcd'
word2 = 'pq'
print(alternate_string(word1, word2))    


