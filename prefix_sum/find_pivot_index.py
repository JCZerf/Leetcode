import unittest


def pivotIndex(nums):
    max_sum = sum(nums)
    left_sum = 0
    for i, n in enumerate(nums):
        if left_sum == max_sum - left_sum - nums[i]:
            return i
        left_sum += n
    return -1

print(pivotIndex([1,7,3,6,5,6]))

class find_pivot_index(unittest.TestCase):
      def test_one(self):
          input = pivotIndex([1,7,3,6,5,6])
          output = 3
          self.assertEqual(input, output)

      def test_two(self):
          input = pivotIndex([1,2,3])
          output = -1
          self.assertEqual(input, output)

      def test_three(self):
          input = pivotIndex([2,1,-1])
          output = 0
          self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()   