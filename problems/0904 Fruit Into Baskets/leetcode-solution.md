# 0904 - Fruit Into Baskets

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers | [Leetcode](https://leetcode.com/problems/fruit-into-baskets) | [solution](https://leetcode.com/problems/fruit-into-baskets/solution/)


-----------

<p>In a row of trees, the <code>i</code>-th tree&nbsp;produces&nbsp;fruit with type&nbsp;<code>tree[i]</code>.</p>

<p>You <strong>start at any tree&nbsp;of your choice</strong>, then repeatedly perform the following steps:</p>

<ol>
	<li>Add one piece of fruit from this tree to your baskets.&nbsp; If you cannot, stop.</li>
	<li>Move to the next tree to the right of the current tree.&nbsp; If there is no tree to the right, stop.</li>
</ol>

<p>Note that you do not have any choice after the initial choice of starting tree:&nbsp;you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.</p>

<p>You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.</p>

<p>What is the total amount of fruit you can collect with this procedure?</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,1]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong><span>Explanation: </span></strong><span>We can collect [1,2,1].</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,1,2,2]</span>
<strong>Output: </strong><span id="example-output-2">3
</span><strong><span>Explanation: </span></strong><span>We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,2,3,2,2]</span>
<strong>Output: </strong><span id="example-output-3">4
</span><strong><span>Explanation: </span></strong><span>We can collect [2,3,2,2].</span>
<span>If we started at the first tree, we would only collect [1, 2].</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,3,3,1,2,1,1,2,3,3,4]</span>
<strong>Output: </strong>5<span id="example-output-4">
</span><strong><span>Explanation: </span></strong><span>We can collect [1,2,1,1,2].</span>
<span>If we started at the first tree or the eighth tree, we would only collect 4 fruits.</span>
</pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= tree.length &lt;= 40000</code></li>
	<li><code>0 &lt;= tree[i] &lt; tree.length</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Scan Through Blocks

**Intuition**

Equivalently, we want the longest subarray with at most two "types" (values of `tree[i]`).

Instead of considering each element individually, we can consider blocks of adjacent elements of the same type.

For example, instead of `tree = [1, 1, 1, 1, 2, 2, 3, 3, 3]`, we can say this is `blocks = [(1, weight = 4), (2, weight = 2), (3, weight = 3)]`.

Now say we brute forced, scanning from left to right.  We'll have something like `blocks = [1, _2_, 1, 2, 1, 2, _1_, 3, ...]` (with various weights).

The key insight is that when we encounter a `3`, we do not need to start from the second element `2` (marked `_2_` for convenience); we can start from the first element (`_1_`) before the `3`.  This is because if we started two or more elements before, the sequence must have types `1` and `2`, and that sequence is going to end at the `3`, and thus be shorter than anything we've already considered.

Since every starting point (that is the left-most index of a block) was considered, this solution is correct.

**Algorithm**

As the notation and strategy around implementing this differs between Python and Java, please see the inline comments for more details.

<iframe src="https://leetcode.com/playground/pvsyyXLb/shared" frameBorder="0" width="100%" height="500" name="pvsyyXLb"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `tree`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Sliding Window

**Intuition**

As in *Approach 1*, we want the longest subarray with at most two different "types" (values of `tree[i]`).  Call these subarrays *valid*.

Say we consider all valid subarrays that end at index `j`.  There must be one with the smallest possible starting index `i`: lets say `opt(j) = i`.

Now the key idea is that `opt(j)` is a monotone increasing function.  This is because any subarray of a valid subarray is valid.

**Algorithm**

Let's perform a sliding window, keeping the loop invariant that `i` will be the smallest index for which `[i, j]` is a valid subarray.

We'll maintain `count`, the count of all the elements in the subarray.  This allows us to quickly query whether there are 3 types in the subarray or not.

<iframe src="https://leetcode.com/playground/tZWTV9pU/shared" frameBorder="0" width="100%" height="500" name="tZWTV9pU"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `tree`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---

Analysis written by: [@awice](https://leetcode.com/awice).
