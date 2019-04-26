# 0875 - Koko Eating Bananas

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Binary Search | [Leetcode](https://leetcode.com/problems/koko-eating-bananas) | [solution](https://leetcode.com/problems/koko-eating-bananas/solution/)


-----------

<p>Koko loves to eat bananas.&nbsp; There are <code>N</code>&nbsp;piles of bananas, the <code>i</code>-th&nbsp;pile has <code>piles[i]</code> bananas.&nbsp; The guards have gone and will come back in <code>H</code> hours.</p>

<p>Koko can decide her bananas-per-hour eating speed of <code>K</code>.&nbsp; Each hour, she chooses some pile of bananas, and eats K bananas from that pile.&nbsp; If the pile has less than <code>K</code> bananas, she eats all of them instead, and won&#39;t eat any more bananas during this hour.</p>

<p>Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.</p>

<p>Return the minimum integer <code>K</code> such that she can eat all the bananas within <code>H</code> hours.</p>

<p>&nbsp;</p>

<ul>
</ul>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>piles = <span id="example-input-1-1">[3,6,7,11]</span>, H = <span id="example-input-1-2">8</span>
<strong>Output: </strong><span id="example-output-1">4</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>piles = <span id="example-input-2-1">[30,11,23,4,20]</span>, H = <span id="example-input-2-2">5</span>
<strong>Output: </strong><span id="example-output-2">30</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>piles = <span id="example-input-3-1">[30,11,23,4,20]</span>, H = <span id="example-input-3-2">6</span>
<strong>Output: </strong><span id="example-output-3">23</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= piles.length &lt;= 10^4</code></li>
	<li><code>piles.length &lt;= H &lt;= 10^9</code></li>
	<li><code>1 &lt;= piles[i] &lt;= 10^9</code></li>
</ul>
</div>
</div>
</div>


-----------


## Similar Problems

- [Hard] [Minimize Max Distance to Gas Station](minimize-max-distance-to-gas-station)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Binary Search

**Intuition**

If Koko can finish eating all the bananas (within `H` hours) with an eating speed of `K`, she can finish with a larger speed too.

If we let `possible(K)` be `true` if and only if Koko can finish with an eating speed of `K`, then there is some `X` such that `possible(K) = True` if and only if `K >= X`.

For example, with `piles = [3, 6, 7, 11]` and `H = 8`, there is some `X = 4` so that `possible(1) = possible(2) = possible(3) = False`, and `possible(4) = possible(5) = ... = True`.

**Algorithm**

We can binary search on the values of `possible(K)` to find the first `X` such that `possible(X)` is `True`: that will be our answer.  Our loop invariant will be that `possible(hi)` is always `True`, and `lo` is always less than or equal to the answer.  For more information on binary search, please visit [[LeetCode Explore - Binary Search]](https://leetcode.com/explore/learn/card/binary-search/).

To find the value of `possible(K)`, (ie. whether `Koko` with an eating speed of `K` can eat all bananas in `H` hours), we simulate it.  For each pile of size `p > 0`, we can deduce that Koko finishes it in `Math.ceil(p / K) = ((p-1) // K) + 1` hours, and we add these times across all piles and compare it to `H`.


<iframe src="https://leetcode.com/playground/r7NHTXn2/shared" frameBorder="0" width="100%" height="446" name="r7NHTXn2"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log W)$$, where $$N$$ is the number of piles, and $$W$$ is the maximum size of a pile.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
