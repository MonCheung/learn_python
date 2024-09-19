class ReverseString(object):

    def reverse(self, chars):

        ### 完善代码 ###
        if chars is None or chars == []:
            return chars
        else:
            left = 0
            right = len(chars)-1
            #双指针原地反转
            while left < right:
                chars[left],chars[right] = chars[right],chars[left]
                left +=1
                right -=1
            return chars

reverse = ReverseString().reverse
target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
print(reverse(target_list) == target_list)
