class Solution(object):

    def fizz_buzz(self, num):
        #异常判断
        if num is None:
            raise TypeError
        elif num < 1:
            raise ValueError

        #把输入参数列表化，以及创建一个新列表接收遍历后的值
        num_list1 = list(range(1,num+1))
        num_list2 = []
        for i in num_list1:
            if i % 3 ==0 and i % 5 == 0:
                num_list2.append('FizzBuzz')
            elif i % 3 == 0:
                num_list2.append('Fizz')
            elif i % 5 == 0:
                num_list2.append('Buzz')
            else:
                num_list2.append(str(i))
        return num_list2
