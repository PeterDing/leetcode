# 0746 - Min Cost Climbing Stairs

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Dynamic Programming | [Leetcode](https://leetcode.com/problems/min-cost-climbing-stairs) | [solution](https://leetcode.com/problems/min-cost-climbing-stairs/solution/)


-----------

<p>
On a staircase, the <code>i</code>-th step has some non-negative cost <code>cost[i]</code> assigned (0 indexed).
</p><p>
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> cost = [10, 15, 20]
<b>Output:</b> 15
<b>Explanation:</b> Cheapest is start on cost[1], pay that cost and go to the top.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
<b>Output:</b> 6
<b>Explanation:</b> Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>cost</code> will have a length in the range <code>[2, 1000]</code>.</li>
<li>Every <code>cost[i]</code> will be an integer in the range <code>[0, 999]</code>.</li>
</ol>
</p>

-----------


## Similar Problems

- [Easy] [Climbing Stairs](climbing-stairs)




## Solution:

[TOC]

#### Approach #1: Dynamic Programming [Accepted]

**Intuition**

There is a clear recursion available: the final cost `f[i]` to climb the staircase from some step `i` is `f[i] = cost[i] + min(f[i+1], f[i+2])`.  This motivates *dynamic programming*.

**Algorithm**

Let's evaluate `f` backwards in order.  That way, when we are deciding what `f[i]` will be, we've already figured out `f[i+1]` and `f[i+2]`.

We can do even better than that.  At the `i`-th step, let `f1, f2` be the old value of `f[i+1]`, `f[i+2]`, and update them to be the new values `f[i], f[i+1]`.  We keep these updated as we iterate through `i` backwards.  At the end, we want `min(f1, f2)`.

<iframe src="https://leetcode.com/playground/R8h7KgV3/shared" frameBorder="0" width="100%" height="242" name="R8h7KgV3"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the length of `cost`.

* Space Complexity: $$O(1)$$, the space used by `f1, f2`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
