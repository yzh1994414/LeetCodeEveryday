'''给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack_val,stack_ind = [],[]
        res_list = [0]* len(s)
        for i in range(0, len(s)):
            if s[i] == '(': 
                stack_val.append('(')
                stack_ind.append(i)
            else:
                if len(stack_val) == 0: continue
                tmp_val = stack_val.pop()
                tmp_ind = stack_ind.pop()
                if tmp_val == s[i]: stack_val,stack_ind = [],[]
                else : 
                    res_list[tmp_ind] = 1
                    res_list[i] = 1
        tmp_res, result = 0, 0
        for i in range(0, len(res_list)):
            if res_list[i] == 0: 
                if tmp_res > result : result = tmp_res
                tmp_res = 0
            else: tmp_res += 1
        if tmp_res > result : result = tmp_res
        return result

if __name__ == "__main__":
    while True:
        s = input('input:')
        if s =='quit':break
        solution = Solution()
        solution.longestValidParentheses(s=s)