# 0646 - Maximum Length of Pair Chain

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/maximum-length-of-pair-chain) | [solution](https://leetcode.com/problems/maximum-length-of-pair-chain/solution/)


-----------

<p>
You are given <code>n</code> pairs of numbers. In every pair, the first number is always smaller than the second number.
</p>

<p>
Now, we define a pair <code>(c, d)</code> can follow another pair <code>(a, b)</code> if and only if <code>b < c</code>. Chain of pairs can be formed in this fashion. 
</p>

<p>
Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,2], [2,3], [3,4]]
<b>Output:</b> 2
<b>Explanation:</b> The longest chain is [1,2] -> [3,4]
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The number of given pairs will be in the range [1, 1000].</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Longest Increasing Subsequence](longest-increasing-subsequence)

- [Medium] [Increasing Subsequences](increasing-subsequences)




## Solution:

[TOC]

---
#### Approach #1: Dynamic Programming [Accepted]

**Intuition**

If a chain of length `k` ends at some `pairs[i]`, and `pairs[i][1] < pairs[j][0]`, we can extend this chain to a chain of length `k+1`.

**Algorithm**

Sort the pairs by first coordinate, and let `dp[i]` be the length of the longest chain ending at `pairs[i]`.  When `i < j` and `pairs[i][1] < pairs[j][0]`, we can extend the chain, and so we have the candidate answer `dp[j] = max(dp[j], dp[i] + 1)`.

<iframe src="https://leetcode.com/playground/5RAj49MD/shared" frameBorder="0" width="100%" height="378" name="5RAj49MD"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$ where $$N$$ is the length of `pairs`.  There are two for loops, and $$N^2$$ dominates the sorting step.

* Space Complexity: $$O(N)$$ for sorting and to store `dp`.

---
#### Approach #2: Greedy [Accepted]

**Intuition**

We can greedily add to our chain.  Choosing the next addition to be the one with the lowest second coordinate is at least better than a choice with a larger second coordinate.

**Algorithm**

Consider the pairs in increasing order of their *second* coordinate.  We'll try to add them to our chain.  If we can, by the above argument we know that it is correct to do so.

<iframe src="https://leetcode.com/playground/imd3oEYD/shared" frameBorder="0" width="100%" height="242" name="imd3oEYD"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N \log N)$$ where $$N$$ is the length of `S`.  The complexity comes from the sorting step, but the rest of the solution does linear work.

* Space Complexity: $$O(N)$$.  The additional space complexity of storing `cur` and `ans`, but sorting uses $$O(N)$$ space.  Depending on the implementation of the language used, sorting can sometimes use less space.

---

Analysis written by: [@awice](https://leetcode.com/awice).
