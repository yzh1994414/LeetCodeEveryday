'''一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0': return 0
        if len(s)<=1 : return 1
        dp = len(s)*[1]
        if s[1]!='0':
            dp[1]=1
            if int(s[:2])<=26 and int(s[:2])>9:
                dp[1]+=1
        else:
            if int(s[:2])<=26 and int(s[:2])>9:
                dp[1]=1
            else: dp[1]=0
        for i in range(2,len(s)):
            if s[i] != '0':
                dp[i] = dp[i-1]
                if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>9:
                    dp[i]+=dp[i-2]
            else:
                if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>9:
                    dp[i]=dp[i-2]
                else: dp[i]=0
        return dp[len(s)-1]


if __name__ == "__main__":
    Solution =Solution()
    inputs = '12120'
    Solution.numDecodings(inputs)



# 226 
# 2 2 6
# 22 6
# 2 26
