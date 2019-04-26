# 0975 - Odd Even Jump

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming, Stack, Binary Search Tree | [Leetcode](https://leetcode.com/problems/odd-even-jump) | [solution](https://leetcode.com/problems/odd-even-jump/solution/)


-----------

<p>You are given an integer array <code>A</code>.&nbsp; From&nbsp;some starting index, you can make a series of jumps.&nbsp; The (1st, 3rd, 5th, ...)&nbsp;jumps in the series are called <em>odd numbered jumps</em>, and the (2nd, 4th, 6th, ...) jumps in the series are called <em>even numbered jumps</em>.</p>

<p>You may from index <code>i</code>&nbsp;jump forward to index <code><font face="monospace">j</font></code>&nbsp;(with <code>i&nbsp;&lt; j</code>) in the following way:</p>

<ul>
	<li>During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index <font face="monospace">j</font>&nbsp;such that <code>A[i] &lt;= A[j]</code> and <code>A[j]</code> is the smallest possible value.&nbsp; If there are multiple such indexes <code><font face="monospace">j</font></code>, you can only jump to the <strong>smallest</strong> such index <code><font face="monospace">j</font></code>.</li>
	<li>During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index <font face="monospace">j</font>&nbsp;such that <code>A[i] &gt;= A[j]</code> and <code>A[j]</code> is the largest&nbsp;possible value.&nbsp; If there are multiple such indexes <code><font face="monospace">j</font></code>, you can only jump to the <strong>smallest</strong> such index <code><font face="monospace">j</font></code>.</li>
	<li>(It may be the case that for some index <code><font face="monospace">i</font>,</code> there are no legal jumps.)</li>
</ul>

<p>A starting index is <em>good</em> if, starting from that index, you can reach the end of the array (index <code>A.length - 1</code>) by jumping some number of times (possibly 0 or more than once.)</p>

<p>Return the number of good starting indexes.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[10,13,12,14,15]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can&#39;t jump any more.
From starting index i = 1 and i = 2, we can jump to i = 3, then we can&#39;t jump any more.
From starting index i = 3, we can jump to i = 4, so we&#39;ve reached the end.
From starting index i = 4, we&#39;ve reached the end already.
In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,3,1,1,4]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:

During our 1st jump (odd numbered), we first jump to i = 1 because A[1] is the smallest value in (A[1], A[2], A[3], A[4]) that is greater than or equal to A[0].

During our 2nd jump (even numbered), we jump from i = 1 to i = 2 because A[2] is the largest value in (A[2], A[3], A[4]) that is less than or equal to A[1].  A[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3.

During our 3rd jump (odd numbered), we jump from i = 2 to i = 3 because A[3] is the smallest value in (A[3], A[4]) that is greater than or equal to A[2].

We can&#39;t jump from i = 3 to i = 4, so the starting index i = 0 is not good.

In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can&#39;t jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where we can reach the end with some number of jumps.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[5,1,3,4,2]</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong>
We can reach the end from starting indexes 1, 2, and 4.
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>0 &lt;= A[i] &lt; 100000</code></li>
</ol>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Monotonic Stack

**Intuition**

First, we notice that where you jump to is determined only by the state of your current index and the jump number parity.

For each state, there is exactly one state you could jump to (or you can't jump.)  If we somehow knew these jumps, we could solve the problem by a simple traversal.

So the problem reduces to solving this question: for some index `i` during an odd numbered jump, what index do we jump to (if any)?  The question for even-numbered jumps is similar.

**Algorithm**

Let's figure out where index `i` jumps to, assuming this is an odd-numbered jump.

Let's consider each value of `A` in order from smallest to largest.  When we consider a value `A[j] = v`, we search the values we have already processed (which are `<= v`) from largest to smallest.  If we find that we have already processed some value `v0 = A[i]` with `i < j`, then we know `i` jumps to `j`.

Naively this is a little slow, but we can speed this up with a common trick for harder problems: a monotonic stack.  (For another example of this technique, please see the solution to this problem: [(Article - Sum of Subarray Minimums)](https://leetcode.com/articles/sum-of-subarray-minimums/))

Let's store the indices `i` of the processed values `v0 = A[i]` in a stack, and maintain the invariant that this is monotone decreasing.  When we add a new index `j`, we pop all the smaller indices `i < j` from the stack, which all jump to `j`.

Afterwards, we know `oddnext[i]`, the index where `i` jumps to if this is an odd numbered jump.  Similarly, we know `evennext[i]`.  We can use this information to quickly build out all reachable states using dynamic programming.

<iframe src="https://leetcode.com/playground/fYvxEXx8/shared" frameBorder="0" width="100%" height="500" name="fYvxEXx8"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Tree Map

**Intuition**

As in *Approach 1*, the problem reduces to solving this question: for some index `i` during an odd numbered jump, what index do we jump to (if any)?

**Algorithm**

We can use a `TreeMap`, which is an excellent structure for maintaining sorted data.  Our map `vals` will map values `v = A[i]` to indices `i`.

Iterating from `i = N-2` to `i = 0`, we have some value `v = A[i]` and we want to know what the next largest or next smallest value is.  The `TreeMap.lowerKey` and `TreeMap.higherKey` functions do this for us.

With this in mind, the rest of the solution is straightforward: we use dynamic programming to maintain `odd[i]` and `even[i]`: whether the state of being at index `i` on an odd or even numbered jump is possible to reach.

<iframe src="https://leetcode.com/playground/RtJL4zUR/shared" frameBorder="0" width="100%" height="500" name="RtJL4zUR"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
