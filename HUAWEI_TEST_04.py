'''
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组

示例1
输入
复制
abc
123456789
输出
复制
abc00000
12345678
90000000
'''

while True:
    try:
        string = input()
        length = len(string)
        divisor_8 = length//8
        remainder_8 = length%8
        for i in range(divisor_8):
            print(string[i*8:(i+1)*8])
        differ_remainder_8 = 8-remainder_8
        if remainder_8!=0: print(string[divisor_8*8:]+'0'*differ_remainder_8)
    except:
        break