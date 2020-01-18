'''「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 : return '1'
        if n == 2 : return '11'
        numbers = '11'
        for i in range(3,n+1):
            cnt = 1 
            tmp_numbers = ''
            for j in range(len(numbers)-1):
                if numbers[j] == numbers[j+1]: cnt+=1
                else : 
                    tmp_numbers = tmp_numbers + str(cnt)+numbers[j]
                    cnt=1
            if numbers[len(numbers)-1] != numbers[len(numbers)-2]:
                tmp_numbers = tmp_numbers + '1'+numbers[len(numbers)-1]
            else : tmp_numbers = tmp_numbers + str(cnt) +numbers[len(numbers)-1]
            numbers = tmp_numbers
        return numbers

if __name__ == "__main__":
    solution = Solution()
    solution.countAndSay(6)