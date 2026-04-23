import unittest


def findMaxAverage(nums, k):
    soma_atual = sum(nums[:k])
    maior_soma = soma_atual
    for i in range(k, len(nums)):
        soma_atual = soma_atual - nums[i - k] + nums[i] 
        maior_soma = max(maior_soma, soma_atual)
    return maior_soma / k
print(findMaxAverage([1,12,-5,-6,50,3], 4))    


class Maximum_average_subarray(unittest.TestCase):
    def test_one(self):
        input = findMaxAverage([1,12,-5,-6,50,3], 4)
        output = 12.75000
        self.assertEqual(input, output)

    def test_two(self):
        input = findMaxAverage([5], 1)
        output = 5.00000
        self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()        
        
