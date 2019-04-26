# 0001 - Two Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Hash Table | [Leetcode](https://leetcode.com/problems/two-sum) | [solution](https://leetcode.com/problems/two-sum/solution/)


-----------

<p>Given an array of integers, return <strong>indices</strong> of the two numbers such that they add up to a specific target.</p>

<p>You may assume that each input would have <strong><em>exactly</em></strong> one solution, and you may not use the <em>same</em> element twice.</p>

<p><strong>Example:</strong></p>

<pre>
Given nums = [2, 7, 11, 15], target = 9,

Because nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9,
return [<strong>0</strong>, <strong>1</strong>].
</pre>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [3Sum](3sum)

- [Medium] [4Sum](4sum)

- [Easy] [Two Sum II - Input array is sorted](two-sum-ii-input-array-is-sorted)

- [Easy] [Two Sum III - Data structure design](two-sum-iii-data-structure-design)

- [Medium] [Subarray Sum Equals K](subarray-sum-equals-k)

- [Easy] [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Brute Force

The brute force approach is simple. Loop through each element $$x$$ and find if there is another value that equals to $$target - x$$.

<iframe src="https://leetcode.com/playground/CLZq9vzU/shared" frameBorder="0" width="100%" height="225" name="CLZq9vzU"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$.
For each element, we try to find its complement by looping through the rest of array which takes $$O(n)$$ time. Therefore, the time complexity is $$O(n^2)$$.

* Space complexity : $$O(1)$$.
<br />
<br />

---
#### Approach 2: Two-pass Hash Table

To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.

We reduce the look up time from $$O(n)$$ to $$O(1)$$ by trading space for speed. A hash table is built exactly for this purpose, it supports fast look up in *near* constant time. I say "near" because if a collision occurred, a look up could degenerate to $$O(n)$$ time. But look up in hash table should be amortized $$O(1)$$ time as long as the hash function was chosen carefully.

A simple implementation uses two iterations. In the first iteration, we add each element's value and its index to the table. Then, in the second iteration we check if each element's complement ($$target - nums[i]$$) exists in the table. Beware that the complement must not be $$nums[i]$$ itself!

<iframe src="https://leetcode.com/playground/QhqBrfm7/shared" frameBorder="0" width="100%" height="276" name="QhqBrfm7"></iframe>

**Complexity Analysis:**

* Time complexity : $$O(n)$$.
We traverse the list containing $$n$$ elements exactly twice. Since the hash table reduces the look up time to $$O(1)$$, the time complexity is $$O(n)$$.

* Space complexity : $$O(n)$$.
The extra space required depends on the number of items stored in the hash table, which stores exactly $$n$$ elements.
<br />
<br />

---
#### Approach 3: One-pass Hash Table

It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.

<iframe src="https://leetcode.com/playground/fbBQEjxv/shared" frameBorder="0" width="100%" height="242" name="fbBQEjxv"></iframe>

**Complexity Analysis:**

* Time complexity : $$O(n)$$.
We traverse the list containing $$n$$ elements only once. Each look up in the table costs only $$O(1)$$ time.

* Space complexity : $$O(n)$$.
The extra space required depends on the number of items stored in the hash table, which stores at most $$n$$ elements.
