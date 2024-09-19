class CompressString(object):

    def compress(self, string):

        ### 完善代码 ###
        if string is None or string == '':
            return string

        count = 1
        compressed = []
        #遍历字符串
        for i in range(1,len(string)):
            if string[i] == string[i-1]:
                count +=1
            else:
                #把当前字符和计数记录进压缩结果中
                compressed.append(string[i-1])
                if count > 1:
                    compressed.append(str(count))
                count = 1

        #处理最后一个字符
        compressed.append(string[-1])
        if count > 1:
            compressed.append(str(count))

        #拼接压缩后的字符串
        compressed_str=''.join(compressed)

        return compressed_str if len(compressed_str)<len(string) else string
