# 0670 - Maximum Swap

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Math | [Leetcode](https://leetcode.com/problems/maximum-swap) | [solution](https://leetcode.com/problems/maximum-swap/solution/)


-----------

<p>
Given a non-negative integer, you could swap two digits <b>at most</b> once to get the maximum valued number. Return the maximum valued number you could get.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 2736
<b>Output:</b> 7236
<b>Explanation:</b> Swap the number 2 and the number 7.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 9973
<b>Output:</b> 9973
<b>Explanation:</b> No swap.
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The given number is in the range [0, 10<sup>8</sup>]</li>
</ol>
</p>

-----------


## Similar Problems

- [Hard] [Create Maximum Number](create-maximum-number)




## Solution:

[TOC]

## Solution

---
#### Approach #1: Brute Force [Accepted]

**Intuition**

The number only has at most 8 digits, so there are only $${}^{8}\text{C}_{2}$$ = 28 available swaps.  We can easily brute force them all.

**Algorithm**

We will store the candidates as lists of length $$\text{len(num)}$$.  For each candidate swap with positions $$\text{(i, j)}$$, we swap the number and record if the candidate is larger than the current answer, then swap back to restore the original number.

The only detail is possibly to check that we didn't introduce a leading zero.  We don't actually need to check it, because our original number doesn't have one.

<iframe src="https://leetcode.com/playground/9BbnzEUC/shared" frameBorder="0" name="9BbnzEUC" width="100%" height="462"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^3)$$, where $$N$$ is the total number of digits in the input number.  For each pair of digits, we spend up to $$O(N)$$ time to compare the final sequences.

* Space Complexity: $$O(N)$$, the information stored in $$\text{A}$$.

---

#### Approach #2: Greedy [Accepted]

**Intuition**

At each digit of the input number in order, if there is a larger digit that occurs later, we know that the best swap must occur with the digit we are currently considering.

**Algorithm**

We will compute $$\text{last[d] = i}$$, the index $$\text{i}$$ of the last occurrence of digit $$\text{d}$$ (if it exists).

Afterwards, when scanning the number from left to right, if there is a larger digit in the future, we will swap it with the largest such digit; if there are multiple such digits, we will swap it with the one that occurs the latest.

<iframe src="https://leetcode.com/playground/c2u3L78L/shared" frameBorder="0" name="c2u3L78L" width="100%" height="411"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the total number of digits in the input number.  Every digit is considered at most once.

* Space Complexity: $$O(1)$$.  The additional space used by $$\text{last}$$ only has up to 10 values.

---
Analysis written by: [@awice](https://leetcode.com/awice)
