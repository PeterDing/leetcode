# 0946 - Validate Stack Sequences

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Stack | [Leetcode](https://leetcode.com/problems/validate-stack-sequences) | [solution](https://leetcode.com/problems/validate-stack-sequences/solution/)


-----------

<p>Given two sequences <code>pushed</code> and <code>popped</code>&nbsp;<strong>with distinct values</strong>,&nbsp;return <code>true</code> if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>pushed = <span id="example-input-1-1">[1,2,3,4,5]</span>, popped = <span id="example-input-1-2">[4,5,3,2,1]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -&gt; 4,
push(5), pop() -&gt; 5, pop() -&gt; 3, pop() -&gt; 2, pop() -&gt; 1
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>pushed = <span id="example-input-2-1">[1,2,3,4,5]</span>, popped = <span id="example-input-2-2">[4,3,5,1,2]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>1 cannot be popped before 2.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= pushed.length == popped.length &lt;= 1000</code></li>
	<li><code>0 &lt;= pushed[i], popped[i] &lt; 1000</code></li>
	<li><code>pushed</code> is a permutation of <code>popped</code>.</li>
	<li><code>pushed</code> and <code>popped</code> have distinct values.</li>
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

We have to push the items in order, so when do we pop them?

If the stack has say, `2` at the top, then if we have to pop that value next, we must do it now.  That's because any subsequent push will make the top of the stack different from `2`, and we will never be able to pop again.

**Algorithm**

For each value, push it to the stack.

Then, greedily pop values from the stack if they are the next values to pop.

At the end, we check if we have popped all the values successfully.

<iframe src="https://leetcode.com/playground/3SkVeyqy/shared" frameBorder="0" width="100%" height="344" name="3SkVeyqy"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `pushed` and `popped`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
