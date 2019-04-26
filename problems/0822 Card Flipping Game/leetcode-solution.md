# 0822 - Card Flipping Game

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/card-flipping-game) | [solution](https://leetcode.com/problems/card-flipping-game/solution/)


-----------

<p>On a table are <code>N</code> cards, with a positive integer printed on the front and back of each card (possibly different).</p>

<p>We flip any number of cards, and after we choose one&nbsp;card.&nbsp;</p>

<p>If the number <code>X</code> on the back of the chosen&nbsp;card is not on the front of any card, then this number X is good.</p>

<p>What is the smallest number that is good?&nbsp; If no number is good, output <code>0</code>.</p>

<p>Here, <code>fronts[i]</code> and <code>backs[i]</code> represent the number on the front and back of card <code>i</code>.&nbsp;</p>

<p>A&nbsp;flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
<strong>Output:</strong> <code>2</code>
<strong>Explanation:</strong> If we flip the second card, the fronts are <code>[1,3,4,4,7]</code> and the backs are <code>[1,2,4,1,3]</code>.
We choose the second card, which has number 2 on the back, and it isn&#39;t on the front of any card, so <code>2</code> is good.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= fronts.length == backs.length&nbsp;&lt;=&nbsp;1000</code>.</li>
	<li><code>1 &lt;=&nbsp;fronts[i]&nbsp;&lt;= 2000</code>.</li>
	<li><code>1 &lt;= backs[i]&nbsp;&lt;= 2000</code>.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Hash Set [Accepted]

**Intuition**

If a card has the same value `x` on the front and back, it is impossible to win with `x`.  Otherwise, it has two different values, and if we win with `x`, we can put `x` face down on the rest of the cards.

**Algorithm**

Remember all values `same` that occur twice on a single card.  Then for every value `x` on any card that isn't in `same`, `x` is a candidate answer.  If we have no candidate answers, the final answer is zero.

<iframe src="https://leetcode.com/playground/DvJ47nbA/shared" frameBorder="0" width="100%" height="378" name="DvJ47nbA"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `fronts` (and `backs`).  We scan through the arrays.

* Space Complexity: $$O(N)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
