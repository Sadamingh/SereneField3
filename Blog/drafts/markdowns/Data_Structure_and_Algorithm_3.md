## Data Structure and Algorithm 3 | Sorting Algorithms

![0_QXrDY4nVmhZ1umbX](../../image/0_QXrDY4nVmhZ1umbX.jpeg)

#### 1. General Sorting Algorithms

**(1) Selection Sort**

Select the minimum value in an array, then put it to the front.

Time complexity $O(n^2)$.

```python
def selectionSort(a):
   
    for step in range(len(a)):
        min_idx = step
        for i in range(step + 1, len(a)):
            if a[i] < a[min_idx]:
                min_idx = i
        a[step], a[min_idx] = a[min_idx], a[step]
        
    return a
```

**(2) Insertion Sort**

Traverse each value, put it forward if the former one is smaller until the former one is larger.

Time complexity $O(n^2)$.

```python
def insertionSort(a):

    for i, key in enumerate(a[1:]):
      
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        
        a[j + 1] = key
        
    return a
```

**(3) Exchange Sort**

Traverse each key in the array, swap if the key and the following key pairs are unordered. Note that this is different from bubble sort.

Time complexity $O(n^2)$.

```python
def exchangeSort(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j],  a[i]

		return a
```

**(4) Bubble Sort: Baseline**

Select each pair of keys, swap them if the former one is larger than the later one. Remember the last `i` keys must be sorted in the $i^{th}$ iteration so that we can skip them.

Time complexity $O(n^2)$.

```python
def bubbleSort(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
```

**(5) Bubble Sort: Optimized**

In the bubble sort, we can stop early when there's no more swaps in one iteration, which means the rest of the array is already sorted. We can add a `swapped` variable to show if we need to go to the next iteration.

Time complexity $O(n^2)$.

```python
def bubbleSort(a):
    for i in range(len(a)):
      	swapped = False
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped: break
    return a
```

<img src="../../image/Screen Shot 2022-03-10 at 9.27.28 PM.png" alt="Screen Shot 2022-03-10 at 9.27.28 PM" style="zoom:90%;" />

**(6) Merge Sort**

Merge sort is a divide and conquer solution which first divide the array into pairs. Then we sort these pairs and finally merge these sorted arrays together with `mergeTwoSortedArray` function of time complexity of $O(n)$. 

In general, this sorting technique has a time complexity of $O(n \log n)$.

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
```

Here is an example of `mergeTwoSortedArray` function with time complexity of $O(n)$.

```python
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

**(7) Quick Sort**

Quick sort is another divide and conquer algorithm. The idea of quick sort is to select one key as pivot, then put all the keys smaller than it on its left, and put all the other keys on its right by function `partition`. Then we continue this process for the left and right part until we get a sorted array. 

```python
def quickSort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quickSort(a, low, pi - 1)
        quickSort(a, pi + 1, high)
        
quickSort(a, 0, len(a)-1)
```

There are many ways to perform the partition. Here is a naive solution of time complexity $O(n)$.

```python
def partition(a, lo, hi):
    pivot = a[hi]
    left  = [a[i] for i in range(lo,hi) if a[i]<pivot]
    right = [a[i] for i in range(lo,hi) if a[i]>=pivot]
    a[lo:hi+1] = left + [pivot] + right
    return lo + len(left)
```

Or we can also use the following partition function for partition with ime complexity $O(m)$, where $m = hi - lo$. This method is called **Lomuto partition scheme**.

```python
def partition(a, lo, hi):

    pivot = a[hi]
    
    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i = i + 1
      			a[i], a[j] = a[j], a[i]
  	a[i+1], a[hi] = a[hi], a[i+1]
    
  	return i + 1
```

#### 2. Heuristic Sorting Algorithms

Let's say we know some domain knowledge of the keys we have in the array, then we can develop some heuristic sorting algorithms that is much much faster than the general theorical limition $O(n \log n)$.

**(1) Sorting Non-negative Integers: Pigeonhole**

The idea is very simple. It is like we first count the amout of each integer we have in the list. And then we output the integers in the order from low to high with repeating times we calculated. So this is not actually sorting. 

Time complexity is $O(n) = T(n, \max)$.

```python
def pigeonholeSort(a):
  
  	result = []
    
    size = max(a) + 1
    holes = [0] * size
    for x in a:
        holes[x] += 1
    
    for i in range(0,size):
        result.extend([i] * holes[i])
        
    return result
```

Note that when we have a short array with an extraordinary large maximum value, we are going to experience a huge cost of the space complexity and the algorithm will become super slow!

**(2) Sorting Non-negative Integers: Bucket Sort** 

To deal with the problem of pigeonhole, we can use a hashtable like data structure to store the keys. The difference is that these buckets actually have an order that we can directly join the sorted keys in each bucket to get a sorted result. The worst time complexity is $O(n^2)$ and the average time complexity is $O(n)$.

```python
def bsort(a, nbuckets=5) -> list:
  
    mx = max(a)
    buckets = [[] for i in range(nbuckets)]
    result = []
    
    for x in a:
        x_normalized = x / mx 
        i = int(x_normalized * (nbuckets-1)) 
        buckets[i].append(x)
        
    for i in range(nbuckets):
        result.extend(sorted(buckets[i]))
        
    return result
```

**(3) Sorting Strings: Bucket Sort**

Bucket sort can also be used to sort a string array. It is similar to a hashtable with index of letters. The problem is that if we have all the words start with the same letter in an array, this data structure will be useless. In order to deal with this problem, we will introduce **trie** structure in the next section.

```python
def pstr_sort(a):
  	
    result = []
  	
  	nbuckets = ord('z') - ord('a') + 1
    buckets = [[] for i in range(nbuckets)]
    
    for x in a:
        i = ord(x[0]) - ord('a')
        buckets[i].append(x)

    for i in range(nbuckets):
        result.extend(sorted(buckets[i]))
        
    return result
```