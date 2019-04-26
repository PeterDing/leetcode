# 0870 - Advantage Shuffle

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Greedy | [Leetcode](https://leetcode.com/problems/advantage-shuffle) | [solution](https://leetcode.com/problems/advantage-shuffle/solution/)


-----------

<p>Given two arrays <code>A</code> and <code>B</code> of equal size, the <em>advantage of <code>A</code> with respect to <code>B</code></em> is the number of indices <code>i</code>&nbsp;for which <code>A[i] &gt; B[i]</code>.</p>

<p>Return <strong>any</strong> permutation of <code>A</code> that maximizes its advantage with respect to <code>B</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[2,7,11,15]</span>, B = <span id="example-input-1-2">[1,10,4,11]</span>
<strong>Output: </strong><span id="example-output-1">[2,11,7,15]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[12,24,8,32]</span>, B = <span id="example-input-2-2">[13,25,32,11]</span>
<strong>Output: </strong><span id="example-output-2">[24,32,8,12]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length = B.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= B[i] &lt;= 10^9</code></li>
</ol>
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

If the smallest card `a` in `A` beats the smallest card `b` in `B`, we should pair them.  Otherwise, `a` is useless for our score, as it can't beat any cards.

Why should we pair `a` and `b` if `a > b`?  Because every card in `A` is larger than `b`, any card we place in front of `b` will score a point.  We might as well use the weakest card to pair with `b` as it makes the rest of the cards in `A` strictly larger, and thus have more potential to score points.

**Algorithm**

We can use the above intuition to create a greedy approach.  The current smallest card to beat in `B` will always be `b = sortedB[j]`.  For each card `a` in `sortedA`, we will either have `a` beat that card `b` (put `a` into `assigned[b]`), or throw `a` out (put `a` into `remaining`).

Afterwards, we can use our annotations `assigned` and `remaining` to reconstruct the answer.  Please see the comments for more details.


<iframe src="https://leetcode.com/playground/GJdLmnhx/shared" frameBorder="0" width="100%" height="500" name="GJdLmnhx"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A` and `B`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
