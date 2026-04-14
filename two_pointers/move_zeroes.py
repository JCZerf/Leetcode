import unittest

def moveZeroes(nums):
  pos = 0
  for i in range(len(nums)):
      if nums[i] != 0:
          nums[pos] = nums[i]   
          pos += 1  
  for i in range(pos, len(nums)):
      nums[i] = 0
  return nums


class Move_zeroes(unittest.TestCase):
    def  test_one(self):
        resultado = moveZeroes([0,1,0,3,12])
        esperado = [1,3,12,0,0]
        self.assertEqual(resultado, esperado)
    def  test_two(self):
        resultado = moveZeroes([0])
        esperado = [0]
        self.assertEqual(resultado, esperado)    

if __name__ == '__main__':
    unittest.main()
