# 0817 - Linked List Components

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Linked List | [Leetcode](https://leetcode.com/problems/linked-list-components) | [solution](https://leetcode.com/problems/linked-list-components/solution/)


-----------

<p>We are given&nbsp;<code>head</code>,&nbsp;the head node of a linked list containing&nbsp;<strong>unique integer values</strong>.</p>

<p>We are also given the list&nbsp;<code>G</code>, a subset of the values in the linked list.</p>

<p>Return the number of connected components in <code>G</code>, where two values are connected if they appear consecutively in the linked list.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
head: 0-&gt;1-&gt;2-&gt;3
G = [0, 1, 3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
head: 0-&gt;1-&gt;2-&gt;3-&gt;4
G = [0, 3, 1, 4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li>If&nbsp;<code>N</code>&nbsp;is the&nbsp;length of the linked list given by&nbsp;<code>head</code>,&nbsp;<code>1 &lt;= N &lt;= 10000</code>.</li>
	<li>The value of each node in the linked list will be in the range<code> [0, N - 1]</code>.</li>
	<li><code>1 &lt;= G.length &lt;= 10000</code>.</li>
	<li><code>G</code> is a subset of all values in the linked list.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Grouping [Accepted]

**Intuition**

Instead of thinking about connected components in `G`, think about them in the linked list.  Connected components in `G` must occur consecutively in the linked list.

**Algorithm**

Scanning through the list, if `node.val` is in `G` and `node.next.val` isn't (including if `node.next` is `null`), then this must be the end of a connected component.

For example, if the list is `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`, and `G = [0, 2, 3, 5, 7]`, then when scanning through the list, we fulfill the above condition at `0, 3, 5, 7`, for a total answer of `4`.

<iframe src="https://leetcode.com/playground/V3u2LbFe/shared" frameBorder="0" width="100%" height="361" name="V3u2LbFe"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N + G\text{.length})$$, where $$N$$ is the length of the linked list with root node `head`.

* Space Complexity: $$O(G\text{.length})$$, to store `Gset`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
