'''给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2**31,  2**31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend>0) ^ (divisor>0)
        dividend,divisor = abs(dividend),abs(divisor)
        cnt,result = 0,0 
        while dividend >= divisor:
            cnt +=1
            divisor <<= 1
        while cnt>0:
            cnt -= 1
            divisor >>= 1
            if dividend >= divisor:
                result += (1 << cnt)
                dividend -= divisor
        if sign == True: result = -result
        if result > 2**31-1: result = 2**31 -1
        if result < -2**31: result = -2**31
        return result

if __name__ == "__main__":
    while(True):
        solution =Solution()
        inputs_1 = int(input('inputs1:'))
        inputs_2 = int(input('inputs2:'))
        print(solution.divide(dividend= inputs_1,divisor=inputs_2))
