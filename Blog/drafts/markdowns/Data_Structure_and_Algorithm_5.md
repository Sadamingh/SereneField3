## Data Structure and Algorithm 5 | Graph Algorithms

![0_QXrDY4nVmhZ1umbX](../../image/0_QXrDY4nVmhZ1umbX.jpeg)

#### 1. Graph Representation

**(1) Adjacency Matrix**

The adjacency matrix with shape $n \times n$ is a symmetric matrix that has {0, 1} as its values, where 1 means two nodes are connected.

**(2) Adjacency List**

Adjacency list is a list of length $n$ stores the list of edge information.

**(3) Connected Nodes**

A node in the graph is defined by,

```python
class Node:
  	def __init__(self, value):
    		self.value = value
    		self.edges = [] 
  	def add(self, target):
    		self.edges.append(target)
  	def __repr__(self): 
    		return str(self.value)
```

This is the common implementation due to nice mapping to objects.

**(4) Node with Labelled Edges**

```python
class LNode:
		def __init__(self, value):
    		self.value = value
    		self.edges = {}
  	def add(self, label, target):
    		self.edges[label] = target
    def __repr__(self): 
    		return str(self.value)
```

#### 2. Graph Algorithms

**(1) Recall: DFS Search**

Time complexity $O(n)$.

```python
def dfsSearch(root, x, visited):
  
		if not root: return None
    if root in visited: return None
    
    visited.add(root)
    
    if root.val == x: 
      	return root
      
    for p in root.edges:
      	return dfsSearch(p, visited)
```

**(2) Reachable Nodes**

Start from a node, then get a set of nodes it can reach by,

```python
def reachable(root, reaches, visited):
  
    if root in visited: return None
    
    visited.add(root)
    
    for q in root.edges:
        reaches.add(q)
        reachable(q, reaches, visited)
        
    return reaches
```

**(3) Detecting Cycles**

```python
def iscyclic(p):
    return iscyclic_(p, p, set())

def iscyclic_(start, p, visited):
  
    if p in visited: 
        if p is start: return True
        else: return False
      
    visited.add(p)
    
    for q in p.edges:
        if iscyclic_(start, q, visited): return True 
    return False
```

**(4) Find First Path**

```python
def path(p, q):
    return path_(p, q, [p], set())

def path_(p, q, path, visited):
  
    if p is q: return path
    if p in visited: return None
    
    visited.add(p)
    
    for t in p.edges:
        pa = path_(t, q, path+[t], visited)
        if pa is not None: return pa
        
    return None
```

**(5) Find all Path**

```python
def allpaths(p, q):
    allpaths = []
    allpaths_(p, q, [p], allpaths, set())
    return allpaths

def allpaths_(p, q, path, allpaths, visited):
  
    if p is q:
        allpaths.append(path)
        return
    if p in visited: return None
    
    visited.add(p)
    
    for e in p.edges:
        allpaths_(e, q, path+[e], allpaths, visited)
        
    return None
```

**(7) BFS Search**

```python
def bfsSearch(root, x): 

    visited = {root}
    worklist = [root] 
    
    while len(worklist) > 0: 
      
        p = worklist.pop(0)
        
        if p.val == x:
          	return True
        
        for q in p.edges:
            if q not in visited:
                worklist.append(q)
                visited.add(q)
                
     return False
```

**(8) Shortest Path**

```python
def shortestPath(root, target): 
  
    visited = {root}
    worklist = [[root]]
    
    while len(worklist) > 0: 
      
        path = worklist.pop(0)
        p = path[-1]
        
        if p.value == target.value:
            return path
          
        for q in p.edges:
            if q not in visited:
                worklist.append(path+[q])
                visited.add(q)
                
    return None
```

**(9) Depth/Distance**

```python
def depths(p):
    reaches = dict()
    depths_(p, reaches, depth=0)
    return reaches

def depths_(p, reaches, depth):
  
    if p in reaches: return None
    
    reaches[p] = depth
    
    for q in p.edges:
        depths_(q, reaches, depth+1)
```

**(10) Find Neighbour within k Distance**

```python
def neighbors(p, k):
    reaches = dict()
    neighbors_(p, k, reaches, depth=0)
    return reaches

def neighbors_(p, k, reaches, depth):
  
    if p in reaches or depth > k: return None
    
    reaches[p] = depth
    
    for q in p.edges:
        neighbors_(q, k, reaches, depth+1)
```

**(11) DFS Based Topological Sort**

Here `visited` set is added not because we are caring about the cycles. It means that we don't take the nodes we have visited into the account because these nodes have already beem sorted.

```python
def topoSort(nodes):
  
    sorted = []
    visited = set()
    
    while len(visited) < len(nodes):
        todo = [node for node in nodes.values() if node not in visited]
        if len(todo) > 0:
            postorder(todo[0], sorted, visited)
            
    return sorted
```

Here it requires a post order DFS as we have written in the searching part.

```python
def postorder(p, sorted, visited):
  
    if p in visited: return
    
    visited.add(p)
    
    for q in p.edges:
        postorder(q, sorted, visited)
    sorted.append(p)
```