# 0985 - Sum of Even Numbers After Queries

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/sum-of-even-numbers-after-queries) | [solution](https://leetcode.com/problems/sum-of-even-numbers-after-queries/solution/)


-----------

<p>We have an array <code>A</code> of integers, and an array <code>queries</code>&nbsp;of queries.</p>

<p>For the <code>i</code>-th&nbsp;query <code>val =&nbsp;queries[i][0], index&nbsp;= queries[i][1]</code>, we add <font face="monospace">val</font>&nbsp;to <code>A[index]</code>.&nbsp; Then, the answer to the <code>i</code>-th query is the sum of the even values of <code>A</code>.</p>

<p><em>(Here, the given <code>index = queries[i][1]</code> is a 0-based index, and each query permanently modifies the array <code>A</code>.)</em></p>

<p>Return the answer to all queries.&nbsp; Your <code>answer</code> array should have&nbsp;<code>answer[i]</code>&nbsp;as&nbsp;the answer to the <code>i</code>-th query.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,2,3,4]</span>, queries = <span id="example-input-1-2">[[1,0],[-3,1],[-4,0],[2,3]]</span>
<strong>Output: </strong><span id="example-output-1">[8,6,2,4]</span>
<strong>Explanation: </strong>
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= queries[i][0] &lt;= 10000</code></li>
	<li><code>0 &lt;= queries[i][1] &lt; A.length</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Maintain Array Sum

**Intuition and Algorithm**

Let's try to maintain `S`, the sum of the array throughout one query operation.

When acting on an array element `A[index]`, the rest of the values of `A` remain the same.  Let's remove `A[index]` from `S` if it is even, then add `A[index] + val` back (if it is even.)

Here are some examples:

* If we have `A = [2,2,2,2,2]`, `S = 10`, and we do `A[0] += 4`: we will update `S -= 2`, then `S += 6`.  At the end, we will have `A = [6,2,2,2,2]` and `S = 14`.

* If we have `A = [1,2,2,2,2]`, `S = 8`, and we do `A[0] += 3`: we will skip updating `S` (since `A[0]` is odd), then `S += 4`.  At the end, we will have `A = [4,2,2,2,2]` and `S = 12`.

* If we have `A = [2,2,2,2,2]`, `S = 10` and we do `A[0] += 1`: we will update `S -= 2`, then skip updating `S` (since `A[0] + 1` is odd.)  At the end, we will have `A = [3,2,2,2,2]` and `S = 8`.

* If we have `A = [1,2,2,2,2]`, `S = 8` and we do `A[0] += 2`: we will skip updating `S` (since `A[0]` is odd), then skip updating `S` again (since `A[0] + 2` is odd.)  At the end, we will have `A = [3,2,2,2,2]` and `S = 8`.

These examples help illustrate that our algorithm actually maintains the value of `S` throughout each query operation.

<iframe src="https://leetcode.com/playground/cYwLoifs/shared" frameBorder="0" width="100%" height="395" name="cYwLoifs"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N+Q)$$, where $$N$$ is the length of `A` and $$Q$$ is the number of `queries`.

* Space Complexity:  $$O(Q)$$, though we only allocate $$O(1)$$ additional space.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
