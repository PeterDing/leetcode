# 0846 - Hand of Straights

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Ordered Map | [Leetcode](https://leetcode.com/problems/hand-of-straights) | [solution](https://leetcode.com/problems/hand-of-straights/solution/)


-----------

<p>Alice has a <code>hand</code> of cards, given as an array of integers.</p>

<p>Now she wants to rearrange the cards into groups so that each group is size <code>W</code>, and consists of <code>W</code> consecutive cards.</p>

<p>Return <code>true</code> if and only if she can.</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>hand = [1,2,3,6,2,3,4,7,8], W = 3
<strong>Output: </strong>true
<strong>Explanation:</strong> Alice&#39;s <code>hand</code> can be rearranged as <code>[1,2,3],[2,3,4],[6,7,8]</code>.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>hand = [1,2,3,4,5], W = 4
<strong>Output: </strong>false
<strong>Explanation:</strong> Alice&#39;s <code>hand</code> can&#39;t be rearranged into groups of <code>4</code>.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= hand.length &lt;= 10000</code></li>
	<li><code>0 &lt;= hand[i]&nbsp;&lt;= 10^9</code></li>
	<li><code>1 &lt;= W &lt;= hand.length</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Brute Force [Accepted]

**Intuition**

We will repeatedly try to form a group (of size W) starting with the lowest card.  This works because the lowest card still in our hand must be the bottom end of a size `W` straight.

**Algorithm**

Let's keep a count `{card: number of copies of card}` as a `TreeMap` (or `dict`).

Then, repeatedly we will do the following steps: find the lowest value card that has 1 or more copies (say with value `x`), and try to remove `x, x+1, x+2, ..., x+W-1` from our count.  If we can't, then the task is impossible.

<iframe src="https://leetcode.com/playground/VyDASsga/shared" frameBorder="0" width="100%" height="446" name="VyDASsga"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N * (N/W))$$, where $$N$$ is the length of `hand`.  The $$(N / W)$$ factor comes from `min(count)`.  In Java, the $$(N / W)$$ factor becomes $$\log N$$ due to the complexity of `TreeMap`.

* Space Complexity:  $$O(N)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
