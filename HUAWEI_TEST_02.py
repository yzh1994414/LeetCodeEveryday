'''
题目描述
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

输入描述:
第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述:
输出输入字符串中含有该字符的个数。

示例1
输入
复制
ABCDEF
A
输出
复制
1
'''
String = input()
String=String.lower()
print(String)
c = input()
c_dict={}
for s in String:
    if c_dict.get(s) is None:
        c_dict[s]=1
    else:
        c_dict[s]+=1
if c_dict.get(c) is None:
    c_dict[c]=0
print(c_dict[c])