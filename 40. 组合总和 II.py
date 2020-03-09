

'''给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    res = []
    def dfs(self, ind:int ,paths:[int] ,tmp_cnt : int,candidates:[int] ,target:int):
        if tmp_cnt == target: 
            res_paths = list(paths)
            self.res.append(res_paths)
            return True
        if tmp_cnt >target: return True
        for i in range(ind,len(candidates)):
            if (i > ind)&(candidates[i]==candidates[i-1]): continue
            paths.append(candidates[i])
            flag = self.dfs(i+1,paths,tmp_cnt+candidates[i],candidates,target)
            paths.pop()
            if flag == True : break
        return False

    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        self.res=[]
        path = []
        self.dfs(0,path,0,candidates,target)
        return self.res


if __name__ == "__main__":
    solution = Solution()
    solution.combinationSum2([10,1,2,7,6,1,5],8)