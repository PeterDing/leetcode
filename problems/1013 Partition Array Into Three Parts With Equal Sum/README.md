# 1013 - Partition Array Into Three Parts With Equal Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum) | [solution](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/solution/)


-----------

<p>Given an array <code>A</code> of integers, return <code>true</code> if and only if we can partition the array into three <strong>non-empty</strong> parts with equal sums.</p>

<p>Formally, we can partition the array if we can find indexes <code>i+1 &lt; j</code> with <code>(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])</code></p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[0,2,1,-6,6,-7,9,1,2,0,1]</span>
<strong>Output: </strong><span id="example-output-1">true
<strong>Explanation: </strong>0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,2,1,-6,6,7,9,-1,2,0,1]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[3,3,6,5,-2,2,5,1,-9,4]</span>
<strong>Output: </strong><span id="example-output-3">true
<strong>Explanation: </strong>3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4</span>
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 50000</code></li>
	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>
</ol>

-----------


## Similar Problems




## Thought:
