# 0031 - Next Permutation

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/next-permutation) | [solution](https://leetcode.com/problems/next-permutation/solution/)


-----------

<p>Implement <strong>next permutation</strong>, which rearranges numbers into the lexicographically next greater permutation of numbers.</p>

<p>If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).</p>

<p>The replacement must be <strong><a href="http://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> and use only constant&nbsp;extra memory.</p>

<p>Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.</p>

<p><code>1,2,3</code> &rarr; <code>1,3,2</code><br />
<code>3,2,1</code> &rarr; <code>1,2,3</code><br />
<code>1,1,5</code> &rarr; <code>1,5,1</code></p>


-----------


## Similar Problems

- [Medium] [Permutations](permutations)

- [Medium] [Permutations II](permutations-ii)

- [Medium] [Permutation Sequence](permutation-sequence)

- [Medium] [Palindrome Permutation II](palindrome-permutation-ii)




## Solution:

[TOC]

## Summary

We need to find the next lexicographic permutation of the given list of numbers than the number formed by the given array.

## Solution

---
#### Approach 1: Brute Force

**Algorithm**

In this approach, we find out every possible permutation of list formed by the elements of the given array and find out the permutation which is
just larger than the given one. But this one will be a very naive approach, since it requires us to find out every possible permutation
 which will take really long time and the implementation is complex.
 Thus, this approach is not acceptable at all. Hence, we move on directly to the correct approach.

**Complexity Analysis**

* Time complexity : $$O(n!)$$. Total possible permutations is $$n!$$.
* Space complexity : $$O(n)$$. Since an array will be used to store the permutations.
<br />
<br />
---
#### Approach 2: Single Pass Approach

**Algorithm**

First, we observe that for any given sequence that is in descending order, no next larger permutation is possible.
 For example, no next permutation is possible for the following array:
 ```
 [9, 5, 4, 3, 1]
 ```

We need to find the first pair of two successive numbers $$a[i]$$ and $$a[i-1]$$, from the right, which satisfy
 $$a[i] > a[i-1]$$. Now, no rearrangements to the right of $$a[i-1]$$ can create a larger permutation since that subarray consists of numbers in descending order.
 Thus, we need to rearrange the numbers to the right of $$a[i-1]$$ including itself.

Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. Therefore, we need to replace the number $$a[i-1]$$ with the number which is just larger than itself among the numbers lying to its right section, say $$a[j]$$.

![ Next Permutation ](https://leetcode.com/media/original_images/31_nums_graph.png)

We swap the numbers $$a[i-1]$$ and $$a[j]$$. We now have the correct number at index $$i-1$$. But still the current permutation isn't the permutation
    that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of $$a[i-1]$$. Therefore, we need to place those
     numbers in ascending order to get their smallest permutation.

But, recall that while scanning the numbers from the right, we simply kept decrementing the index
      until we found the pair $$a[i]$$ and $$a[i-1]$$ where,  $$a[i] > a[i-1]$$. Thus, all numbers to the right of $$a[i-1]$$ were already sorted in descending order.
      Furthermore, swapping $$a[i-1]$$ and $$a[j]$$ didn't change that order.
      Therefore, we simply need to reverse the numbers following $$a[i-1]$$ to get the next smallest lexicographic permutation.

The following animation will make things clearer:

![Next Permutation](https://leetcode.com/media/original_images/31_Next_Permutation.gif)

<iframe src="https://leetcode.com/playground/tJPs3ERV/shared" frameBorder="0" width="100%" height="500" name="tJPs3ERV"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. In worst case, only two scans of the whole array are needed.

* Space complexity : $$O(1)$$. No extra space is used. In place replacements are done.
