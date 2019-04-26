# 0347 - Top K Frequent Elements

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table, Heap | [Leetcode](https://leetcode.com/problems/top-k-frequent-elements) | [solution](https://leetcode.com/problems/top-k-frequent-elements/solution/)


-----------

<p>Given a non-empty array of integers, return the <b><i>k</i></b> most frequent elements.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[1,1,1,2,2,3]</span>, k = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">[1,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[1]</span>, k = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">[1]</span></pre>
</div>

<p><b>Note: </b></p>

<ul>
	<li>You may assume <i>k</i> is always valid, 1 &le; <i>k</i> &le; number of unique elements.</li>
	<li>Your algorithm&#39;s time complexity <b>must be</b> better than O(<i>n</i> log <i>n</i>), where <i>n</i> is the array&#39;s size.</li>
</ul>


-----------


## Similar Problems

- [Medium] [Word Frequency](word-frequency)

- [Medium] [Kth Largest Element in an Array](kth-largest-element-in-an-array)

- [Medium] [Sort Characters By Frequency](sort-characters-by-frequency)

- [Medium] [Split Array into Consecutive Subsequences](split-array-into-consecutive-subsequences)

- [Medium] [Top K Frequent Words](top-k-frequent-words)

- [Medium] [K Closest Points to Origin](k-closest-points-to-origin)




## Solution:

[TOC]

## Solution

---

#### Intuition

If `k = 1` the linear-time solution is quite simple. One could keep 
the frequency of elements appearance in a hash map and update the maximum
element at each step. 

When `k > 1` we need a data structure that 
has a fast access to the elements
ordered by their frequencies. 
The idea here is to use the heap which is also known as priority queue.
<br />
<br />


---
#### Approach 1: Heap

The first step is to build a hash map `element -> its frequency`.
In Java we could use data structure `HashMap` but have to fill it manually.
Python provides us both a dictionary structure for the hash map and
a method `Counter` in the `collections` library 
to build the hash map we need.   
This step takes $$\mathcal{O}(N)$$ time where `N` is number of elements 
in the list.

The second step is to build a heap. 
The time complexity of adding an element in a heap
is $$\mathcal{O}(\log(k))$$ and we do it `N` times that means
$$\mathcal{O}(N \log(k))$$ time complexity for this step.

The last step to build an output list has  
$$\mathcal{O}(k \log(k))$$ time complexity.
 
In Python there is a method `nlargest` in `heapq` library 
([check here the source code](https://hg.python.org/cpython/file/2.7/Lib/heapq.py#l203))
which has the same $$\mathcal{O}(k \log(k))$$ time complexity
and combines two last steps in one line.

<!--![LIS](../Figures/347/347_tr.gif)-->
!?!../Documents/347_LIS.json:1000,498!?!

<iframe src="https://leetcode.com/playground/nMWGBTcf/shared" frameBorder="0" width="100%" height="500" name="nMWGBTcf"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N \log(k))$$. 
The complexity of `Counter` method is $$\mathcal{O}(N)$$. 
To build a heap and output list takes $$\mathcal{O}(N \log(k))$$.
Hence the overall complexity of the algorithm is 
$$\mathcal{O}(N + N \log(k)) = \mathcal{O}(N \log(k))$$.

* Space complexity : $$\mathcal{O}(N)$$ to store the hash map.

**Side Notes**

Following the complexity analysis, the approach is
optimal for small `k`. In the case of large `k`, one could
revert the procedure by excluding the less frequent elements from
the output.

Analysis written by @[liaison](https://leetcode.com/liaison/)
and @[andvary](https://leetcode.com/andvary/)
