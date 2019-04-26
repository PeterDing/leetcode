# 0349 - Intersection of Two Arrays

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table, Two Pointers, Binary Search, Sort | [Leetcode](https://leetcode.com/problems/intersection-of-two-arrays) | [solution](https://leetcode.com/problems/intersection-of-two-arrays/solution/)


-----------

<p>Given two arrays, write a function to compute their intersection.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-1-1">[1,2,2,1]</span>, nums2 = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-2-1">[4,9,5]</span>, nums2 = <span id="example-input-2-2">[9,4,9,8,4]</span>
<strong>Output: </strong><span id="example-output-2">[9,4]</span></pre>
</div>

<p><b>Note:</b></p>

<ul>
	<li>Each element in the result must be unique.</li>
	<li>The result can be in any order.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Easy] [Intersection of Two Arrays II](intersection-of-two-arrays-ii)




## Solution:

[TOC]

## Solution

---

#### Approach 1: Two Sets

**Intuition**

The naive approach would be to iterate along the first array `nums1`
and to check for each value if this value in `nums2` or not. 
If yes - add the value to output. Such an approach would result 
in a pretty bad
$$\mathcal{O}(n \times m)$$ time complexity, where `n` and `m` are 
arrays' lengths.

> To solve the problem in linear time, let's use the structure `set`,
which provides `in/contains` operation in $$\mathcal{O}(1)$$ time in
average case.

The idea is to convert both arrays into sets, and then iterate over 
the smallest set checking the presence of each element in the larger set.
Time complexity of this approach is $$\mathcal{O}(n + m)$$ in the average case.

!?!../Documents/349_LIS.json:1000,352!?!

**Implementation**

<iframe src="https://leetcode.com/playground/i5eLapjz/shared" frameBorder="0" width="100%" height="395" name="i5eLapjz"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(n + m)$$, where `n` and `m` are 
arrays' lengths. $$\mathcal{O}(n)$$ time is used to convert `nums1`
into set, $$\mathcal{O}(m)$$ time is used to convert `nums2`, and
`contains/in` operations are $$\mathcal{O}(1)$$ in the average case.
 
* Space complexity : $$\mathcal{O}(m + n)$$ in the worst case when
all elements in the arrays are different.
<br />
<br />


---
#### Approach 2: Built-in Set Intersection

**Intuition**

There are built-in intersection facilities,
which provide $$\mathcal{O}(n + m)$$ time complexity in the 
average case and $$\mathcal{O}(n \times m)$$ time complexity in the 
worst case. 

> In Python it's [intersection operator](https://wiki.python.org/moin/TimeComplexity#set), 
in Java - [retainAll() function](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractCollection.html#retainAll-java.util.Collection-).

**Implementation**

<iframe src="https://leetcode.com/playground/fYrF2xVt/shared" frameBorder="0" width="100%" height="310" name="fYrF2xVt"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(n + m)$$ in the average case 
 and $$\mathcal{O}(n \times m)$$ [in the worst case
 when load factor is high enough](https://wiki.python.org/moin/TimeComplexity#set).
 
* Space complexity : $$\mathcal{O}(n + m)$$ in the worst case when
all elements in the arrays are different.

Analysis written by @[liaison](https://leetcode.com/liaison/)
and @[andvary](https://leetcode.com/andvary/)
