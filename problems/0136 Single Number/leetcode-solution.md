# 0136 - Single Number

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table, Bit Manipulation | [Leetcode](https://leetcode.com/problems/single-number) | [solution](https://leetcode.com/problems/single-number/solution/)


-----------

<p>Given a <strong>non-empty</strong>&nbsp;array of integers, every element appears <em>twice</em> except for one. Find that single one.</p>

<p><strong>Note:</strong></p>

<p>Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,2,1]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,1,2,1,2]
<strong>Output:</strong> 4
</pre>


-----------


## Similar Problems

- [Medium] [Single Number II](single-number-ii)

- [Medium] [Single Number III](single-number-iii)

- [Easy] [Missing Number](missing-number)

- [Medium] [Find the Duplicate Number](find-the-duplicate-number)

- [Easy] [Find the Difference](find-the-difference)




## Solution:

[TOC]

## Solution

---

#### Approach 1: List operation

**Algorithm**

1. Iterate over all the elements in $$\text{nums}$$
2. If some number in $$\text{nums}$$ is new to array, append it
3. If some number is already in the array, remove it

<iframe src="https://leetcode.com/playground/bCj3rwUg/shared" frameBorder="0" width="100%" height="276" name="bCj3rwUg"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. We iterate through $$\text{nums}$$, taking $$O(n)$$ time. We search the whole list to find whether there is duplicate number, taking $$O(n)$$ time. Because search is in the `for` loop, so we have to multiply both time complexities which is $$O(n^2)$$.

* Space complexity : $$O(n)$$.  We need a list of size $$n$$ to contain elements in $$\text{nums}$$.
<br />
<br />
---
#### Approach 2: Hash Table

**Algorithm**

We use hash table to avoid the $$O(n)$$ time required for searching the elements.

1. Iterate through all elements in $$\text{nums}$$
2. Try if $$hash\_table$$ has the key for `pop`
3. If not, set up key/value pair
4. In the end, there is only one element in $$hash\_table$$, so use `popitem` to get it

<iframe src="https://leetcode.com/playground/ebzkQT6R/shared" frameBorder="0" width="100%" height="276" name="ebzkQT6R"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n \cdot 1) = O(n)$$.  Time complexity of `for` loop is $$O(n)$$. Time complexity of hash table(dictionary in python) operation `pop` is $$O(1)$$.

* Space complexity : $$O(n)$$. The space required by $$hash\_table$$ is equal to the number of elements in $$\text{nums}$$.
<br />
<br />
---
#### Approach 3: Math

**Concept**

$$2 * (a + b + c) - (a + a + b + b + c) = c$$

<iframe src="https://leetcode.com/playground/hQwrqahc/shared" frameBorder="0" width="100%" height="174" name="hQwrqahc"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n + n) = O(n)$$. `sum` will call `next` to iterate through $$\text{nums}$$.
We can see it as `sum(list(i, for i in nums))` which means the time complexity is $$O(n)$$ because of the number of elements($$n$$) in $$\text{nums}$$.

* Space complexity : $$O(n + n) = O(n)$$. `set` needs space for the elements in `nums`
<br />
<br />
---
#### Approach 4: Bit Manipulation

**Concept**

- If we take XOR of zero and some bit, it will return that bit
    - $$a \oplus 0 = a$$
- If we take XOR of two same bits, it will return 0
    - $$a \oplus a = 0$$
- $$a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b$$

So we can XOR all bits together to find the unique number.

<iframe src="https://leetcode.com/playground/3TAX3mmj/shared" frameBorder="0" width="100%" height="225" name="3TAX3mmj"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$.  We only iterate through $$\text{nums}$$, so the time complexity is the number of elements in $$\text{nums}$$.

* Space complexity : $$O(1)$$.
