## Data Structure and Algorithm 7 | Divide and Conquer

![0_QXrDY4nVmhZ1umbX](../../image/0_QXrDY4nVmhZ1umbX.jpeg)

#### 1. Divide-and-Conquer Algorithm

**(1) Definition**

The divide-and-conquer algorithm recursively breaks down a problem two or more sub-problems of the same or related type, until these become simple enough to be solved directly.  The solutions to the sub-problems are then combined to give a solution to the original problem.

**(2) Pseudocode**

```python
def divide_and_conquer(case):
		subcases = divide(case)
		results = [conquer(subcase) for subcase in subcases]
		return combine(results)
```

**(3) Review: Merge Sort**

Time complexity $O(n\log n)$.

Leetcode [912](https://leetcode.com/problems/sort-an-array/).

```python
def mergesort(data):
  
    if len(data)==0:
        return []
      
    elif len(data)==1:
        return [data[0]]
      
    elif len(data)==2:
        if data[0]<data[1]:
            return data
        return [data[1], data[0]]
      
    else:
        m = len(data) // 2
        left = mergesort(data[0:m])
        right = mergesort(data[m:])
        return mergeTwoSortedArray(left, right)
        
def mergeTwoSortedArray(list1, list2):
 		result = []
        
    p1 = 0
    p2 = 0
        
    while True:
        if p1 == len(list1) and p2 == len(list2):
            return result
        elif p1 == len(list1):
            result.append(list2[p2])
            p2 += 1
        elif p2 == len(list2):
            result.append(list1[p1])
            p1 += 1
        else:
            if list1[p1] > list2[p2]:
                result.append(list2[p2])
                p2 += 1
            else:
                result.append(list1[p1])
                p1 += 1
                
   return result
```

**(4) Review: Quick Sort**

Time complexity $O(n\log n)$.

Leetcode [912](https://leetcode.com/problems/sort-an-array/).

```python
def partition(a, lo, hi):
    pivot = a[hi]
    left  = [a[i] for i in range(lo,hi) if a[i]<pivot]
    right = [a[i] for i in range(lo,hi) if a[i]>=pivot]
    a[lo:hi+1] = left + [pivot] + right
    return lo + len(left)

def quickSort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quickSort(a, low, pi - 1)
        quickSort(a, pi + 1, high)
        
quickSort(a, 0, len(a)-1)
```

**(5) Valid BST**

Given the root of a tree, return if it is a BST.

Leetcode [98]().

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)
    
    def validate(self, node, low=-math.inf, high=math.inf):
        
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        return self.validate(node.right, node.val, high) and self.validate(node.left, low, node.val)
```

**(6) Search Matrix I**

Search a target element in a sorted matrix. This is a binary search problem.

Leetcode [240](https://leetcode.com/problems/search-a-2d-matrix-ii/).

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat_flat = []
        for row in matrix:
            mat_flat += row
            
        left = 0
        right = len(mat_flat) - 1
        
        pivot = right // 2
        
        while left <= right:
            if mat_flat[pivot] > target:
                right = pivot - 1
                pivot = (left + right) // 2
            elif mat_flat[pivot] < target:
                left = pivot + 1
                pivot = (left + right) // 2
            else:
                return True
```

**(7) Search Matrix II**

Search a target element in a matrix with both sorted columns and sorted rows. The idea is to device the matrix into smaller ones

Leetcode [240](https://leetcode.com/problems/search-a-2d-matrix-ii/).

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        def search_rec(left, up, right, down):
            
            if left > right or up > down:
                return False
            
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right - left) // 2
            row = up
            
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
                
            return search_rec(left, row, mid - 1, down) or search_rec(mid+1, up, right, row - 1)
        
        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
```

