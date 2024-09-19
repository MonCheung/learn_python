class Solution(object):

    def two_sum(self, nums, val):

        ### 补充代码 ###
        if nums is None or val is None:
            raise TypeError
        if nums == []:
            raise ValueError
        #创建一个字典存储已访问过的元素和索引
        seen = {}

        for i, num in enumerate(nums):
            complement = val - num

            #检查这个值是否已在字典中
            if complement in seen:
                return [seen[complement],i]
            else:
                seen[num] = i

        return None


solution = Solution()
target = 7
nums = [1, 3, 2, -7, 5]
expected = [2, 4]
print(solution.two_sum(nums, target))
print('Success: test_two_sum')
