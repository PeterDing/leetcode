# 0825 - Friends Of Appropriate Ages

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/friends-of-appropriate-ages) | [solution](https://leetcode.com/problems/friends-of-appropriate-ages/solution/)


-----------

<p>Some people will make friend requests. The&nbsp;list of their ages is given and&nbsp;<code>ages[i]</code>&nbsp;is the age of the&nbsp;ith person.&nbsp;</p>

<p>Person A will NOT friend request person B (B != A) if any of the following conditions are true:</p>

<ul>
	<li><code>age[B]&nbsp;&lt;= 0.5 * age[A]&nbsp;+ 7</code></li>
	<li><code>age[B]&nbsp;&gt; age[A]</code></li>
	<li><code>age[B]&nbsp;&gt; 100 &amp;&amp;&nbsp;age[A]&nbsp;&lt; 100</code></li>
</ul>

<p>Otherwise, A will friend request B.</p>

<p>Note that if&nbsp;A requests B, B does not necessarily request A.&nbsp; Also, people will not friend request themselves.</p>

<p>How many total friend requests are made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[16,16]
<strong>Output: </strong>2
<strong>Explanation: </strong>2 people friend request each other.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[16,17,18]
<strong>Output: </strong>2
<strong>Explanation: </strong>Friend requests are made 17 -&gt; 16, 18 -&gt; 17.</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>[20,30,100,110,120]
<strong>Output: </strong>
<strong>Explanation: </strong>Friend requests are made 110 -&gt; 100, 120 -&gt; 110, 120 -&gt; 100.
</pre>

<p>&nbsp;</p>

<p>Notes:</p>

<ul>
	<li><code>1 &lt;= ages.length&nbsp;&lt;= 20000</code>.</li>
	<li><code>1 &lt;= ages[i] &lt;= 120</code>.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Counting [Accepted]

**Intuition**

Instead of processing all `20000` people, we can process pairs of `(age, count)` representing how many people are that age.  Since there are only 120 possible ages, this is a much faster loop.

**Algorithm**

For each pair `(ageA, countA)`, `(ageB, countB)`, if the conditions are satisfied with respect to age, then `countA * countB` pairs of people made friend requests.

If `ageA == ageB`, then we overcounted: we should have `countA * (countA - 1)` pairs of people making friend requests instead, as you cannot friend request yourself.

<iframe src="https://leetcode.com/playground/hhWFMLmx/shared" frameBorder="0" width="100%" height="412" name="hhWFMLmx"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\mathcal{A}^2 + N)$$, where $$N$$ is the number of people, and $$\mathcal{A}$$ is the number of ages.

* Space Complexity: $$O(\mathcal{A})$$, the space used to store `count`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
