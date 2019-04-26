# 0914 - X of a Kind in a Deck of Cards

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Math | [Leetcode](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards) | [solution](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/solution/)


-----------

<p>In a deck of cards, each card has an integer written on it.</p>

<p>Return <code>true</code> if and only if you can choose&nbsp;<code>X &gt;= 2</code> such that&nbsp;it is possible to split the entire deck&nbsp;into 1 or more groups of cards, where:</p>

<ul>
	<li>Each group has exactly <code>X</code> cards.</li>
	<li>All the cards in each group have the same integer.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4,4,3,2,1]</span>
<strong>Output: </strong><span id="example-output-1">true
<strong>Explanation</strong>: Possible partition [1,1],[2,2],[3,3],[4,4]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1,2,2,2,3,3]</span>
<strong>Output: </strong><span id="example-output-2">false
</span><span id="example-output-1"><strong>Explanation</strong>: No possible partition.</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1]</span>
<strong>Output: </strong><span id="example-output-3">false
</span><span id="example-output-1"><strong>Explanation</strong>: No possible partition.</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,1]</span>
<strong>Output: </strong><span id="example-output-4">true
</span><span id="example-output-1"><strong>Explanation</strong>: Possible partition [1,1]</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[1,1,2,2,2,2]</span>
<strong>Output: </strong><span id="example-output-5">true
</span><span id="example-output-1"><strong>Explanation</strong>: Possible partition [1,1],[2,2],[2,2]</span>
</pre>
</div>
</div>
</div>
</div>

<p><br />
<strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= deck.length &lt;= 10000</code></li>
	<li><code>0 &lt;= deck[i] &lt;&nbsp;10000</code></li>
</ol>

<div>
<div>
<div>
<div>
<div>&nbsp;</div>
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
#### Approach 1: Brute Force

**Intuition**

We can try every possible `X`.  

**Algorithm**

Since we divide the deck of `N` cards into say, `K` piles of `X` cards each, we must have `N % X == 0`.

Then, say the deck has `C_i` copies of cards with number `i`.  Each group with number `i` has `X` copies, so we must have `C_i % X == 0`.  These are necessary and sufficient conditions.

<iframe src="https://leetcode.com/playground/FCdXEDEB/shared" frameBorder="0" width="100%" height="446" name="FCdXEDEB"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2 \log \log N)$$, where $$N$$ is the number of cards.  It is outside the scope of this article to prove that the number of divisors of $$N$$ is bounded by $$O(N \log \log N)$$.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Greatest Common Divisor

**Intuition and Algorithm**

Again, say there are `C_i` cards of number `i`.  These must be broken down into piles of `X` cards each, ie. `C_i % X == 0` for all `i`.

Thus, `X` must divide the greatest common divisor of `C_i`.  If this greatest common divisor `g` is greater than `1`, then `X = g` will satisfy.  Otherwise, it won't.

<iframe src="https://leetcode.com/playground/biA9HRs5/shared" frameBorder="0" width="100%" height="429" name="biA9HRs5"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log^2 N)$$, where $$N$$ is the number of votes.  If there are $$C_i$$ cards with number $$i$$, then each `gcd` operation is naively $$O(\log^2 C_i)$$.  Better bounds exist, but are outside the scope of this article to develop.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
