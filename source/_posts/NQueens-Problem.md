---
title: NQueens Problem
date: 2023-07-20 15:05:51
tags:
---
# NQueens问题

著名的N皇后问题，N皇后问题是一个经典的问题，在一个N*N的棋盘上放置N个皇后，每行一个并使其不能互相攻击（同一行、同一列、同一斜线上的皇后都会自动攻击
通过之前的文章中提到的DFS可以解决。
其实没有啥好的办法，就是回溯（backtracking）。时间复杂的为： Big O of N！， N的阶乘，非常耗时，几乎是最差的了。
看一下伪代码：

1) Start in the leftmost column --最左边的列开始
2) If all queens are placed -- 退出条件，n个皇后都摆好了
    return true
3) Try all rows in the current column. -- 试每一个行
   Do following for every tried row.
    a) If the queen can be placed safely in this row --回溯算法，先用上当前
       then mark this [row, column] as part of the
       solution and recursively check if placing
       queen here leads to a solution.
    b) If placing the queen in [row, column] leads to  -- 递归调用，试下一列
       a solution then return true.
    c) If placing queen doesn't lead to a solution then -- 回溯算法， 用完恢复
       unmark this [row, column] (Backtrack) and go to
       step (a) to try other rows.
3) If all rows have been tried and nothing worked, -- 找不到返回false
   return false to trigger backtracking.
 比较难写的部分其实在于区check当前状态是否有效。可以有点儿小技巧。 不bb了， let code do the talking。

```
public boolean isValid(char[][] chessboard, int x, int y) {

    int rowLen = chessboard.length;
    int colLen = chessboard[0].length;
    // check single column, 检查列
    for (int i = 0; i < chessboard.length; i++) { 
        if (chessboard[i][y] == 'Q') { 
            return false; 
        } 
    } // no need to check single row，没必要检查行，因为遍历的时候就已经天然的一行放一个了。 
    // check 45 diagonal，重点来了 45度检查，巧妙，i-j 为定值。 
    for (int i = x, j = y; i >= 0 && j >= 0; i--, j--) {
        if (chessboard[i][j] == 'Q') {
            return false;
        }
    }
    for (int i = x, j = y; i < rowLen && j < colLen; i++, j++) {
        if (chessboard[i][j] == 'Q') {
            return false;
        }
    }
    // check 135 diagonal， 135度的检查， i+j 为定值。
    for (int i = x, j = y; i < rowLen && j >= 0; i++, j--) {
        if (chessboard[i][j] == 'Q') {
            return false;
        }
    }
    for (int i = x, j = y; i >= 0 && j < colLen; i--, j++) {
        if (chessboard[i][j] == 'Q') {
            return false;
        }
    }

    return true;
}
```
