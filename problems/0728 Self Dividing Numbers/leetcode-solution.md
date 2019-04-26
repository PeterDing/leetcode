# 0728 - Self Dividing Numbers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/self-dividing-numbers) | [solution](https://leetcode.com/problems/self-dividing-numbers/solution/)


-----------

<p>
A <i>self-dividing number</i> is a number that is divisible by every digit it contains.
</p><p>
For example, 128 is a self-dividing number because <code>128 % 1 == 0</code>, <code>128 % 2 == 0</code>, and <code>128 % 8 == 0</code>.
</p><p>
Also, a self-dividing number is not allowed to contain the digit zero.
</p><p>
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
</p>
<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
left = 1, right = 22
<b>Output:</b> [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
</pre>
</p>

<p><b>Note:</b>
<li>The boundaries of each input argument are <code>1 <= left <= right <= 10000</code>.</li>
</p>

-----------


## Similar Problems

- [Easy] [Perfect Number](perfect-number)




## Solution:

[TOC]

#### Approach #1: Brute Force [Accepted]

**Intuition and Algorithm**

For each number in the given range, we will directly test if that number is self-dividing.

By definition, we want to test each whether each digit is non-zero and divides the number.  For example, with `128`, we want to test `d != 0 && 128 % d == 0` for `d = 1, 2, 8`.  To do that, we need to iterate over each digit of the number.

A straightforward approach to that problem would be to convert the number into a character array (string in Python), and then convert back to integer to perform the modulo operation when checking `n % d == 0`.

We could also continually divide the number by 10 and peek at the last digit.  That is shown as a variation in a comment.

<iframe src="https://leetcode.com/playground/6GUVmusj/shared" frameBorder="0" width="100%" height="500" name="6GUVmusj"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(D)$$, where $$D$$ is the number of integers in the range $$[L, R]$$, and assuming $$\log(R)$$ is bounded.  (In general, the complexity would be $$O(D\log R)$$.)

* Space Complexity: $$O(D)$$, the length of the answer.

---

Analysis written by: [@awice](https://leetcode.com/awice).
