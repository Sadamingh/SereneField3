## Data Structure and Algorithm 4 | Walking and Searching

![0_QXrDY4nVmhZ1umbX](../../image/0_QXrDY4nVmhZ1umbX.jpeg)

#### 1. Walking Algorithms

**(1) Array Walking**

Time complexity $O(n)$.

```python
def walkArray(a):
		for i in range(len(a)):
				print(a[i])
```

**(2) 2D Array (Matrix) Walking** 

Time complexity $O(n^2)$.

```python
def walkMatrix(a):
		for i in range(len(a)):
				for j in range(len(a[0])):
          	print(a[i][j])
```

**(3) Linked List Walking**

Time complexity $O(n)$.

```python
def walkLinkedList(root):
		p = root
    while p:
      	print(p.val)
				p = p.next
```

**(4) Pre-Order Tree Walking (DFS)**

Suppose we have a tree of,

```
              1
           /     \   
         2         3
       /   \     /
      4     5   6
```

Then the pre-order output should be a sequence of,

```
[1, 2, 4, 5, 3, 6]
```

Time complexity $O(n)$,

```python
def preorderTraversal(root):
    if not root: return
		print(root.val)
    if root.left: preorderTraversal(root.left)
    if root.right: preorderTraversal(root.right)
```

**(6) In-Order Tree Walking (DFS)**

See [leetcode 94](https://leetcode.com/problems/binary-tree-inorder-traversal/).

Suppose we have a tree of,

```
              1
           /     \   
         2         3
       /   \     /
      4     5   6
```

Then the in-order output should be a sequence of,

```
[4, 2, 5, 1, 6, 3]
```

Time complexity $O(n)$,

```python
def inorderTraversal(root):
    if not root: return
    if root.left: preorderTraversal(root.left)
    print(root.val)
    if root.right: preorderTraversal(root.right)
```

**(7) Post-Order Tree Walking (DFS)**

Suppose we have a tree of,

```
              1
           /     \   
         2         3
       /   \     /
      4     5   6
```

Then the post-order output should be a sequence of,

```
[4, 5, 2, 6, 3, 1]
```

Time complexity $O(n)$,

```python
def postorderTraversal(root):
    if not root: return
    if root.left: preorderTraversal(root.left)
    if root.right: preorderTraversal(root.right)
    print(root.val)
```

**(8) Walking DAG (DFS)**

Directed acyclic graph are the simplest graph that we can walk through without cycles.

Time complexity $O(n)$.

```python
def walkDAG(root):
		if not root: return
    print(root.val)
    for p in root.edges:
      	walkDAG(p)
```

**(9) Walking Graphs with Cycles (DFS)**

We should maintain a `visited` set to record the nodes we have visited and this requires an $O(n)$ space complexity. 

Time complexity $O(n)$.

```python
def walkGraph(root, visited: set):
		if not root: return
    if root in visited: return
    visited.add(root)
    print(root.val)
    for p in root.edges:
      	walkGraph(p, visited)
```

Note that the `visited` can also be a list but searching a list has a higher time complexity than a set. Remember this algorithm works because we are passing the pointer to `visited`  as an argument so that if we make a copy of the set or list we pass, the algorithm will no longer work for us.

````python
def walkGraph(root, visited: set):
		if not root: return
    if root in visited: return
    visited.add(root)
    print(root.val)
    for p in root.edges:
      	walkGraph(p, visited.copy())
````

#### 2. Searching

**(1) Searching Sorted Array: Binary Search (Iterations)**

Time complexity $O(\log n)$.

```python
def binSearch(a, x):
  	
    left = 0
    right = len(a) - 1
    
    while left <= right:
      	pivot = (left + right) // 2
        if a[pivot] == x: 
          	return pivot
        elif a[pivot] < x: 
          	left = pivot + 1
        else: 
          	right = pivot - 1
            
    return -1
```

**(2) Searching Sorted Array: Binary Search (Recursion)**

Time complexity $O(\log n)$.

````python
def re_binSearch(a, x, left, right):
  
  	if left >= right: return -1
  
    pivot = (left + right) // 2
        
    if a[pivot] == x: 
       return pivot
    elif a[pivot] < x: 
       return re_binSearch(a, x, pivot + 1, right)
    else: 
       return re_binSearch(a, x, left, pivot - 1)
````

**(3) Searching Hash Table**

Time complexity at the best case is $O(1)$, and at the worst case is $O(n)$.

```python
def hashTable(a):
  	buckets = [[] for i in range(len(a))]
    for x in a:
				idx = hash(x) % len(a)
    		buckets[idx].append(x)
   	return buckets

def hashSearch(a, x):
  	ht = hashTable(a)
    for word in ht[hash(x) % len(a)]:
      	if x == word:
          	return True
  	return False
```

**(4) Search String Trie**

String trie is a more efficient data structure for word searching. Suppose the trie nodes has,

```python
class TrieNode:
    def __init__(self):
        self.isword = False
        self.edges = {}
```

And we use the `add` function to add a new word to trie.

```python
def add(p:TrieNode, s:str, i=0) -> None:
  
    if i>=len(s):
        p.isword = True
        return
      
    if s[i] not in p.edges:
        p.edges[s[i]] = TrieNode()
        
    add(p.edges[s[i]], s, i+1)
```

Then, the following search algorithm (similar to walk through a graph) has a time complexity of $O(n)$ for searching a word in that data structure,

```python
def trieSearch(root:TrieNode, s:str, i=0) -> bool:
    
    p = root
    
    while p is not None:
      
        if i >= len(s): 
            return p.isword
          
        if s[i] not in p.edges: 
            return False
          
        p = p.edges[s[i]]
        i += 1
```