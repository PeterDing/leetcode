# 0899 - Orderly Queue

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math, String | [Leetcode](https://leetcode.com/problems/orderly-queue) | [solution](https://leetcode.com/problems/orderly-queue/solution/)


-----------

<p>A string <code>S</code> of lowercase letters is given.&nbsp; Then, we may make any number of <em>moves</em>.</p>

<p>In each move, we&nbsp;choose one&nbsp;of the first <code>K</code> letters (starting from the left), remove it,&nbsp;and place it at the end of the string.</p>

<p>Return the lexicographically smallest string we could have after any number of moves.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">&quot;cba&quot;</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">&quot;acb&quot;</span>
<strong>Explanation: </strong>
In the first move, we move the 1st character (&quot;c&quot;) to the end, obtaining the string &quot;bac&quot;.
In the second move, we move the 1st character (&quot;b&quot;) to the end, obtaining the final result &quot;acb&quot;.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">&quot;baaca&quot;</span>, K = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">&quot;aaabc&quot;</span>
<strong>Explanation: </strong>
In the first move, we move the 1st character (&quot;b&quot;) to the end, obtaining the string &quot;aacab&quot;.
In the second move, we move the 3rd character (&quot;c&quot;) to the end, obtaining the final result &quot;aaabc&quot;.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= S.length&nbsp;&lt;= 1000</code></li>
	<li><code>S</code>&nbsp;consists of lowercase letters only.</li>
</ol>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Mathematical

**Intuition**

Call the move that takes the `K`th letter from the beginning and puts it on the end, a "*`K`-kick*" move.

Examining 1-kick moves, they let us consider the string as a "necklace" that may be rotated freely, where each bead of the necklace corresponds to a letter in the string.  (Formally, this is the equivalence class under 1-kick moves.)

Examining 2-kick moves (in the context of treating the string as a necklace), they allow us to swap the positions of two adjacent beads.  Thus, with 2-kick moves, every permutation of necklace is possible.  (To actually construct the necklace, we bring the second smallest bead to be after the smallest, then the third smallest to be after the second smallest, and so on.)

The previous insight may be difficult to find.  Another strategy is to write a brute force program to examine the result of 2-kick moves - then we might notice that 2-kick moves allow any permutation of the string.

Yet another strategy might be to explicitly construct new moves based on previous moves.  If we perform a 2 kick move followed by many 1 kick moves, we can move a string like `"xyzzzzzz" -> "xzzzzzzy" -> "yxzzzzzz"`, proving we can swap the positions of any two adjacent letters.

**Algorithm**

If `K = 1`, only rotations of `S` are possible, and the answer is the smallest rotation.

If `K > 1`, any permutation of `S` is possible, and the answer is the letters of `S` written in lexicographic order.

<iframe src="https://leetcode.com/playground/DCwCw7ZJ/shared" frameBorder="0" width="100%" height="327" name="DCwCw7ZJ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N^2)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
