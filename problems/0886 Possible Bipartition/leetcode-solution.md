# 0886 - Possible Bipartition

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Depth-first Search | [Leetcode](https://leetcode.com/problems/possible-bipartition) | [solution](https://leetcode.com/problems/possible-bipartition/solution/)


-----------

<p>Given a set of <code>N</code>&nbsp;people (numbered <code>1, 2, ..., N</code>), we would like to split everyone into two groups of <strong>any</strong> size.</p>

<p>Each person may dislike some other people, and they should not go into the same group.&nbsp;</p>

<p>Formally, if <code>dislikes[i] = [a, b]</code>, it means it is not allowed to put the people numbered <code>a</code> and <code>b</code> into the same group.</p>

<p>Return <code>true</code>&nbsp;if and only if it is possible to split everyone into two groups in this way.</p>

<p>&nbsp;</p>

<div>
<div>
<ol>
</ol>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">4</span>, dislikes = <span id="example-input-1-2">[[1,2],[1,3],[2,4]]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation</strong>: group1 [1,4], group2 [2,3]
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">3</span>, dislikes = <span id="example-input-2-2">[[1,2],[1,3],[2,3]]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-3-1">5</span>, dislikes = <span id="example-input-3-2">[[1,2],[2,3],[3,4],[4,5],[1,5]]</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 2000</code></li>
	<li><code>0 &lt;= dislikes.length &lt;= 10000</code></li>
	<li><code>1 &lt;= dislikes[i][j] &lt;= N</code></li>
	<li><code>dislikes[i][0] &lt; dislikes[i][1]</code></li>
	<li>There does not exist <code>i != j</code> for which <code>dislikes[i] == dislikes[j]</code>.</li>
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
#### Approach 1: Depth-First Search

**Intuition**

It's natural to try to assign everyone to a group.  Let's say people in the first group are red, and people in the second group are blue.

If the first person is red, anyone disliked by this person must be blue.  Then, anyone disliked by a blue person is red, then anyone disliked by a red person is blue, and so on.

If at any point there is a conflict, the task is impossible, as every step logically follows from the first step.  If there isn't a conflict, then the coloring was valid, so the answer would be `true`.

**Algorithm**

Consider the graph on `N` people formed by the given "dislike" edges.  We want to check that each connected component of this graph is bipartite.

For each connected component, we can check whether it is bipartite by just trying to coloring it with two colors.  How to do this is as follows: color any node red, then all of it's neighbors blue, then all of those neighbors red, and so on.  If we ever color a red node blue (or a blue node red), then we've reached a conflict.

<iframe src="https://leetcode.com/playground/aD5rzLRZ/shared" frameBorder="0" width="100%" height="500" name="aD5rzLRZ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N + E)$$, where $$E$$ is the length of `dislikes`.

* Space Complexity:  $$O(N + E)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
