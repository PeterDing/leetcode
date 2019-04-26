# 0667 - Beautiful Arrangement II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/beautiful-arrangement-ii) | [solution](https://leetcode.com/problems/beautiful-arrangement-ii/solution/)


-----------

<p>
Given two integers <code>n</code> and <code>k</code>, you need to construct a list which contains <code>n</code> different positive integers ranging from <code>1</code> to <code>n</code> and obeys the following requirement: <br/>

Suppose this list is [a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ... , a<sub>n</sub>], then the list [|a<sub>1</sub> - a<sub>2</sub>|, |a<sub>2</sub> - a<sub>3</sub>|, |a<sub>3</sub> - a<sub>4</sub>|, ... , |a<sub>n-1</sub> - a<sub>n</sub>|] has exactly <code>k</code> distinct integers.
</p>

<p>
If there are multiple answers, print any of them.
</p>

<p><b>Example 1:</b><br/>
<pre>
<b>Input:</b> n = 3, k = 1
<b>Output:</b> [1, 2, 3]
<b>Explanation:</b> The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> n = 3, k = 2
<b>Output:</b> [1, 3, 2]
<b>Explanation:</b> The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The <code>n</code> and <code>k</code> are in the range 1 <= k < n <= 10<sup>4</sup>.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Beautiful Arrangement](beautiful-arrangement)




## Solution:

[TOC]

## Solution

---
#### Approach #1: Brute Force [Time Limit Exceeded]

**Intuition**

For each permutation of $$\text{[1, 2, ..., n]}$$, let's look at the set of differences of the adjacent elements.

**Algorithm**

For each permutation, we find the number of unique differences of adjacent elements.  If it is the desired number, we'll return that permutation.

To enumerate each permutation without using library functions, we use a recursive algorithm, where `permute` is responsible for permuting the indexes of $$\text{nums}$$ in the interval $$\text{[start, nums.length)}$$.

<iframe src="https://leetcode.com/playground/JvKeuMXb/shared" frameBorder="0" name="JvKeuMXb" width="100%" height="515"></iframe>
**Complexity Analysis**

* Time Complexity: $$O(n!)$$ to generate every permutation in the outer loop, then $$O(n)$$ work to check differences.  In total taking $$O(n* n!)$$ time.

* Space Complexity:  $$O(n)$$.  We use $$\text{seen}$$ to store whether we've seen the differences, and each generated permutation has a length equal to $$\text{n}$$.

---
#### Approach #2: Construction [Accepted]

**Intuition**

When $$\text{k = n-1}$$, a valid construction is $$\text{[1, n, 2, n-1, 3, n-2, ....]}$$. One way to see this is, we need to have a difference of $$\text{n-1}$$, which means we need $$\text{1}$$ and $$\text{n}$$ adjacent; then, we need a difference of $$\text{n-2}$$, etc.

Also, when $$\text{k = 1}$$, a valid construction is $$\text{[1, 2, 3, ..., n]}$$. So we have a construction when $$\text{n-k}$$ is tiny, and when it is large.  This leads to the idea that we can stitch together these two constructions:  we can put $$\text{[1, 2, ..., n-k-1]}$$ first so that $$\text{n}$$ is effectively $$\text{k+1}$$, and then finish the construction with the first $$\text{"k = n-1"}$$ method.

For example, when $$\text{n = 6}$$ and $$\text{k = 3}$$, we will construct the array as $$\text{[1, 2, 3, 6, 4, 5]}$$.  This consists of two parts: a construction of $$\text{[1, 2]}$$ and a construction of $$\text{[1, 4, 2, 3]}$$ where every element had $$\text{2}$$ added to it (i.e. $$\text{[3, 6, 4, 5]}$$).

**Algorithm**

As before, write $$\text{[1, 2, ..., n-k-1]}$$ first.  The remaining $$\text{k+1}$$ elements to be written are $$\text{[n-k, n-k+1, ..., n]}$$, and we'll write them in alternating head and tail order.

When we are writing the $$i^{th}$$ element from the remaining $$\text{k+1}$$, every even $$i$$ is going to be chosen from the head, and will have value $$\text{n-k + i//2}$$.  Every odd $$i$$ is going to be chosen from the tail, and will have value $$\text{n - i//2}$$.

<iframe src="https://leetcode.com/playground/knXdznYV/shared" frameBorder="0" name="knXdznYV" width="100%" height="275"></iframe>
**Complexity Analysis**

* Time Complexity: $$O(n)$$.  We are making a list of size $$\text{n}$$.

* Space Complexity:  $$O(n)$$.  Our answer has a length equal to $$\text{n}$$.

---
Analysis written by: [@awice](https://leetcode.com/awice)
