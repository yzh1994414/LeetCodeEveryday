'''题目描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。

输出描述:
输出该数值的十进制字符串。

示例1
输入
复制
0xA
输出
复制
10'''

while True:
    try:
        inputs=input().strip()
        num_dict_16={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        res = 0
        for i in range(2,len(inputs)):
            if num_dict_16.get(inputs[i]) is None:
                res = res*16 + int(inputs[i])
            else:
                res = res*16 + num_dict_16[inputs[i]]
        print(res)
    except:
        break
'''
inputs=input().strip()
print(int(inputs,16))
'''