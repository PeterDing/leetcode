# 0952 - Largest Component Size by Common Factor

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math, Union Find | [Leetcode](https://leetcode.com/problems/largest-component-size-by-common-factor) | [solution](https://leetcode.com/problems/largest-component-size-by-common-factor/solution/)


-----------

<p>Given a non-empty&nbsp;array of unique positive integers <code>A</code>, consider the following graph:</p>

<ul>
	<li>There are <code>A.length</code> nodes, labelled <code>A[0]</code> to <code>A[A.length - 1];</code></li>
	<li>There is an edge between <code>A[i]</code> and <code>A[j]</code>&nbsp;if and only if&nbsp;<code>A[i]</code> and <code>A[j]</code> share a common factor greater than 1.</li>
</ul>

<p>Return the size of the largest connected component in the graph.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[4,6,15,35]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex1.png" style="width: 257px; height: 50px;" /></span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[20,50,9,63]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex2.png" style="width: 293px; height: 50px;" /></span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[2,3,6,7,4,12,21,39]</span>
<strong>Output: </strong><span id="example-output-3">8</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex3.png" style="width: 346px; height: 180px;" /></span>
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Union-Find

We will skip the explanation of how a DSU structure is implemented.  Please refer to [https://leetcode.com/problems/redundant-connection/solution/](https://leetcode.com/problems/redundant-connection/solution/) for a tutorial on DSU.

**Intuition**

Let $$W = \max(A[i])$$, and $$R = \sqrt{W}$$.  For each value $$A[i]$$, there is at most one prime factor $$p \geq R$$ dividing $$A[i]$$.  Let's call $$A[i]$$'s "big prime" this $$p$$, if it exists.

This means that there are at most $$R + A\text{.length}$$ unique prime divisors of elements in $$A$$:  the big primes correspond to a maximum of $$A\text{.length}$$ values, and the small primes are all less than $$R$$, so there's at most $$R$$ of them too.

**Algorithm**

Factor each $$A[i]$$ into prime factors, and index every occurrence of these primes.  (To save time, we can use a sieve.  Please see this article's comments for more details.)

Then, use a union-find structure to union together any prime factors that came from the same $$A[i]$$.

Finally, we can count the size of each component, by inspecting and counting the id of the component each $$A[i]$$ belongs to.

<iframe src="https://leetcode.com/playground/MAiR5RjS/shared" frameBorder="0" width="100%" height="500" name="MAiR5RjS"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N\sqrt{W})$$ where $$N$$ is the length of `A`, and $$W = \max(A[i])$$.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
