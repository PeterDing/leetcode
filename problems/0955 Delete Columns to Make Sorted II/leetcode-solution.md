# 0955 - Delete Columns to Make Sorted II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Greedy | [Leetcode](https://leetcode.com/problems/delete-columns-to-make-sorted-ii) | [solution](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/solution/)


-----------

<p>We are given an array&nbsp;<code>A</code> of <code>N</code> lowercase letter strings, all of the same length.</p>

<p>Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.</p>

<p>For example, if we have an array <code>A = [&quot;abcdef&quot;,&quot;uvwxyz&quot;]</code> and deletion indices <code>{0, 2, 3}</code>, then the final array after deletions is <code>[&quot;bef&quot;,&quot;vyz&quot;]</code>.</p>

<p>Suppose we chose a set of deletion indices <code>D</code> such that after deletions, the final array has its elements in <strong>lexicographic</strong> order (<code>A[0] &lt;= A[1] &lt;= A[2] ... &lt;= A[A.length - 1]</code>).</p>

<p>Return the minimum possible value of <code>D.length</code>.</p>

<p>&nbsp;</p>

<div>
<div>
<ol>
</ol>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;ca&quot;,&quot;bb&quot;,&quot;ac&quot;]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>
After deleting the first column, A = [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;].
Now A is in lexicographic order (ie. A[0] &lt;= A[1] &lt;= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span>[&quot;xc&quot;,&quot;yb&quot;,&quot;za&quot;]</span>
<strong>Output: </strong><span id="example-output-2">0</span>
<strong>Explanation: </strong>
A is already in lexicographic order, so we don&#39;t need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] &lt;= A[0][1] &lt;= ...)
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[&quot;zyx&quot;,&quot;wvu&quot;,&quot;tsr&quot;]</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong>
We have to delete every column.
</pre>

<p>&nbsp;</p>

<div>
<div>
<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 100</code></li>
</ol>
</div>
</div>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Greedy

**Intuition**

Instead of thinking about column deletions, let's think about which columns we will keep in the final answer.

If the first column isn't lexicographically sorted, we have to delete it.

Otherwise, we will argue that we can keep this first column without consequence.  There are two cases:

* If we don't keep the first column, then the final rows of the answer all have to be sorted.

* If we do keep the first column, then the final rows of the answer (minus the first column) only have to be sorted if they share the same first letter (coming from the first column).

  The above statement is hard to digest, so let's use an example:

  Say we have `A = ["axx","ayy","baa","bbb","bcc"]`.  When we keep the first column, the final rows are `R = ["xx","yy","aa","bb","cc"]`, and instead of the requirement that these all have to be sorted (ie. `R[0] <= R[1] <= R[2] <= R[3] <= R[4]`), we have a weaker requirement that they only have to be sorted if they share the same first letter of the first column, (ie. `R[0] <= R[1] and R[2] <= R[3] <= R[4]`).

Now, we applied this argument only for the first column, but it actually works for every column we could consider taking.  If we can't take a column, we have to delete it.  Otherwise, we take it because it can only make adding subsequent columns easier.

**Algorithm**

All our effort has led us to a simple algorithmic idea.

Start with no columns kept.  For each column, if we could keep it and have a valid answer, keep it - otherwise delete it.


<iframe src="https://leetcode.com/playground/VebVmQZ4/shared" frameBorder="0" width="100%" height="500" name="VebVmQZ4"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(NW^2)$$, where $$N$$ is the length of `A`, and $$W$$ is the length of `A[i]`.

* Space Complexity:  $$O(NW)$$.
<br />
<br />


---
#### Approach 2: Greedy with Optimizations

**Explanation**

It is also possible to implement the solution in *Approach 1* without using as much time and space.

The key idea is that we will record the "cuts" that each column makes.  In our first example from *Approach 1* with `A = ["axx","ayy","baa","bbb","bcc"]` (and `R` defined as in Approach 1), the first column cuts our condition from `R[0] <= R[1] <= R[2] <= R[3] <= R[4]` to `R[0] <= R[1]` and `R[2] <= R[3] <= R[4]`.  That is, the boundary `"a" == column[1] != column[2] == "b"` has 'cut' one of the conditions for `R` out.

At a high level, our algorithm depends on evaluating whether adding a new column will keep all the rows sorted.  By maintaining information about these cuts, we only need to compare characters in the newest column.


<iframe src="https://leetcode.com/playground/bbGofp6M/shared" frameBorder="0" width="100%" height="500" name="bbGofp6M"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(NW)$$, where $$N$$ is the length of `A`, and $$W$$ is the length of `A[i]`.

* Space Complexity:  $$O(N)$$ in additional space complexity.  (In Python, `zip(*A)` uses $$O(NW)$$ space.)
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
