# 0943 - Find the Shortest Superstring

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/find-the-shortest-superstring) | [solution](https://leetcode.com/problems/find-the-shortest-superstring/solution/)


-----------

<p>Given an array A of strings, find any&nbsp;smallest string that contains each string in <code>A</code> as a&nbsp;substring.</p>

<p>We may assume that no string in <code>A</code> is substring of another string in <code>A</code>.</p>

<div>&nbsp;</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot;]</span>
<strong>Output: </strong><span id="example-output-1">&quot;alexlovesleetcode&quot;</span>
<strong>Explanation: </strong>All permutations of &quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot; would also be accepted.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;catg&quot;,&quot;ctaagt&quot;,&quot;gcta&quot;,&quot;ttca&quot;,&quot;atgcatc&quot;]</span>
<strong>Output: </strong><span id="example-output-2">&quot;gctaagttcatgcatc&quot;</span></pre>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 12</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 20</code></li>
</ol>

<div>
<div>&nbsp;</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

We have to put the words into a row, where each word may overlap the previous word.  This is because no word is contained in any word.

Also, it is sufficient to try to maximize the total overlap of the words.

Say we have put some words down in our row, ending with word `A[i]`.  Now say we put down word `A[j]` as the next word, where word `j` hasn't been put down yet.  The overlap increases by `overlap(A[i], A[j])`.

We can use dynamic programming to leverage this recursion.  Let `dp(mask, i)` be the total overlap after putting some words down (represented by a bitmask `mask`), for which `A[i]` was the last word put down.  Then, the key recursion is `dp(mask ^ (1<<j), j) = max(overlap(A[i], A[j]) + dp(mask, i))`, where the `j`th bit is not set in mask, and `i` ranges over all bits set in `mask`.

Of course, this only tells us what the maximum overlap is for each set of words.  We also need to remember each choice along the way (ie. the specific `i` that made `dp(mask ^ (1<<j), j)` achieve a minimum) so that we can reconstruct the answer.

**Algorithm**

Our algorithm has 3 main components:

* Precompute `overlap(A[i], A[j])` for all possible `i, j`.
* Calculate `dp[mask][i]`, keeping track of the "`parent`" `i` for each `j` as described above.
* Reconstruct the answer using `parent` information.

Please see the implementation for more details about each section.

<iframe src="https://leetcode.com/playground/bMRiuMrv/shared" frameBorder="0" width="100%" height="500" name="bMRiuMrv"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2 (2^N + W))$$, where $$N$$ is the number of words, and $$W$$ is the maximum length of each word.

* Space Complexity:  $$O(N (2^N + W))$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
