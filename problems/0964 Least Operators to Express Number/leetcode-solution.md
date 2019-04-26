# 0964 - Least Operators to Express Number

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math, Dynamic Programming | [Leetcode](https://leetcode.com/problems/least-operators-to-express-number) | [solution](https://leetcode.com/problems/least-operators-to-express-number/solution/)


-----------

<p>Given a single positive integer <code>x</code>, we will write an expression of the form <code>x (op1) x (op2) x (op3) x ...</code>&nbsp;where each operator <code>op1</code>, <code>op2</code>, etc. is either addition, subtraction, multiplication, or division (<code>+</code>, <code>-</code>, <code>*</code>, or <code>/)</code>.&nbsp; For example, with <code>x = 3</code>, we might write <code>3 * 3 / 3 + 3 - 3</code>&nbsp;which is a value of <font face="monospace">3</font>.</p>

<p>When writing such an expression, we adhere to the following conventions:</p>

<ol>
	<li>The division operator (<code>/</code>) returns rational numbers.</li>
	<li>There are no parentheses placed anywhere.</li>
	<li>We use the usual order of operations: multiplication and division happens before addition and subtraction.</li>
	<li>It&#39;s not allowed to use the unary negation&nbsp;operator (<code>-</code>).&nbsp; For example, &quot;<code>x&nbsp;- x</code>&quot;&nbsp;is a valid expression as it only uses subtraction, but &quot;<code>-x +&nbsp;x</code>&quot; is not because it uses negation.</li>
</ol>

<p>We would like to write an expression with the least number of operators such that the expression equals the given <code>target</code>.&nbsp; Return the least number of operators used.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>x = <span id="example-input-1-1">3</span>, target = <span id="example-input-1-2">19</span>
<strong>Output: </strong><span id="example-output-1">5</span>
<strong>Explanation: </strong><span id="example-output-1">3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.</span>
</pre>

<p><strong>Example 2:</strong></p>

<div>
<pre>
<strong>Input: </strong>x = <span id="example-input-2-1">5</span>, target = <span id="example-input-2-2">501</span>
<strong>Output: </strong><span id="example-output-2">8</span>
<strong>Explanation: </strong><span id="example-output-1">5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>x = <span id="example-input-3-1">100</span>, target = <span id="example-input-3-2">100000000</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong><span id="example-output-1">100 * 100 * 100 * 100.  The expression contains 3 operations.</span></pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ul>
	<li><code>2 &lt;= x &lt;= 100</code></li>
	<li><code>1 &lt;= target &lt;= 2 * 10^8</code></li>
</ul>

<div>
<div>
<div>&nbsp;</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

First, we notice that we can consider blocks of multiplication and division separately.  Each block is a power of `x`: either `x / x`, `x`, `x * x`, `x * x * x`, `x * x * x * x` and so on.  (There is no point to write expressions like `x * x / x` because it uses strictly more operators.)

Let's think of the cost of a block as all the operators needed to express it, including the addition or subtraction operator in front of it.  For example, we can think of `x * x + x + x / x` as `(+ x * x) (+ x) (+ x / x)` for a cost of `2 + 1 + 2`, minus 1 for the leading `+` (so the total cost is `4`).

We can write the cost of writing a block that has value $$x^e$$: it is $$e$$, except when $$e = 0$$ it is 2.  We want the sum of the costs of all blocks minus 1.

Now, we have the reduced problem: we have the costs of writing all $$x^e$$ or $$-x^e$$, and we want to find the least cost to express the target.

Notice that modulo $$x$$, the only blocks that change the expression are $$x^0$$.  Let $$r_1 = \text{target} \pmod x$$.  So we must either subtract $$r_1$$ $$x^0$$'s, or add $$x-r_1$$ $$x^0$$'s.  This will form a new "remaining" target, $$\text{target}_2$$, that is divisible by $$x$$.

Then, modulo $$x^2$$, the only blocks that change the expression are $$x^1$$ and $$x^0$$.  However, since the new target is divisible by $$x$$, there is no point to use $$x^0$$, as we would have to use at least $$x$$ of them to do the same work as one use of $$x^1$$, which is a strictly higher cost.

Again, in a similar way, we have $$r_2 = \text{target}_2 \pmod {x^2}$$, and we must either subtract $$r_2 / x$$ $$x^1$$'s, or add $$x - r_2 / x$$ $$x^1$$'s.  This will form a new remaining target $$\text{target}_3$$, and so on.

As a concrete example, say `x = 5, target = 123`.  We either add `2` or subtract `3`.  This leaves us with a target of `120` or `125`.  If the target is `120`, we can either add `5` or subtract `20`, leaving us with a target of `100` or `125`.  If the target is `100`, we can either add `25` or subtract `100`, leaving us with a target of `125` or `0`.  If the target is `125`, we subtract `125`.

**Algorithm**

Let's calculate `dp(i, target)` using a top down `dp`.  Here, `i` will be the exponent of the block $$x^i$$ being considered, and `target` will be the remaining target, already divided by $$x^i$$.

From here, the recursion is straightforward: $$r = \text{target} \pmod x$$, and we either subtract $$r$$ blocks or add $$(x-r)$$ of them.  The base cases are easily deduced - see the code for more details.

<iframe src="https://leetcode.com/playground/zS62KWLG/shared" frameBorder="0" width="100%" height="500" name="zS62KWLG"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\log_{x} \text{target})$$.  We can prove that we only visit up to two states for each base-x digit of $$\text{target}$$.

* Space Complexity:  $$O(\log \text{target})$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
