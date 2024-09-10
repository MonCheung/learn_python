def vowel_count(string):
    vowel_list=['a','e','i','o','u']
    vowel_num = 0

    for char in string.lower():
        if char in vowel_list:
            vowel_num +=1

    return vowel_num
    # 此处写你的代码

# 获取输入字符串
input_string = 'AOU'
# 调用函数
print(vowel_count(input_string))
