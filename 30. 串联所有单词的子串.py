'''给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if words == [] : return []  
        length_one = len(words[0])
        length_total = length_one * len(words)
        s_len = len(s)
        words = Counter(words)
        res = []
        for i in range(s_len - length_total + 1):
            tmp_s = s[i:i+length_total]
            tmp_words = []
            for j in range(0,len(tmp_s) , length_one):
                tmp_word = tmp_s[j:j+length_one] 
                if tmp_word not in words:
                    break
                tmp_words.append(tmp_word)
            if Counter(tmp_words) == words:
                res.append(i)
        return res



if __name__ == "__main__":
  while True:
    s = input('Input string:')
    words = input('Input words :').split(',')
    if s =='quit':
      break
    solution = Solution()
    solution.findSubstring(words=words,s=s)





