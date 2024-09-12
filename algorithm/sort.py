class SelectionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError
        if data == []:
            return data

        #使用浅拷贝生成一个新的副本，不直接修改原数组避免后面测试代码的断言执行失败
        temp_data = data[:]
        new_data = []
        while temp_data:
            #新建一个变量来存储每次循环时数组的最小值，减少min()函数调用次数，提升性能
            min_val = min(temp_data)
            new_data.append(min_val)
            temp_data.remove(min_val)

        return new_data

sort = SelectionSort().sort
data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
print(sort(data) == sorted(data))  # True
