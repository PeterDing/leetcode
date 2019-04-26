# 0992 - Subarrays with K Different Integers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Hash Table, Two Pointers, Sliding Window | [Leetcode](https://leetcode.com/problems/subarrays-with-k-different-integers) | [solution](https://leetcode.com/problems/subarrays-with-k-different-integers/solution/)


-----------

<p>Given an array <code>A</code> of positive integers, call a (contiguous, not necessarily distinct) subarray of <code>A</code> <em>good</em> if the number of different integers in that subarray is exactly <code>K</code>.</p>

<p>(For example, <code>[1,2,3,1,2]</code> has <code>3</code> different integers: <code>1</code>, <code>2</code>, and <code>3</code>.)</p>

<p>Return the number of good subarrays of <code>A</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,2,1,2,3]</span>, K = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">7</span>
<strong>Explanation: </strong>Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,2,1,3,4]</span>, K = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>1 &lt;= A[i] &lt;= A.length</code></li>
	<li><code>1 &lt;= K &lt;= A.length</code></li>
</ol>

-----------


## Similar Problems

- [Medium] [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters)

- [Hard] [Longest Substring with At Most Two Distinct Characters](longest-substring-with-at-most-two-distinct-characters)

- [Hard] [Longest Substring with At Most K Distinct Characters](longest-substring-with-at-most-k-distinct-characters)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sliding Window

**Intuition**

For convenience, let's denote subarrays by tuples: `(i,j) = [A[i], A[i+1], ..., A[j]]`, and call a subarray *valid* if it has `K` different integers.

For each `j`, let's consider the set $$S_j$$ of all `i` such that the subarray `(i, j)` is valid.

Firstly, $$S_j$$ must be a contiguous interval.  If `i1 < i2 < i3`, `(i1,j)` and `(i3,j)` are valid, but `(i2,j)` is not valid, this is a contradiction because `(i2,j)` must contain more than `K` different elements [as `(i3,j)` contains `K`], but `(i1,j)` [which is a superset of `(i2,j)`] only contains `K` different integers.

So now let's write $$S_j$$ as intervals: $$S_j = [\text{left1}_j, \text{left2}_j]$$.

The second observation is that the endpoints of these intervals must be monotone increeasing - namely, $$\text{left1}_j$$ and $$\text{left2}_j$$ are monotone increasing.  With similar logic to the above, we could construct a proof of this fact, but the intuition is that after adding an extra element to our subarrays, they are already valid, or we need to shrink them a bit to keep them valid.

**Algorithm**

We'll maintain two sliding windows, corresponding to $$\text{left1}_j$$ and $$\text{left2}_j$$.  Each sliding window will be able to count how many different elements there are in the window, and add and remove elements in a queue-like fashion.

<iframe src="https://leetcode.com/playground/MkaZoDQt/shared" frameBorder="0" width="100%" height="500" name="MkaZoDQt"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
