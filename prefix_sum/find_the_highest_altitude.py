import unittest


def largestAltitude(gain):
    my_gain = 0
    max_gain = my_gain
    for n in gain:
        my_gain += n
        if my_gain > max_gain:
            max_gain = my_gain
    return max_gain


class find_the_hidhest_altitude(unittest.TestCase):
      def test_one(self):
          input = largestAltitude([-5,1,5,0,-7])
          output = 1
          self.assertEqual(input, output)

      def test_two(self):
          input = largestAltitude([-4,-3,-2,-1,4,3,2])
          output = 0
          self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()          