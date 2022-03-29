## Data Structure and Algorithm 8 | Hashtable

![0_QXrDY4nVmhZ1umbX](../../image/0_QXrDY4nVmhZ1umbX.jpeg)

#### 1. Hashtable

**(1) Hashset Implementation**

Design a hashset.

Leetcode [75](https://leetcode.com/problems/design-hashset/).

```python
class MyHashSet:

    def __init__(self):
        self.nbuckets = 10000
        self.set = [[] for _ in range(self.nbuckets)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            index = key % self.nbuckets
            self.set[index].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            index = key % self.nbuckets
            self.set[index].remove(key)
        
    def contains(self, key: int) -> bool:
        index = key % self.nbuckets
        return key in self.set[index]
```

**(2) Hashset Implementation**

Design a hashmap.

Leetcode [75](https://leetcode.com/problems/design-hashset/).

```python
class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        
    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key)
```

**(3) Single Number**

Find the only number appeared once.

Leetcode [136](https://leetcode.com/problems/single-number/).

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        visited = set()
        
        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                visited.remove(num)
                
        return visited.pop()
```

**(4) Happy Number**

Check if an integer follows the rule of a happy number.

Leetcode [202](https://leetcode.com/problems/happy-number/).

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        visited.add(n)
        
        while True:
            
            next_n = sum([int(i)**2 for i in str(n)])
            
            if next_n == 1:
                return True
            
            elif next_n in visited:
                return False
            
            else:
                visited.add(next_n)
                n = next_n
```

**(5) Two Sum**

Find two values sum up to target.

Leetcode [1](https://leetcode.com/problems/two-sum/).

```python
class Solution(object):
    def twoSum(self, nums, target):
        
        hashmap = {o: i for i, o in enumerate(nums)}
        
        for i in range(len(nums)):
            
            j = target - nums[i]
            
            if j in hashmap and hashmap[j] != i:
                return [i, hashmap[j]]
```

**(6) Isomorphic Strings**

Leetcode [205](https://leetcode.com/problems/isomorphic-strings/).

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
                else:
                    continue
            else:
                hashmap[s[i]] = t[i]
                
        hashmap = {}
        
        for i in range(len(t)):
            if t[i] in hashmap:
                if hashmap[t[i]] != s[i]:
                    return False
                else:
                    continue
            else:
                hashmap[t[i]] = s[i]
                
        return True
```

**(7) Find Restaurant**

Trick: mapping keywords to index.

Leetcode [599](https://leetcode.com/problems/minimum-index-sum-of-two-lists/).

```python
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        minval = math.inf
        keyword = []
        
        map1 = {o:i for i, o in enumerate(list1)}
        map2 = {o:i for i, o in enumerate(list2)}
        
        for key in set(list1).intersection(set(list2)):
            sumval = map1[key] + map2[key]
            if sumval < minval:
                minval = sumval
                keyword = [key]
            elif sumval == minval:
                keyword.append(key)

        return keyword
```
