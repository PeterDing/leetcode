# 0665 - Non-decreasing Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/non-decreasing-array) | [solution](https://leetcode.com/problems/non-decreasing-array/solution/)


-----------

<p>
Given an array with <code>n</code> integers, your task is to check if it could become non-decreasing by modifying <b>at most</b> <code>1</code> element.
</p>

<p>
We define an array is non-decreasing if <code>array[i] <= array[i + 1]</code> holds for every <code>i</code> (1 <= i < n).
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [4,2,3]
<b>Output:</b> True
<b>Explanation:</b> You could modify the first <code>4</code> to <code>1</code> to get a non-decreasing array.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [4,2,1]
<b>Output:</b> False
<b>Explanation:</b> You can't get a non-decreasing array by modify at most one element.
</pre>
</p>

<p><b>Note:</b>
The <code>n</code> belongs to [1, 10,000].
</p>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach #1: Brute Force [Time Limit Exceeded]

**Intuition**

For the given array $$\text{A}$$, if we are changing at most one element $$\text{A[i]}$$, we should change $$\text{A[i]}$$ to $$\text{A[i-1]}$$, as it would be guaranteed that $$\text{A[i-1]} &leq; \text{A[i]}$$, and $$\text{A[i]}$$ would be the smallest possible to try and achieve $$\text{A[i]} &leq; \text{A[i+1]}$$.

**Algorithm**

For each possible change $$\text{A[i]}$$, check if the sequence is monotone increasing.  We'll modify $$\text{new}$$, a copy of the array $$\text{A}$$.

<iframe src="https://leetcode.com/playground/FK7JPfxR/shared" frameBorder="0" name="FK7JPfxR" width="100%" height="343"></iframe>

**Complexity Analysis**

* Time Complexity: Let $$N$$ be the length of the given array.  For each element $$\text{A[i]}$$, we check if some sequence is monotone increasing, which takes $$O(N)$$ steps.  In total, this is a complexity of $$O(N^2)$$.

* Space Complexity: To hold our array $$\text{new}$$, we need $$O(N)$$ space.

---
#### Approach #2: Reduce to Smaller Problem [Accepted]

**Intuition**

If $$\text{A[0]} &leq; \text{A[1]} &leq; \text{A[2]}$$, then we may remove $$\text{A[0]}$$ without changing the answer.  Similarly, if $$\text{A}\big[\text{len(A)-3}\big] &leq; \text{A}\big[\text{len(A)-2}\big] &leq; \text{A}\big[\text{len(A)-1}\big]$$, we may remove $$\text{A[len(A)-1]}$$ without changing the answer.

If the problem is solvable, then after these removals, very few numbers will remain.

**Algorithm**

Consider the interval $$\text{[i, j]}$$ corresponding to the subarray $$\big[\text{A[i], A[i+1], ..., A[j]}\big]$$.  When $$\text{A[i]} &leq; \text{A[i+1]} &leq; \text{A[i+2]}$$, we know we do not need to modify $$\text{A[i]}$$, and we can consider solving the problem on the interval $$\text{[i+1, j]}$$ instead.  We use a similar approach for $$j$$.

Afterwards, with the length of the interval under consideration being $$\text{j - i + 1}$$, if the interval has size 2 or less, then we did not find any problem.  

If our interval under consideration has 5 or more elements, then there are two disjoint problems that cannot be fixed with one replacement.  

Otherwise, our problem size is now at most 4 elements, which we can easily brute force.


<iframe src="https://leetcode.com/playground/4ypTHUiy/shared" frameBorder="0" name="4ypTHUiy" width="100%" height="343"></iframe>

**Complexity Analysis**

* Time Complexity: Let $$N$$ be the length of the given array.  Our pointers $$i$$ and $$j$$ move at most $$O(N)$$ times.  Our brute force is constant time as there are at most 4 elements in the array.  Hence, the complexity is $$O(N)$$.

* Space Complexity:  The extra array $$\text{A[i: j+1]}$$ only has at most 4 elements, so it is constant space, and so is the space used by our auxillary brute force algorithm.  In total, the space complexity is $$O(1)$$.

---
#### Approach #3: Locate and Analyze Problem Index [Accepted]

**Intuition**

Consider all indices $$p$$ for which $$\text{A[p]} > \text{A[p+1]}$$.  If there are zero, the answer is `True`.  If there are 2 or more, the answer is `False`, as more than one element of the array must be changed for $$\text{A}$$ to be monotone increasing.

At the problem index $$p$$, we only care about the surrounding elements.  Thus, immediately the problem is reduced to a very small size that can be analyzed by casework.

**Algorithm**

As before, let $$p$$ be the unique problem index for which $$\text{A[p]} > \text{A[p+1]}$$.  If this is not unique or doesn't exist, the answer is `False` or `True` respectively.  We analyze the following cases:

* If $$\text{p = 0}$$, then we could make the array good by setting $$\text{A[p] = A[p+1]}$$.
* If $$\text{p = len(A) - 2}$$, then we could make the array good by setting $$\text{A[p+1] = A[p]}$$.
* Otherwise, $$\text{A[p-1], A[p], A[p+1], A[p+2]}$$ all exist, and:
    * We could change $$\text{A[p]}$$ to be between $$\text{A[p-1]}$$ and $$\text{A[p+1]}$$ if possible, or;
    * We could change $$\text{A[p+1]}$$ to be between $$\text{A[p]}$$ and $$\text{A[p+2]}$$ if possible.

<iframe src="https://leetcode.com/playground/NGHYqESJ/shared" frameBorder="0" name="NGHYqESJ" width="100%" height="241"></iframe>

**Complexity Analysis**

* Time Complexity: Let $$N$$ be the length of the given array.  We loop through the array once, so our time complexity is $$O(N)$$.

* Space Complexity:  We only use $$p$$ and $$i$$, and the answer itself as the additional space.  The additional space complexity is $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice)
