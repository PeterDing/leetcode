# 0945 - Minimum Increment to Make Array Unique

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/minimum-increment-to-make-array-unique) | [solution](https://leetcode.com/problems/minimum-increment-to-make-array-unique/solution/)


-----------

<p>Given an array of integers A, a <em>move</em> consists of choosing any <code>A[i]</code>, and incrementing it by <code>1</code>.</p>

<p>Return the least number of moves to make every value in <code>A</code> unique.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,2]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong> After 1 move, the array could be [1, 2, 3].
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[3,2,1,2,1,7]</span>
<strong>Output: </strong><span id="example-output-2">6</span>
<strong>Explanation: </strong> After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 40000</code></li>
	<li><code>0 &lt;= A[i] &lt; 40000</code></li>
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
#### Approach 1: Counting

**Intuition**

Let's count the quantity of each element.  Clearly, we want to increment duplicated values.

For each duplicate value, we could do a "brute force" solution of incrementing it repeatedly until it is not unique.  However, we might do a lot of work - consider the work done by an array of all ones.  We should think of how to amend our solution to solve this case as well.

What we can do instead is lazily evaluate our increments.  If for example we have `[1, 1, 1, 1, 3, 5]`, we don't need to process all the increments of duplicated `1`s.  We could take three ones (`taken = [1, 1, 1]`) and continue processing.  When we find an empty place like `2`, `4`, or `6`, we can then recover that our increment will be `2-1`, `4-1`, and `6-1`.

**Algorithm**

Count the values.  For each possible value `x`:

* If there are 2 or more values `x` in `A`, save the extra duplicated values to increment later.
* If there are 0 values `x` in `A`, then a saved value `v` gets incremented to `x`.

In Java, the code is less verbose with a slight optimization:  we record only the number of saved values, and we subtract from the answer in advance.  In the `[1, 1, 1, 1, 3, 5]` example, we do `taken = 3` and `ans -= 3` in advance, and later we do `ans += 2; ans += 4; ans += 6`.  This optimization is also used in *Approach 2*.

<iframe src="https://leetcode.com/playground/hDLTpYAB/shared" frameBorder="0" width="100%" height="412" name="hDLTpYAB"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Maintain Duplicate Info

**Intuition**

Let's imagine the array is sorted and we are moving from left to right.  As in Approach 1, we want to take duplicate values to release later.

**Algorithm**

There are two cases.

* If `A[i-1] == A[i]`, we have a duplicate to take.

* If `A[i-1] < A[i]`, we might be able to place our taken values into those free positions.  Specifically, we have `give = min(taken, A[i] - A[i-1] - 1)` possible values to release, and they will have final values `A[i-1] + 1, A[i-1] + 2, ..., A[i-1] + give`.  This has a sum of $$A[i-1] * \text{give} + (\sum_{k=1}^{give})$$.

<iframe src="https://leetcode.com/playground/P7fCXnrT/shared" frameBorder="0" width="100%" height="429" name="P7fCXnrT"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N\log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$ in additional space complexity, depending on the specific implementation of the built in sort.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
