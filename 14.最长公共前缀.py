'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''["flower","flow","flight"],["aaa","aa","aaa"],["abcc","abcc","abcb"],['aa','ab']
'''
        res = ''
        if len(strs)==0:
            return res
        tmp_res = strs[0]
        for i in range(0,len(strs)):
            tmp_str = strs[i]
            length = len(tmp_res) if len(tmp_res)<len(tmp_str) else len(tmp_str)
            if tmp_res[:length] == tmp_str[:length]:
                tmp_res = tmp_res[:length]
                res = tmp_res
                continue
            else :
                left,mid,right = 0 , (length)//2, length
                res = ''
                while left <= right:
                    if tmp_res[:mid] == tmp_str[:mid]:
                        res = tmp_str[:mid]
                        left =mid+1
                        mid = (left+right)//2
                    else :
                        right = mid-1
                        mid = (left+right)//2
                if res == '':
                    break
                tmp_res = res
        return res



                        


