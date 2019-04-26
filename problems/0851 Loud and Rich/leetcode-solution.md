# 0851 - Loud and Rich

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Depth-first Search | [Leetcode](https://leetcode.com/problems/loud-and-rich) | [solution](https://leetcode.com/problems/loud-and-rich/solution/)


-----------

<p>In a group of N people (labelled <code>0, 1, 2, ..., N-1</code>), each person has different amounts of money, and different levels of quietness.</p>

<p>For convenience, we&#39;ll call the person with label <code>x</code>, simply &quot;person <code>x</code>&quot;.</p>

<p>We&#39;ll say that <code>richer[i] = [x, y]</code> if person <code>x</code>&nbsp;definitely has more money than person&nbsp;<code>y</code>.&nbsp; Note that <code>richer</code>&nbsp;may only be a subset of valid observations.</p>

<p>Also, we&#39;ll say <code>quiet[x] = q</code> if person <font face="monospace">x</font>&nbsp;has quietness <code>q</code>.</p>

<p>Now, return <code>answer</code>, where <code>answer[x] = y</code> if <code>y</code> is the least quiet person (that is, the person <code>y</code> with the smallest value of <code>quiet[y]</code>), among all people&nbsp;who definitely have&nbsp;equal to or more money than person <code>x</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>richer = <span id="example-input-1-1">[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]</span>, quiet = <span id="example-input-1-2">[3,2,5,4,6,1,7,0]</span>
<strong>Output: </strong><span id="example-output-1">[5,5,2,5,4,5,6,7]</span>
<strong>Explanation: </strong>
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn&#39;t clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
</pre>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= quiet.length = N &lt;= 500</code></li>
	<li><code>0 &lt;= quiet[i] &lt; N</code>, all <code>quiet[i]</code> are different.</li>
	<li><code>0 &lt;= richer.length &lt;= N * (N-1) / 2</code></li>
	<li><code>0 &lt;= richer[i][j] &lt; N</code></li>
	<li><code>richer[i][0] != richer[i][1]</code></li>
	<li><code>richer[i]</code>&#39;s are all different.</li>
	<li>The&nbsp;observations in <code>richer</code> are all logically consistent.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Cached Depth-First Search [Accepted]

**Intuition**

Consider the directed graph with edge `x -> y` if `y` is richer than `x`.

For each person `x`, we want the quietest person in the subtree at `x`.

**Algorithm**

Construct the graph described above, and say `dfs(person)` is the quietest person in the subtree at `person`.   Notice because the statements are logically consistent, the graph must be a DAG - a directed graph with no cycles.

Now `dfs(person)` is either `person`, or `min(dfs(child) for child in person)`.  That is to say, the quietest person in the subtree is either the `person` itself, or the quietest person in some subtree of a child of `person`.

We can cache values of `dfs(person)` as `answer[person]`, when performing our *post-order traversal* of the graph.  That way, we don't repeat work.  This technique reduces a quadratic time algorithm down to linear time.

<iframe src="https://leetcode.com/playground/uMRUYCdD/shared" frameBorder="0" width="100%" height="500" name="uMRUYCdD"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of people.

* Space Complexity:  $$O(N)$$, the space used by the `answer`, and the implicit call stack of `dfs`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
