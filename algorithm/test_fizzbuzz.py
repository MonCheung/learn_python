import unittest
from fizzbuzz import Solution

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        solution = Solution()
        #检查异常抛出
        self.assertRaises(TypeError,solution.fizz_buzz,None)
        self.assertRaises(ValueError,solution.fizz_buzz,0)

        expected = ['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz','11','Fizz','13','14','FizzBuzz']

        #检查正常数值的执行结果
        self.assertEqual(solution.fizz_buzz(15),expected)
        print('Success: test_fizz_buzz')

if __name__ == '__main__':
    unittest.main()
