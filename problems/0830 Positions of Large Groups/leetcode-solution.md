# 0830 - Positions of Large Groups

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/positions-of-large-groups) | [solution](https://leetcode.com/problems/positions-of-large-groups/solution/)


-----------

<p>In a string&nbsp;<code>S</code>&nbsp;of lowercase letters, these letters form consecutive groups of the same character.</p>

<p>For example, a string like <code>S = &quot;abbxxxxzyy&quot;</code> has the groups <code>&quot;a&quot;</code>, <code>&quot;bb&quot;</code>, <code>&quot;xxxx&quot;</code>, <code>&quot;z&quot;</code> and&nbsp;<code>&quot;yy&quot;</code>.</p>

<p>Call a group <em>large</em> if it has 3 or more characters.&nbsp; We would like the starting and ending positions of every large group.</p>

<p>The final answer should be in lexicographic order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;abbxxxxzzy&quot;
<strong>Output: </strong>[[3,6]]
<strong>Explanation</strong>: <code>&quot;xxxx&quot; is the single </code>large group with starting  3 and ending positions 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;abc&quot;
<strong>Output: </strong>[]
<strong>Explanation</strong>: We have &quot;a&quot;,&quot;b&quot; and &quot;c&quot; but no large group.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>&quot;abcdddeeeeaabbbcd&quot;
<strong>Output: </strong>[[3,5],[6,9],[12,14]]</pre>

<p>&nbsp;</p>

<p><strong>Note:&nbsp;</strong>&nbsp;<code>1 &lt;= S.length &lt;= 1000</code></p>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Two Pointer [Accepted]

**Intuition**

We scan through the string to identify the start and end of each group.  If the size of the group is at least 3, we add it to the answer.

**Algorithm**

Maintain pointers `i, j` with `i <= j`.  The `i` pointer will represent the start of the current group, and we will increment `j` forward until it reaches the end of the group.

We know that we have reached the end of the group when `j` is at the end of the string, or `S[j] != S[j+1]`.  At this point, we have some group `[i, j]`; and after, we will update `i = j+1`, the start of the next group.

<iframe src="https://leetcode.com/playground/m9hgNCUd/shared" frameBorder="0" width="100%" height="327" name="m9hgNCUd"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity: $$O(N)$$, the space used by the answer.

---

Analysis written by: [@awice](https://leetcode.com/awice).
