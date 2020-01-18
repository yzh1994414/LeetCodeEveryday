'''编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# class Solution:
#     def solveSudoku(self, board: [[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         #按行的set list
#         rows_arr = [set(arr) for arr in board]
#         #按列的set list
#         columns_arr = [set([arr[i] for arr in board]) for i in range(len(board[0]))]
#         #按区域编号的set list
#         area_arr = [set([board[i][j] for j in range(3) for i in range(3)]),set([board[i][j] for j in range(3,6) for i in range(3)]),set([board[i][j] for j in range(6,9) for i in range(3)]),\
#         set([board[i][j] for j in range(3) for i in range(3,6)]),set([board[i][j] for j in range(3,6) for i in range(3,6)]),set([board[i][j] for j in range(6,9) for i in range(3,6)]),\
#         set([board[i][j] for j in range(3) for i in range(6,9)]),set([board[i][j] for j in range(3,6) for i in range(6,9)]),set([board[i][j] for j in range(6,9) for i in range(6,9)])]
#         #二维数组用于记录区域编号
#         board_area_index = [[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],
#                             [3,3,3,4,4,4,5,5,5],[3,3,3,4,4,4,5,5,5],[3,3,3,4,4,4,5,5,5],
#                             [6,6,6,7,7,7,8,8,8],[6,6,6,7,7,7,8,8,8],[6,6,6,7,7,7,8,8,8]]
#         #数字【1-9】set，用于返回两个集合中不重复的元素集合。
#         all_num_set = {'1','2','3','4','5','6','7','8','9','.'}
#         #用于求解数独面板，记录set交集个数
#         record_cnt_matrix = 9*[9*[0]]
#         #需要填充的个数
#         fill_cnt = 0
#         #每个位置的sudo set
#         board_sudoset_matrix = []
#         for i in range(9):
#             tmp_sudoset_arr = []
#             for j in range(9):
#                 if board[i][j] == '.':
#                     fill_cnt+=1
#                     area_index = board_area_index[i][j]
#                     sudoku_set = rows_arr[i].union(columns_arr[j]).union(area_arr[area_index]).symmetric_difference(all_num_set)
#                     tmp_sudoset_arr.append(sudoku_set)
#                     record_cnt_matrix[i][j] = len(sudoku_set)
#                 else:
#                     tmp_sudoset_arr.append(set())
#             board_sudoset_matrix.append(tmp_sudoset_arr)
#         while fill_cnt>0:
#             for i in range(9):
#                 for j in range(9):
#                     arr = board_sudoset_matrix[i][j]
#                     if len(arr) == 1:
#                         area_ind = board_area_index[i][j]
#                         num = arr.pop()
#                         fill_cnt-=1
#                         for k in range(9): 
#                             if num in board_sudoset_matrix[k][j]:
#                                 board_sudoset_matrix[k][j].remove(num)
#                         for k in range(9): 
#                             if num in board_sudoset_matrix[i][k]:
#                                 board_sudoset_matrix[i][k].remove(num)
#                         for p in range(9):
#                             for q in range(9):
#                                 if (board_area_index[p][q] == area_ind) and (num in board_sudoset_matrix[p][q]):
#                                     board_sudoset_matrix[p][q].remove(num)
#                         board[i][j] = num
#                         break
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3)*3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3)*3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()


if __name__ == "__main__":
    # inputs = [["5","3",".",".","7",".",".",".","."],
    #          ["6",".",".","1","9","5",".",".","."],
    #          [".","9","8",".",".",".",".","6","."],
    #          ["8",".",".",".","6",".",".",".","3"],
    #          ["4",".",".","8",".","3",".",".","1"],
    #          ["7",".",".",".","2",".",".",".","6"],
    #          [".","6",".",".",".",".","2","8","."],
    #          [".",".",".","4","1","9",".",".","5"],
    #          [".",".",".",".","8",".",".","7","9"]]
    inputs = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    solution = Solution()
    solution.solveSudoku(inputs)                                            



                    
