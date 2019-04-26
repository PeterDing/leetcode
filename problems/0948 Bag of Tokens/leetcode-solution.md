# 0948 - Bag of Tokens

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Greedy | [Leetcode](https://leetcode.com/problems/bag-of-tokens) | [solution](https://leetcode.com/problems/bag-of-tokens/solution/)


-----------

<p>You have an initial power <code>P</code>, an initial score of <code>0</code> points, and a bag of tokens.</p>

<p>Each token can be used at most once, has a value <code>token[i]</code>, and has potentially two ways to use it.</p>

<ul>
	<li>If we have at least <code>token[i]</code> power, we may play the token face up, losing <code>token[i]</code> power, and gaining <code>1</code> point.</li>
	<li>If we have at least <code>1</code> point, we may play the token face down, gaining <code>token[i]</code> power, and losing <code>1</code> point.</li>
</ul>

<p>Return the largest number of points we can have after playing any number of tokens.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>tokens = <span id="example-input-1-1">[100]</span>, P = <span id="example-input-1-2">50</span>
<strong>Output: </strong><span id="example-output-1">0</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>tokens = <span id="example-input-2-1">[100,200]</span>, P = <span id="example-input-2-2">150</span>
<strong>Output: </strong><span id="example-output-2">1</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>tokens = <span id="example-input-3-1">[100,200,300,400]</span>, P = <span id="example-input-3-2">200</span>
<strong>Output: </strong><span id="example-output-3">2</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>tokens.length &lt;= 1000</code></li>
	<li><code>0 &lt;= tokens[i] &lt; 10000</code></li>
	<li><code>0 &lt;= P &lt; 10000</code></li>
</ol>
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

If we play a token face up, we might as well play the one with the smallest value.  Similarly, if we play a token face down, we might as well play the one with the largest value.

**Algorithm**

We don't need to play anything until absolutely necessary.  Let's play tokens face up until we can't, then play a token face down and continue.

We must be careful, as it is easy for our implementation to be incorrect if we do not handle corner cases correctly.  We should always play tokens face up until exhaustion, then play one token face down and continue.

Our loop must be constructed with the right termination condition: we can either play a token face up or face down.

Our final answer could be any of the intermediate answers we got after playing tokens face up (but before playing them face down.)

<iframe src="https://leetcode.com/playground/FarrjFkE/shared" frameBorder="0" width="100%" height="412" name="FarrjFkE"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `tokens`.

* Space Complexity:  $$O(N)$$. 
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
