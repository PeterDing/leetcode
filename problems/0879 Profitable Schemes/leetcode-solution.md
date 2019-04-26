# 0879 - Profitable Schemes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/profitable-schemes) | [solution](https://leetcode.com/problems/profitable-schemes/solution/)


-----------

<p>There are G people in a gang, and a list of various crimes they could commit.</p>

<p>The <code>i</code>-th crime generates a <code>profit[i]</code> and requires <code>group[i]</code> gang members to participate.</p>

<p>If a gang member participates in one crime, that member can&#39;t participate in another crime.</p>

<p>Let&#39;s call a <em>profitable&nbsp;scheme</em>&nbsp;any subset of these crimes that generates at least <code>P</code> profit, and the total number of gang members participating in that subset of crimes is at most G.</p>

<p>How many schemes can be chosen?&nbsp; Since the answer may be very&nbsp;large, <strong>return it modulo</strong> <code>10^9 + 7</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>G = <span id="example-input-1-1">5</span>, P = <span id="example-input-1-2">3</span>, group = <span id="example-input-1-3">[2,2]</span>, profit = <span id="example-input-1-4">[2,3]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>G = <span id="example-input-2-1">10</span>, P = <span id="example-input-2-2">5</span>, group = <span id="example-input-2-3">[2,3,5]</span>, profit = <span id="example-input-2-4">[6,7,8]</span>
<strong>Output: </strong><span id="example-output-2">7</span>
<strong>Explanation: </strong>
To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= G &lt;= 100</code></li>
	<li><code>0 &lt;= P &lt;= 100</code></li>
	<li><code>1 &lt;= group[i] &lt;= 100</code></li>
	<li><code>0 &lt;= profit[i] &lt;= 100</code></li>
	<li><code>1 &lt;= group.length = profit.length &lt;= 100</code></li>
</ol>

<div>
<div>&nbsp;</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

We don't care about the profit of the scheme if it is $$\geq P$$, because it surely will be over the threshold of profitability required.  Similarly, we don't care about the number of people required in the scheme if it is $$> G$$, since we know the scheme will be too big for the gang to execute.

As a result, the bounds are small enough to use dynamic programming.  Let's keep track of `cur[p][g]`, the number of schemes with profitability $$p$$ and requiring $$g$$ gang members: except we'll say (without changing the answer) that all schemes that profit *at least* `P` dollars will instead profit *exactly* `P` dollars.

**Algorithm**

Keeping track of `cur[p][g]` as defined above, let's understand how it changes as we consider 1 extra crime that will profit `p0` and require `g0` gang members.  We will put the updated counts into `cur2`.

For each possible scheme with profit `p1` and group size `g1`, that scheme plus the extra crime (`p0, g0`) being considered, has a profit of `p2 = min(p1 + p0, P)`, and uses a group size of `g2 = g1 + g0`.

<iframe src="https://leetcode.com/playground/gFHdtSWS/shared" frameBorder="0" width="100%" height="500" name="gFHdtSWS"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N * P * G)$$, where $$N$$ is the number of crimes available to the gang.

* Space Complexity:  $$O(P * G)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
