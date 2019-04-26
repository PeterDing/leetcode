# 0960 - Delete Columns to Make Sorted III

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/delete-columns-to-make-sorted-iii) | [solution](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/solution/)


-----------

<p>We are given an array&nbsp;<code>A</code> of <code>N</code> lowercase letter strings, all of the same length.</p>

<p>Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.</p>

<p>For example, if we have an array <code>A = [&quot;babca&quot;,&quot;bbazb&quot;]</code> and deletion indices <code>{0, 1, 4}</code>, then the final array after deletions is <code>[&quot;bc&quot;,&quot;az&quot;]</code>.</p>

<p>Suppose we chose a set of deletion indices <code>D</code> such that after deletions, the final array has <strong>every element (row) in&nbsp;lexicographic</strong> order.</p>

<p>For clarity, <code>A[0]</code> is in lexicographic order (ie. <code>A[0][0] &lt;= A[0][1] &lt;= ... &lt;= A[0][A[0].length - 1]</code>), <code>A[1]</code> is in lexicographic order (ie. <code>A[1][0] &lt;= A[1][1] &lt;= ... &lt;= A[1][A[1].length - 1]</code>), and so on.</p>

<p>Return the minimum possible value of <code>D.length</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;babca&quot;,&quot;bbazb&quot;]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>After deleting columns 0, 1, and 4, the final array is A = [&quot;bc&quot;, &quot;az&quot;].
Both these rows are individually in lexicographic order (ie. A[0][0] &lt;= A[0][1] and A[1][0] &lt;= A[1][1]).
Note that A[0] &gt; A[1] - the array A isn&#39;t necessarily in lexicographic order.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;edcba&quot;]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation: </strong>If we delete less than 4 columns, the only row won&#39;t be lexicographically sorted.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[&quot;ghi&quot;,&quot;def&quot;,&quot;abc&quot;]</span>
<strong>Output: </strong><span id="example-output-3">0</span>
<strong>Explanation: </strong>All rows are already lexicographically sorted.
</pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 100</code></li>
</ol>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition and Algorithm**

This is a tricky problem that is hard to build an intuition about.

First, lets try to find the number of columns to keep, instead of the number to delete.  At the end, we can subtract to find the desired answer.

Now, let's say we must keep the first column `C`.  The next column `D` we keep must have all rows lexicographically sorted (ie. `C[i] <= D[i]`), and we can say that we have deleted all columns between `C` and `D`.

Now, we can use dynamic programming to solve the problem in this manner.  Let `dp[k]` be the number of columns that are kept in answering the question for input `[row[k:] for row in A]`.  The above gives a simple recursion for `dp[k]`.

<iframe src="https://leetcode.com/playground/dYqmP2Pc/shared" frameBorder="0" width="100%" height="395" name="dYqmP2Pc"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N * W^2)$$, where $$N$$ is the length of `A`, and $$W$$ is the length of each word in `A`.

* Space Complexity:  $$O(W)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
