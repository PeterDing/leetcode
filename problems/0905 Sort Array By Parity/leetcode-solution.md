# 0905 - Sort Array By Parity

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/sort-array-by-parity) | [solution](https://leetcode.com/problems/sort-array-by-parity/solution/)


-----------

<p>Given an array <code>A</code> of non-negative integers, return an array consisting of all the even elements of <code>A</code>, followed by all the odd elements of <code>A</code>.</p>

<p>You may return any answer array that satisfies this condition.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,2,4]</span>
<strong>Output: </strong><span id="example-output-1">[2,4,3,1]</span>
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 5000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 5000</code></li>
</ol>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sort

**Intuition and Algorithm**

Use a custom comparator when sorting, to sort by parity.

<iframe src="https://leetcode.com/playground/bcMSW6MA/shared" frameBorder="0" width="100%" height="412" name="bcMSW6MA"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$ for the sort, depending on the built-in implementation of `sort`.
<br />
<br />


---
#### Approach 2: Two Pass

**Intuition and Algorithm**

Write all the even elements first, then write all the odd elements.

<iframe src="https://leetcode.com/playground/uepE6ksC/shared" frameBorder="0" width="100%" height="327" name="uepE6ksC"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$ for the sort, depending on the built-in implementation of `sort`.
<br />
<br />


---
#### Approach 2: Two Pass

**Intuition and Algorithm**

Write all the even elements first, then write all the odd elements.

<iframe src="https://leetcode.com/playground/AjwfiQ8K/shared" frameBorder="0" width="100%" height="327" name="AjwfiQ8K"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$, the space used by the answer.
<br />
<br />


---
#### Approach 3: In-Place

**Intuition**

If we want to do the sort in-place, we can use quicksort, a standard textbook algorithm.

**Algorithm**

We'll maintain two pointers `i` and `j`.  The loop invariant is everything below `i` has parity `0` (ie. `A[k] % 2 == 0` when `k < i`), and everything above `j` has parity `1`.

Then, there are 4 cases for `(A[i] % 2, A[j] % 2)`:

* If it is `(0, 1)`, then everything is correct: `i++` and `j--`.

* If it is `(1, 0)`, we swap them so they are correct, then continue.

* If it is `(0, 0)`, only the `i` place is correct, so we `i++` and continue.

* If it is `(1, 1)`, only the `j` place is correct, so we `j--` and continue.

Throughout all 4 cases, the loop invariant is maintained, and `j-i` is getting smaller.  So eventually we will be done with the array sorted as desired.

<iframe src="https://leetcode.com/playground/SCAvRwWS/shared" frameBorder="0" width="100%" height="344" name="SCAvRwWS"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.  Each step of the while loop makes `j-i` decrease by at least one.  (Note that while quicksort is $$O(N \log N)$$ normally, this is $$O(N)$$ because we only need one pass to sort the elements.)

* Space Complexity:  $$O(1)$$ in additional space complexity.
<br />
<br />


---

Analysis written by: [@awice](https://leetcode.com/awice).
