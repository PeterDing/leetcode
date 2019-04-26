# 0679 - 24 Game

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Depth-first Search | [Leetcode](https://leetcode.com/problems/24-game) | [solution](https://leetcode.com/problems/24-game/solution/)


-----------

<p>
You have 4 cards each containing a number from 1 to 9.  You need to judge whether they could operated through <code>*</code>, <code>/</code>, <code>+</code>, <code>-</code>, <code>(</code>, <code>)</code> to get the value of 24.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [4, 1, 8, 7]
<b>Output:</b> True
<b>Explanation:</b> (8-4) * (7-1) = 24
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1, 2, 1, 2]
<b>Output:</b> False
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The division operator <code>/</code> represents real division, not integer division.  For example, 4 / (1 - 2/3) = 12.</li>
<li>Every operation done is between two numbers.  In particular, we cannot use <code>-</code> as a unary operator.  For example, with <code>[1, 1, 1, 1]</code> as input, the expression <code>-1 - 1 - 1 - 1</code> is not allowed.</li>
<li>You cannot concatenate numbers together.  For example, if the input is <code>[1, 2, 1, 2]</code>, we cannot write this as 12 + 12.</li>
</ol>
</p>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

#### Approach #1: Backtracking [Accepted]

**Intuition and Algorithm**

There are only 4 cards and only 4 operations that can be performed.  Even when all operations do not commute, that gives us an upper bound of $$12 * 6 * 2 * 4 * 4 * 4 = 9216$$ possibilities, which makes it feasible to just try them all.  Specifically, we choose two numbers (with order) in 12 ways and perform one of 4 operations (12 * 4). Then, with 3 remaining numbers, we choose 2 of them and perform one of 4 operations (6 * 4).  Finally we have two numbers left and make a final choice of 2 * 4 possibilities.

We will perform 3 binary operations (`+, -, *, /` are the operations) on either our numbers or resulting numbers.  Because `-` and `/` do not commute, we must be careful to consider both `a / b` and `b / a`.

For every way to remove two numbers `a, b` in our list, and for each possible result they can make, like `a+b`, `a/b`, etc., we will recursively solve the problem on this smaller list of numbers.

<iframe src="https://leetcode.com/playground/vSR6aMjS/shared" frameBorder="0" name="vSR6aMjS" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(1)$$.  There is a hard limit of 9216 possibilities, and we do $$O(1)$$ work for each of them.

* Space Complexity: $$O(1)$$.  Our intermediate arrays are at most 4 elements, and the number made is bounded by an $$O(1)$$ factor.

---

Analysis written by: [@awice](https://leetcode.com/awice)
