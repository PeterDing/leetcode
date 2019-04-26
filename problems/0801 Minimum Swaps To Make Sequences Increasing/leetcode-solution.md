# 0801 - Minimum Swaps To Make Sequences Increasing

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing) | [solution](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/solution/)


-----------

<p>We have two integer sequences <code>A</code> and <code>B</code> of the same non-zero length.</p>

<p>We are allowed to swap elements <code>A[i]</code> and <code>B[i]</code>.&nbsp; Note that both elements are in the same index position in their respective sequences.</p>

<p>At the end of some number of swaps, <code>A</code> and <code>B</code> are both strictly increasing.&nbsp; (A sequence is <em>strictly increasing</em> if and only if <code>A[0] &lt; A[1] &lt; A[2] &lt; ... &lt; A[A.length - 1]</code>.)</p>

<p>Given A and B, return the minimum number of swaps to make both sequences strictly increasing.&nbsp; It is guaranteed that the given input always makes it possible.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> A = [1,3,5,4], B = [1,2,3,7]
<strong>Output:</strong> 1
<strong>Explanation: </strong>
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A, B</code> are arrays with the same length, and that length will be in the range <code>[1, 1000]</code>.</li>
	<li><code>A[i], B[i]</code> are integer values in the range <code>[0, 2000]</code>.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Dynamic Programming [Accepted]

**Intuition**

The cost of making both sequences increasing up to the first `i` columns can be expressed in terms of the cost of making both sequences increasing up to the first `i-1` columns.  This is because the only thing that matters to the `i`th column is whether the previous column was swapped or not.  This makes dynamic programming an ideal choice.

Let's remember `n1` (`natural1`), the cost of making the first `i-1` columns increasing and not swapping the `i-1`th column; and `s1` (`swapped1`), the cost of making the first `i-1` columns increasing and swapping the `i-1`th column.

Now we want candidates `n2` (and `s2`), the costs of making the first `i` columns increasing if we do not swap (or swap, respectively) the `i`th column.

**Algorithm**

For convenience, say `a1 = A[i-1], b1 = B[i-1]` and `a2 = A[i], b2 = B[i]`.

Now, if `a1 < a2` and `b1 < b2`, then it is allowed to have both of these columns natural (unswapped), or both of these columns swapped.  This possibility leads to `n2 = min(n2, n1)` and `s2 = min(s2, s1 + 1)`.

Another, (not exclusive) possibility is that `a1 < b2` and `b1 < a2`.  This means that it is allowed to have exactly one of these columns swapped.  This possibility leads to `n2 = min(n2, s1)` or `s2 = min(s2, n1 + 1)`.

Note that it is important to use two if statements separately, because both of the above possibilities might be possible.

At the end, the optimal solution must leave the last column either natural or swapped, so we take the minimum number of swaps between the two possibilities.


<iframe src="https://leetcode.com/playground/KT3yuKkz/shared" frameBorder="0" width="100%" height="395" name="KT3yuKkz"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$.

* Space Complexity:  $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
