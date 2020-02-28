'''题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格

详细描述：


函数接口说明：

public String getResult(long ulDataInput)

输入参数：

long ulDataInput：输入的正整数

返回值：

String



输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
复制
180
输出
复制
2 2 3 3 5'''

inputs = int(input())
def getResult(ulDataInput):
    zhi = 1
    for i in range(2,int(ulDataInput**0.5+2)):
        if ulDataInput%i==0:
            zhi = 0
            print(str(i),end=" ")
            getResult(int(ulDataInput/i))
            break
    if zhi ==1: print(str(ulDataInput),end=" ")

getResult(inputs)
    