## Data Structure and Algorithm 6 | P-NP and Backtracking

![0_QXrDY4nVmhZ1umbX](../../image/0_QXrDY4nVmhZ1umbX.jpeg)

#### 1. P-NP Problem

**(1) Longest Increasing Subsequence**

Leetcode: [300](https://leetcode.com/problems/longest-increasing-subsequence/).

Pseudocode: DP, Time complexity $O(n^2)$.

```
L[i] = 1 + max{ L[j]: for all nums[j] < nums[i] and j < i }
```

Python code,

```python
L = [1] * len(nums)

for i in range(len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            L[i] = max(L[i], L[j] + 1)

return max(L)
```

**(2) Polynomal Time**

An algorithm runs in polynomial time if its runtime is some polynomial in $n$, which can be written as $O(n^k)$.

**(3) Cobham-Edmonds Thesis**

A language $L$ can be decided efficiently if and only if it can be decided in time $O(n^k)$ for some $k \in \mathbb{N}$.

For example,
$$
n^{100000000000000}
$$
can be decided efficiently but,
$$
1.0000000000001^n
$$
can not be decided efficiently.

**(4) Complexity Class P**

The complexity class $P$ is a class that contains all the problems that can be solved in polynomial time,
$$
P = \{L\ |\text{ There is a polynomial-time decider (TM) for } L\}
$$
Where $TM$ stands for Turing Machine.

Common P problems are,

* graph connectivity
* primality testing
* maximum matching
* remoteness testing
* linear programming
* string transform distance
* Etc.

**(5) Non-deterministic Turing machine**

A nondeterministic Turing machine (NTM) is a theoretical model of computation whose governing rules specify more than one possible action when in some given situations. For example, BST is an NTM because its time complexity is the height of the tree.

**(6) NTM to TM Theorem**

For any NTM with time complexity $f(n)$, there is a TM with time complexity $2^{O(f(n))}$.

**(7) Complexity Class NP**

The complexity class NP (nondeterministic polynomial time) contains all problems that can be solved in polynomial time by an NTM.
$$
NP = \{L\ |\text{ There is a NTM that decides }\ L \text{ in non-deterministic polynomial time.}\}
$$
Common NP problems are,

* Solve sudoku
* Knapsack probelm
* Travelling salesman
* Graph coloring

From the definition, we can easily know that,
$$
P \subseteq NP
$$
But it is still the most important question in theorical computer science that if
$$
P = NP
$$
It can be explained simply as if a solution to a problem can be checked efficiently, can that problem be solved efficiently?

#### 2. Backtracking

**(1) Definition**

Backtracking is a general algorithm for finding the solutions to some computational problems. It abandons a candidate (called backtrack) as soon as it determinates the candidate can not possibily be completed to a valid solution. Backtracking is commonly used to solve some NP-complete questions.

**(2) Template** 

```python
def backtrack(case):

  	if find_solution(case):
    		return
        
    for next_case in cases:
      
      	if not is_valid(next_case):
          	continue
        
        set_next()
    		backtrack(next_case)
        reset_last()
```

**(3) Crosswords I**

Find a specific word in a matrix.

Leetcode [79](https://leetcode.com/problems/word-search/).

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        
        for i in range(self.m):
            for j in range(self.n):
                if self.backtrack(i, j, word):
                    return True

        return False
    
    def backtrack(self, row, col, suffix):
        
        if len(suffix) == 0:
            return True
        
        if row < 0 or row == self.m or col < 0 or col == self.n:
            return False
        
        if self.board[row][col] != suffix[0]:
            return False
        
        self.board[row][col] = '#'
        
        for roffset, coffset in [(0,1), (1,0), (0,-1), (-1,0)]:
            if self.backtrack(row+roffset, col+coffset, suffix[1:]):
                self.board[row][col] = suffix[0]
                return True
            
        self.board[row][col] = suffix[0]
        return False
```

**(4) Crosswords II**

Clean a room by robot.

Leetcode [489](https://leetcode.com/problems/robot-room-cleaner/).

```python
def cleanRoom(self, robot):
    """
    :type robot: Robot
    :rtype: None
    """
    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(cell=(0, 0), direction=0):
        visited.add(cell)
        robot.clean()

        for i in range(4):
            new_direction_index = (direction + i) % 4
            next_direction = directions[new_direction_index]
            next_cell = (cell[0] + next_direction[0], cell[1] + next_direction[1])

            if not next_cell in visited and robot.move():
                backtrack(next_cell, new_direction_index)
                go_back()

            robot.turnRight()

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    backtrack()
```

**(5) N-Queens I**

Leetcode [51](https://leetcode.com/problems/n-queens/).

**Trick 1**: how to get the diagonal/anti-diagonal index for a cell in an $n \times n$ matrix.

For an $n \times n$ matrix, there will be $2n - 1$ diagonals or anti-diagonals. So the index of a diagonal can be calculated by,

```
diagonal_in = row_in - col_in
```

And the index of an anti-diagonal can be calculated by,

```
antidiagonal_in = row_in + col_in
```

**Trick 2**: Before we put a queen, we have to check three sets.

- if its column has another queen?
- if its diagonal has another queen?
- if its anti-diagonal has another queen?

We don't need to check the rows because we will only put one queen in each row.

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(row, diagonals, antidiagonals, cols, state):
            
            if row == n:
                ans.append(["".join(row) for row in state])
                return

            for col in range(n):
                diagonal = row - col
                antidiagonal = row + col
                
                if col in cols:
                    continue
                    
                if diagonal in diagonals:
                    continue
                    
                if antidiagonal in antidiagonals:
                    continue
                    
                state[row][col] = "Q"
                cols.add(col)
                diagonals.add(diagonal)
                antidiagonals.add(antidiagonal)
                
                backtrack(row+1, diagonals, antidiagonals, cols, state)
                
                state[row][col] = "."
                cols.remove(col)
                diagonals.remove(diagonal)
                antidiagonals.remove(antidiagonal)
                
        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans
```

**(6) N-Queens II**

This is just a similar question without requirement for printing the board.

Leetcode [52](https://leetcode.com/problems/n-queens-ii/).

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.ans = 0
        
        def backtrack(row, diagonals, antidiagonals, cols):
            
            if row == n:
                self.ans += 1
                return
                
            for col in range(n):
                
                diagonal = row - col
                antidiagonal = row + col
                
                if col in cols:
                    continue
                if diagonal in diagonals:
                    continue
                if antidiagonal in antidiagonals:
                    continue
                    
                cols.add(col)
                diagonals.add(diagonal)
                antidiagonals.add(antidiagonal)
                
                backtrack(row+1, diagonals, antidiagonals, cols)
                
                cols.remove(col)
                diagonals.remove(diagonal)
                antidiagonals.remove(antidiagonal)
            
        backtrack(0, set(), set(), set())
        return self.ans
```

**(6) Valid Sudoku**

Before we see how to solve a Sudoku, let's first see how we can validate one. This is not a backtracking problem.

Leetcode [36](https://leetcode.com/problems/valid-sudoku/).

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        self.board = board
        self.rows = [set() for _ in range(m)]
        self.cols = [set() for _ in range(m)]
        self.boxs = [set() for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == ".":
                    continue
                
                if not self.isValidCell(row, col):
                    return False
        
        return True
        
    def isValidCell(self, row, col):
        
        val = self.board[row][col]
        box = (row // 3) * 3 + col // 3
        
        if val in self.rows[row]:
            return False
        
        if val in self.cols[col]:
            return False
        
        if val in self.boxs[box]:
            return False
        
        self.rows[row].add(val)
        self.cols[col].add(val)
        self.boxs[box].add(val)
        return True
```

**(7) Solve Sudoku**

Next, let's solve a Sudoku.

Leetcode: [37](https://leetcode.com/problems/sudoku-solver/).

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.sudoku_solved = False
        
        def place_number(d, row, col):
            
            if d not in rows[row]:
                rows[row][d] = 1
            else:
                rows[row][d] += 1
                
            if d not in cols[col]:
                cols[col][d] = 1
            else:
                cols[col][d] += 1
                
            if d not in boxs[box_index(row, col)]:
                boxs[box_index(row, col)][d] = 1
            else:
                boxs[box_index(row, col)][d] += 1
                
            board[row][col] = str(d)
            
        def place_next_numbers(row, col):
            if col == N - 1 and row == N - 1:
                self.sudoku_solved = True  
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)
                
                
        def backtrack(row = 0, col = 0):
            
            if board[row][col] == '.':
                
                for d in range(1, 10):
                    
                    if d in rows[row]:
                        continue
                        
                    if d in cols[col]:
                        continue
                        
                    if d in boxs[box_index(row, col)]:
                        continue
                    
                    place_number(d, row, col)
                    place_next_numbers(row, col)
                    
                    if not self.sudoku_solved:
                        board[row][col] = '.'
                        del rows[row][d]
                        del cols[col][d]
                        del boxs[box_index(row, col)][d]
                        
            else:
                place_next_numbers(row, col)
                    
        n = 3
        N = n * n
        box_index = lambda row, col: (row // n ) * n + col // n
        
        rows = [dict() for _ in range(N)]
        cols = [dict() for _ in range(N)]
        boxs = [dict() for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        backtrack()
```

**(8) Combination**

Combination and permutation problems can also be solved by backtracking.

Leetcode [77](https://leetcode.com/problems/combinations).

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.n = n
        self.k = k
        self.backtrack()
        return self.ans
    
    def backtrack(self, first=1, curr=[]):
        
        if len(curr) == self.k:
            self.ans.append(curr.copy())
            
        for i in range(first, self.n + 1):
            curr.append(i)
            self.backtrack(i+1, curr)
            curr.pop()
```

**(9) Combination Sum I**

Find all the combinations that sums up to a target value.

Leetcode [39](https://leetcode.com/problems/combination-sum/).

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.ans = []
        self.candidates = candidates
        self.target = target
        self.backtrack()
        
        return self.ans
        
    def backtrack(self, index=0, curr=[]):
        
        if sum(curr) == self.target:
            self.ans.append(curr.copy())
        
        if sum(curr) > self.target:
            return
            
        for i in range(index, len(self.candidates)):
            
            curr.append(self.candidates[i])
            self.backtrack(i, curr)
            curr.pop()
```

**(10) Subset**

Get the list of all the subsets of a set. Note backtrack doesn't help with this problem because it has to  traverse all the cases.

Leetcode [78](https://leetcode.com/problems/subsets/).

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        for k in range(len(nums) + 1):
            self.backtrack(k)
        return self.ans
        
    def backtrack(self, k, first=0, curr=[]):
        
        if len(curr) == k:
            self.ans.append(curr.copy())
            return
        
        for i in range(first, len(self.nums)):
            
            curr.append(self.nums[i])
            self.backtrack(k, i + 1, curr)
            curr.pop()
```

**(11) Subset II**

Everything is similar but this time the set contains duplicated values. So in this question, the backtracking will work for us.

Leetcode [90](https://leetcode.com/problems/subsets-ii).

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = sorted(nums)
        for k in range(len(nums) + 1):
            self.backtrack(k)
        return self.ans
        
    def backtrack(self, k, first=0, curr=[]):
        
        if len(curr) == k:
            self.ans.append(curr.copy())
            return
        
        for i in range(first, len(self.nums)):
            
            if i > first and self.nums[i] == self.nums[i-1]:
                continue
            
            curr.append(self.nums[i])
            self.backtrack(k, i + 1, curr)
            curr.pop()
```

**(12) Permutations**

Give all the permutations of a list.

Leetcode [46](https://leetcode.com/problems/permutations).

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        self.backtrack(nums)
        return self.ans
    
    def backtrack(self, nums, curr=[]):
        
        if len(curr) == len(self.nums):
            self.ans.append(curr.copy())
            
        for i in range(len(nums)):
            curr.append(nums[i])
            self.backtrack(nums[:i] + nums[i+1:], curr)
            curr.pop()
```

**(12) Permutations II**

Give all the permutations of a list with duplicate values.

Leetcode [47](https://leetcode.com/problems/permutations-ii).

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = sorted(nums)
        self.backtrack(self.nums)
        return self.ans
    
    def backtrack(self, nums, curr=[]):
        
        if len(curr) == len(self.nums):
            self.ans.append(curr.copy())
            
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            curr.append(nums[i])
            self.backtrack(nums[:i] + nums[i+1:], curr)
            curr.pop()
```

**(13) Letter Combinations**

Leetcode [17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/).

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        self.hashmap = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        self.ans = []
        self.backtrack(digits, [])
        return self.ans
    
    def backtrack(self, nums, curr):
        
        if not nums:
            self.ans.append("".join(curr))
            return 
        
        letter_list = self.hashmap[nums[0]]
        
        for letter in letter_list:
            curr.append(letter)
            self.backtrack(nums[1:], curr)
            curr.pop()
        
```

