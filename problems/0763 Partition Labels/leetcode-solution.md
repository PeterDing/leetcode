# 0763 - Partition Labels

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers, Greedy | [Leetcode](https://leetcode.com/problems/partition-labels) | [solution](https://leetcode.com/problems/partition-labels/solution/)


-----------

<p>
A string <code>S</code> of lowercase letters is given.  We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
</p><p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> S = "ababcbacadefegdehijhklij"
<b>Output:</b> [9,7,8]
<b>Explanation:</b>
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
</pre>
</p>

<p><b>Note:</b><br><ol>
<li><code>S</code> will have length in range <code>[1, 500]</code>.</li>
<li><code>S</code> will consist of lowercase letters (<code>'a'</code> to <code>'z'</code>) only.</li>
</ol></p>

-----------


## Similar Problems

- [Medium] [Merge Intervals](merge-intervals)




## Solution:

[TOC]

#### Approach #1: Greedy [Accepted]

**Intuition**

Let's try to repeatedly choose the smallest left-justified partition.
Consider the first label, say it's `'a'`.  The first partition must include it, and also the last occurrence of `'a'`.
However, between those two occurrences of `'a'`, there could be other labels that make the minimum size of this partition bigger.  For example, in `"abccaddbeffe"`, the minimum first partition is `"abccaddb"`. 
This gives us the idea for the algorithm:  For each letter encountered, process the last occurrence of that letter, extending the current partition `[anchor, j]` appropriately.

**Algorithm**

We need an array `last[char] -> index of S where char occurs last`.
Then, let `anchor` and `j` be the start and end of the current partition.
If we are at a label that occurs last at some index after `j`, we'll extend the partition `j = last[c]`.  If we are at the end of the partition (`i == j`) then we'll append a partition size to our answer, and set the start of our new partition to `i+1`.

<iframe src="https://leetcode.com/playground/sSLPrXHh/shared" frameBorder="0" width="100%" height="361" name="sSLPrXHh"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of $$S$$.

* Space Complexity: $$O(N)$$.

---
Analysis written by: [@awice](https://leetcode.com/awice).
