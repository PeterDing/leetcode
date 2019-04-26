# 0995 - Minimum Number of K Consecutive Bit Flips

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Greedy, Sliding Window | [Leetcode](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips) | [solution](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/)


-----------

<p>In an array <code>A</code> containing only 0s and 1s, a <i><code>K</code>-bit flip&nbsp;</i>consists of choosing a (contiguous) subarray of length <code>K</code> and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.</p>

<p>Return the minimum number of <code>K</code>-bit flips required so that there is no 0 in the array.&nbsp; If it is not possible, return <code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[0,1,0]</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>Flip A[0], then flip A[2].
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,1,0]</span>, K = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation:</strong>&nbsp;No matter how we flip subarrays of size 2, we can&#39;t make the array become [1,1,1].
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[0,0,0,1,0,1,1,0]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation:</strong>
Flip A[0],A[1],A[2]:&nbsp;A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]:&nbsp;A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]:&nbsp;A becomes [1,1,1,1,1,1,1,1]
</pre>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;=&nbsp;30000</code></li>
	<li><code>1 &lt;= K &lt;= A.length</code></li>
</ol>

-----------


## Similar Problems

- [Medium] [Bulb Switcher](bulb-switcher)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Greedy + Events

**Intuition**

If the leftmost element is a 0, we must flip the subarray starting at index 0.  Similarly, if the leftmost element is a 1, we should not flip the subarray starting at index 0.  This proves we can proceed in a greedy manner: after finding out whether we have to flip the first subarray (positions 0 to K-1) or not, we can consider the array with the first element (value 1) removed, and repeat this process.

We can do better.  Every time we flip a subarray `A[i], A[i+1], ..., A[i+K-1]`, we can consider this as two "events", one 'opening event' at position `i` that marks the start of the subarray, and one 'closing event' at position `i+K` that marks the end of the subarray.  Using these events, we always know how many overlapping flipped subarrays there are: its simply the number of opening events minus the number of closing events.

**Algorithm**

When we flip a subarray, let's call the set of indices we flipped an interval.  We'll keep track of `flip`, the number of overlapping intervals in our current position.  We only care about the value of `flip` modulo 2.

When we flip an interval starting at `i`, we create a hint for a closing event at `i+K` telling us to flip our writing state back.

Please see the inline comments for more details.

<iframe src="https://leetcode.com/playground/C4RkaMHp/shared" frameBorder="0" width="100%" height="429" name="C4RkaMHp"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
