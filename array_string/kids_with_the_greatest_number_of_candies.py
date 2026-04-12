#Pegar a lista de doces de cada criança e verificar qual é o valor maximo. 
#Para cada item da lista somar o doces extras e verificar se aquela quantidade se tornaria o máximo.
#Retornar uma lista de bool com o teste de cada item da lista

def kids_with_candies(candies, extra_candies):
    can_be_max = []
    max_candies = max(candies)
    
    for n in candies:
        can_be_max.append(n + extra_candies >= max_candies)   

    return can_be_max

#print(kids_with_candies([2,3,5,1,3], 3))



import unittest


class KidsWithTheGreatestNumberOfCandies(unittest.TestCase):
      def test_one(self):
        input = kids_with_candies([2,3,5,1,3], 3)
        output = [True,True,True,False,True]
        self.assertEqual(input, output)

      def test_two(self):
        input = kids_with_candies([4,2,1,1,2], 1)
        output = [True,False,False,False,False]  
        self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()    
