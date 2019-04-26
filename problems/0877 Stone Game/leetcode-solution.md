# 0877 - Stone Game

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math, Dynamic Programming, Minimax | [Leetcode](https://leetcode.com/problems/stone-game) | [solution](https://leetcode.com/problems/stone-game/solution/)


-----------

<p>Alex and Lee play a game with piles of stones.&nbsp; There are an even number of&nbsp;piles <strong>arranged in a row</strong>, and each pile has a positive integer number of stones <code>piles[i]</code>.</p>

<p>The objective of the game is to end with the most&nbsp;stones.&nbsp; The total number of stones is odd, so there are no ties.</p>

<p>Alex and Lee take turns, with Alex starting first.&nbsp; Each turn, a player&nbsp;takes the entire pile of stones from either the beginning or the end of the row.&nbsp; This continues until there are no more piles left, at which point the person with the most stones wins.</p>

<p>Assuming Alex and Lee play optimally, return <code>True</code>&nbsp;if and only if Alex wins the game.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[5,3,4,5]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= piles.length &lt;= 500</code></li>
	<li><code>piles.length</code> is even.</li>
	<li><code>1 &lt;= piles[i] &lt;= 500</code></li>
	<li><code>sum(piles)</code> is odd.</li>
</ol>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

Let's change the game so that whenever Lee scores points, it deducts from Alex's score instead.

Let `dp(i, j)` be the largest score Alex can achieve where the piles remaining are `piles[i], piles[i+1], ..., piles[j]`.  This is natural in games with scoring: we want to know what the value of each position of the game is.

We can formulate a recursion for `dp(i, j)` in terms of `dp(i+1, j)` and `dp(i, j-1)`, and we can use dynamic programming to not repeat work in this recursion.  (This approach can output the correct answer, because the states form a DAG (directed acyclic graph).)

**Algorithm**

When the piles remaining are `piles[i], piles[i+1], ..., piles[j]`, the player who's turn it is has at most 2 moves.

The person who's turn it is can be found by comparing `j-i` to `N` modulo 2.

If the player is Alex, then she either takes `piles[i]` or `piles[j]`, increasing her score by that amount.  Afterwards, the total score is either `piles[i] + dp(i+1, j)`, or `piles[j] + dp(i, j-1)`; and we want the maximum possible score.

If the player is Lee, then he either takes `piles[i]` or `piles[j]`, decreasing Alex's score by that amount.  Afterwards, the total score is either `-piles[i] + dp(i+1, j)`, or `-piles[j] + dp(i, j-1)`; and we want the *minimum* possible score.


<iframe src="https://leetcode.com/playground/4azVgCpr/shared" frameBorder="0" width="100%" height="412" name="4azVgCpr"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the number of piles.

* Space Complexity:  $$O(N^2)$$, the space used storing the intermediate results of each subgame.
<br />
<br />


---
#### Approach 2: Mathematical

**Intuition and Algorithm**

Alex clearly always wins the 2 pile game.  With some effort, we can see that she always wins the 4 pile game.

If Alex takes the first pile initially, she can always take the third pile.  If she takes the fourth pile initially, she can always take the second pile.  At least one of `first + third, second + fourth` is larger, so she can always win.

We can extend this idea to `N` piles.  Say the first, third, fifth, seventh, etc. piles are white, and the second, fourth, sixth, eighth, etc. piles are black.  Alex can always take either all white piles or all black piles, and one of the colors must have a sum number of stones larger than the other color.

Hence, Alex always wins the game.

<iframe src="https://leetcode.com/playground/TdjR4pTJ/shared" frameBorder="0" width="100%" height="157" name="TdjR4pTJ"></iframe>

**Complexity Analysis**

* Time and Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
