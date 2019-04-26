# 0808 - Soup Servings

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/soup-servings) | [solution](https://leetcode.com/problems/soup-servings/solution/)


-----------

<p>There are two types of soup: type A and type B. Initially we have <code>N</code> ml of each type of soup. There are four kinds of operations:</p>

<ol>
	<li>Serve&nbsp;100 ml of soup A and 0 ml of soup B</li>
	<li>Serve&nbsp;75 ml of soup A and 25&nbsp;ml of soup B</li>
	<li>Serve 50 ml of soup A and 50 ml of soup B</li>
	<li>Serve 25&nbsp;ml of soup A and 75&nbsp;ml of soup B</li>
</ol>

<p>When we serve some soup, we give it to someone and we no longer have it.&nbsp; Each turn,&nbsp;we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve&nbsp;as much as we can.&nbsp; We stop once we no longer have some quantity of both types of soup.</p>

<p>Note that we do not have the operation where all 100 ml&#39;s of soup B are used first.&nbsp;&nbsp;</p>

<p>Return the probability that soup A will be empty&nbsp;first, plus half the probability that A and B become empty at the same time.</p>

<p>&nbsp;</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> N = 50
<strong>Output:</strong> 0.625
<strong>Explanation:</strong> 
If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

</pre>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>0 &lt;= N &lt;= 10^9</code>.&nbsp;</li>
	<li>Answers within&nbsp;<code>10^-6</code>&nbsp;of the true value will be accepted as correct.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Dynamic Programming [Accepted]

**Intuition**

First, we can simplify all the numbers by dividing by 25.  More specifically, each unit is 25ml, and partial quantities of 25ml are rounded up to a full quantity.

When `N` is small, this is a relatively straightforward dynamic programming problem: we have quantities of soup represented by the state `(x, y)`, and we can either go to `(x-4, y-0)`, `(x-3, y-1)`, `(x-2, y-2)`, or `(x-1, y-3)` each with equal probability.  

When `N` is very large, this approach fails, so we need a different idea.

Instead of serving in batches of `(4, 0), (3, 1), (2, 2), (1, 3)`, pretend we serve `(1, 0)` on the side first, and then serve from the fair distribution `(3, 0), (2, 1), (1, 2), (0, 3)`.  If the pots of soup initially start at `(N, N)`, then after roughly less than `N/2` servings, one pot will still have soup.  Because of the `(1, 0)` servings on the side, this means that roughly speaking, pot `A` is used first if we serve `N/2` fairly from the first pot before `N` from the second pot.

When `N` is very large, this almost always happens (better than 99.9999%, so we can output 1), and we can check this either experimentally or mathematically.

**Algorithm**

We convert all units by dividing by 25 and rounding up.  If `N >= 500` (in new units), then by the above argument the answer is `1`.

Otherwise, we will perform a dynamic programming algorithm to find the answer.  Our Java implementation showcases a "bottom-up" approach, that fills `memo` diagonally from top left to bottom right, where `s = i + j` is the sum of the indices.  Our Python implemtation showcases a "top-down" approach that uses memoization.

<iframe src="https://leetcode.com/playground/aS5JpTPa/shared" frameBorder="0" width="100%" height="497" name="aS5JpTPa"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(1)$$.  (There exists a constant `C` such that the algorithm never performs more than `C` steps.)

* Space Complexity: $$O(1)$$.  (There exists a constant `C` such that the algorithm never uses more than `C` space.)

---

Analysis written by: [@awice](https://leetcode.com/awice).
