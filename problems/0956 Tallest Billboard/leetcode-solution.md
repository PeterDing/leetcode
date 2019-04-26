# 0956 - Tallest Billboard

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/tallest-billboard) | [solution](https://leetcode.com/problems/tallest-billboard/solution/)


-----------

<p>You are installing a billboard and want it to have the largest height.&nbsp; The billboard will have two steel supports, one on each side.&nbsp; Each steel support must be an equal height.</p>

<p>You have a collection of <code>rods</code> which can be welded together.&nbsp; For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.</p>

<p>Return the largest possible height of your billboard installation.&nbsp; If you cannot support the billboard, return 0.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,6]</span>
<strong>Output: </strong><span id="example-output-1">6</span>
<strong>Explanation:</strong> We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,3,4,5,6]</span>
<strong>Output: </strong><span id="example-output-2">10</span>
<strong>Explanation:</strong> We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
</pre>
</div>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,2]</span>
<strong>Output: </strong><span id="example-output-3">0</span>
<strong>Explanation: </strong>The billboard cannot be supported, so we return 0.
</pre>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= rods.length &lt;= 20</code></li>
	<li><code>1 &lt;= rods[i] &lt;= 1000</code></li>
	<li><code>The sum of rods is at most 5000.</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

For each rod `x`, we can write `+x`, `-x`, or `0`.  Our goal is to write `0` using the largest sum of positive terms.  For writings that have a sum of `0`, let's call the sum of the positive terms written the *score*.  For example, `+1 +2 +3 -6` has a score of `6`.

Since `sum(rods)` is bounded, it suggests to us to use that fact it in some way.  Indeed, if we already wrote some sum in the first few terms, it doesn't matter how we got it.  For example, with `rods = [1,2,2,3]`, we could arrive at a sum of `3` in 3 different ways, but the effective score is `3`.  This upper-bounds the number of states we have to consider to `10001`, as there are only this many possible sums in the interval `[-5000, 5000]`.

**Algorithm**

Let `dp[i][s]` be the largest score we can get using `rods[j]` `(j >= i)`, after previously writing a sum of `s` (that isn't included in the score).  For example, with `rods = [1,2,3,6]`, we might have `dp[1][1] = 5`, as after writing `1`, we could write `+2 +3 -6` with the remaining `rods[i:]` for a score of `5`.

In the base case, `dp[rods.length][s]` is `0` when `s == 0`, and `-infinity` everywhere else.  The recursion is `dp[i][s] = max(dp[i+1][s], dp[i+1][s-rods[i]], rods[i] + dp[i+1][s+rods[i]])`.


<iframe src="https://leetcode.com/playground/w65ZpeRa/shared" frameBorder="0" width="100%" height="480" name="w65ZpeRa"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(NS)$$, where $$N$$ is the length of `rods`, and $$S$$ is the maximum of $$\sum \text{rods}[i]$$.

* Space Complexity:  $$O(NS)$$.
<br />
<br />


---
#### Approach 2: Meet in the Middle

**Intuition**

Typically, the complexity of brute force can be reduced with a "meet in the middle" technique.  As applied to this problem, we have $$3^N$$ possible states, from writing either `+x`, `-x`, or `0` for each rod `x`, and we want to make this brute force faster.

What we can do is write the first and last $$3^{N/2}$$ states separately, and attempt to combine them.  For example, if we have rods `[1, 3, 5, 7]`, then the first two rods create up to nine states: `[0+0, 0+3, 0-3, 1+0, 1+3, 1-3, -1+0, -1+3, -1-3]`, and the last two rods also create nine states.

We will store each state as the sum of positive terms, and the sum of absolute values of the negative terms.  For example, `+1 +2 -3 -4` becomes `(3, 7)`.  Let's also call the difference `3 - 7` to be the *delta* of this state, so this state has a delta of `-4`.

Our high level goal is to combine states with deltas that sum to `0`.  The score of a state will be the sum of the positive terms, and we want the highest score.  Note that for each delta, we only care about the state that has the highest score.

**Algorithm**

Split the rods into two halves: left and right.

For each half, use brute force to compute the reachable states as defined above.  Then, for each state, record the delta and the maximum score.

Now, we have a left and right halves with `[(delta, score)]` information.  We'll find the largest total score, with total delta `0`.

<iframe src="https://leetcode.com/playground/b3NRJoz4/shared" frameBorder="0" width="100%" height="500" name="b3NRJoz4"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(3^{N/2})$$, where $$N$$ is the length of `rods`.

* Space Complexity:  $$O(3^{N/2})$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
