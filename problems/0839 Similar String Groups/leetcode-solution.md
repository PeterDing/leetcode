# 0839 - Similar String Groups

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Depth-first Search, Union Find, Graph | [Leetcode](https://leetcode.com/problems/similar-string-groups) | [solution](https://leetcode.com/problems/similar-string-groups/solution/)


-----------

<p>Two strings <code>X</code>&nbsp;and <code>Y</code>&nbsp;are similar if we can swap two letters (in different positions) of <code>X</code>, so that&nbsp;it equals <code>Y</code>.</p>

<p>For example, <code>&quot;tars&quot;</code>&nbsp;and <code>&quot;rats&quot;</code>&nbsp;are similar (swapping at positions <code>0</code> and <code>2</code>), and <code>&quot;rats&quot;</code> and <code>&quot;arts&quot;</code> are similar, but <code>&quot;star&quot;</code> is not similar to <code>&quot;tars&quot;</code>, <code>&quot;rats&quot;</code>, or <code>&quot;arts&quot;</code>.</p>

<p>Together, these form two connected groups by similarity: <code>{&quot;tars&quot;, &quot;rats&quot;, &quot;arts&quot;}</code> and <code>{&quot;star&quot;}</code>.&nbsp; Notice that <code>&quot;tars&quot;</code> and <code>&quot;arts&quot;</code> are in the same group even though they are not similar.&nbsp; Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.</p>

<p>We are given a list <code>A</code> of strings.&nbsp; Every string in <code>A</code> is an anagram of every other string in <code>A</code>.&nbsp; How many groups are there?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[&quot;tars&quot;,&quot;rats&quot;,&quot;arts&quot;,&quot;star&quot;]
<strong>Output: </strong>2</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>A.length &lt;= 2000</code></li>
	<li><code>A[i].length &lt;= 1000</code></li>
	<li><code>A.length * A[i].length &lt;= 20000</code></li>
	<li>All words in <code>A</code>&nbsp;consist of lowercase letters only.</li>
	<li>All words in <code>A</code> have the same length and are anagrams of each other.</li>
	<li>The judging time limit has been increased for this question.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Piecewise [Accepted]

**Intuition**

Let `W = A[0].length`.  It is clear that we can determine in $$O(W)$$ time, whether two words from `A` are similar.

One attempt is a standard kind of brute force: for each pair of words, let's draw an edge between these words if they are similar.  We can do this in $$O(N^2 W)$$ time.  After, finding the connected components can be done in $$O(N^2)$$ time naively (each node may have up to $$N-1$$ edges), (or $$O(N)$$ with a union-find structure.)  The total complexity is $$O(N^2 W)$$.

Another attempt is to enumerate all neighbors of a word.  A `word` has up to $$\binom{W}{2}$$ neighbors, and if that `neighbor` is itself a given word, we know that `word` and `neighbor` are connected by an edge.  In this way, we can build the graph in $$O(N W^3)$$ time, and again take $$O(N^2)$$ or $$O(N)$$ time to analyze the number of connected components.

One insight is that between these two approaches, we can choose which approach works better.  If we have very few words, we want to use the first approach; if we have very short words, we want to use the second approach.  We'll piecewise add these two approaches (with complexity $$O(N^2 W)$$ and $$O(N W^3)$$), to create an approach with $$O(NW\min(N, W^2))$$ complexity.


**Algorithm**

We will build some underlying graph with `N` nodes, where nodes `i` and `j` are connected if and only if `A[i]` is similar to `A[j]`, then look at the number of connected components.

There are a few challenges involved in this problem, but each challenge is relatively straightforward.  

* Use a helper function `similar(word1, word2)` that is `true` if and only if two given words are similar.

* Enumerate all neighbors of a word, and discover when it is equal to a given word.

* Use either a union-find structure or a depth-first search, to calculate the number of connected components of the underlying graph.  We've showcased a union-find structure in this solution, with notes of a depth-first search in the comments.

For more details, see the implementations below.

<iframe src="https://leetcode.com/playground/B2BjbwA7/shared" frameBorder="0" width="100%" height="500" name="B2BjbwA7"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(NW \min(N, W^2))$$, where $$N$$ is the length of `A`, and $$W$$ is the length of each given word.

* Space Complexity:  $$O(NW^3)$$.  If $$N < W^2$$, the space complexity is $$O(N)$$.  Otherwise, the space complexity is $$O(NW^3)$$: for each of $$NW^2$$ neighbors we store a word of length $$W$$.  (Plus, we store $$O(NW^2)$$ node indices ("buckets") which is dominated by the $$O(NW^3)$$ term.)  Because $$W^2 <= N$$ in this case, we could also write the space complexity as $$O(N^2 W)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
