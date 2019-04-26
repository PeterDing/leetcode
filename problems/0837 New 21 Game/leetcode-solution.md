# 0837 - New 21 Game

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/new-21-game) | [solution](https://leetcode.com/problems/new-21-game/solution/)


-----------

<p>Alice plays the following game, loosely based on the card game &quot;21&quot;.</p>

<p>Alice starts with <code>0</code> points, and draws numbers while she has less than <code>K</code> points.&nbsp; During each draw, she gains an integer number of points randomly from the range <code>[1, W]</code>, where <code>W</code> is an integer.&nbsp; Each draw is independent and the outcomes have equal probabilities.</p>

<p>Alice stops drawing numbers when she gets <code>K</code> or more points.&nbsp; What is the probability&nbsp;that she has <code>N</code> or less points?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = 10, K = 1, W = 10
<strong>Output: </strong>1.00000
<strong>Explanation: </strong> Alice gets a single card, then stops.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = 6, K = 1, W = 10
<strong>Output: </strong>0.60000
<strong>Explanation: </strong> Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = 21, K = 17, W = 10
<strong>Output: </strong>0.73278</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= K &lt;= N &lt;= 10000</code></li>
	<li><code>1 &lt;= W &lt;= 10000</code></li>
	<li>Answers will be accepted as correct if they are within <code>10^-5</code> of the correct answer.</li>
	<li>The judging time limit has been reduced for this question.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Dynamic Programming [Accepted]

**Intuition**

It is clear that the probability that Alice wins the game is only related to how many points `x` she starts the next draw with, so we can try to formulate an answer in terms of `x`.

**Algorithm**

Let `f(x)` be the answer when we already have `x` points.  When she has between `K` and `N` points, then she stops drawing and wins.  If she has more than `N` points, then she loses.

The key recursion is $$f(x) = (\frac{1}{W}) * (f(x+1) + f(x+2) + ... + f(x+W))$$  This is because there is a probability of $$\frac{1}{W}$$ to draw each card from $$1$$ to $$W$$.

With this recursion, we could do a naive dynamic programming solution as follows:

```python
#psuedocode
dp[k] = 1.0 when K <= k <= N, else 0.0
# dp[x] = the answer when Alice has x points
for k from K-1 to 0:
    dp[k] = (dp[k+1] + ... + dp[k+W]) / W
return dp[0]
```

This leads to a solution with $$O(K*W + (N-K))$$ time complexity, which isn't efficient enough.  Every calculation of `dp[k]` does $$O(W)$$ work, but the work is quite similar.

Actually, the difference is $$f(x) - f(x-1) = \frac{1}{W} \big( f(x+W) - f(x) \big)$$.  This allows us to calculate subsequent $$f(k)$$'s in $$O(1)$$ time, by maintaining the numerator $$S = f(x+1) + f(x+2) + \cdots + f(x+W)$$.

As we calculate each `dp[k] = S / W`, we maintain the correct value of this numerator $$S \Rightarrow S + f(k) - f(k+W)$$.

<iframe src="https://leetcode.com/playground/x4pmytdi/shared" frameBorder="0" width="100%" height="327" name="x4pmytdi"></iframe>

**Complexity Analysis**

* Time and Space Complexity:  $$O(N + W)$$.  
Note that we can reduce the time complexity to $$O(\max(K, W))$$ and the space complexity to $$O(W)$$ by only keeping track of the last $$W$$ values of `dp`, but it isn't required.


---

Analysis written by: [@awice](https://leetcode.com/awice).
