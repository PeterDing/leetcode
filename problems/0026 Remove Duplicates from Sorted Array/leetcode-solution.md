# 0026 - Remove Duplicates from Sorted Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Two Pointers | [Leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | [solution](https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/)


-----------

<p>Given a sorted array <em>nums</em>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each element appear only <em>once</em> and return the new length.</p>

<p>Do not allocate extra space for another array, you must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p><strong>Example 1:</strong></p>

<pre>
Given <em>nums</em> = <strong>[1,1,2]</strong>,

Your function should return length = <strong><code>2</code></strong>, with the first two elements of <em><code>nums</code></em> being <strong><code>1</code></strong> and <strong><code>2</code></strong> respectively.

It doesn&#39;t matter what you leave beyond the returned length.</pre>

<p><strong>Example 2:</strong></p>

<pre>
Given <em>nums</em> = <strong>[0,0,1,1,1,2,2,3,3,4]</strong>,

Your function should return length = <strong><code>5</code></strong>, with the first five elements of <em><code>nums</code></em> being modified to&nbsp;<strong><code>0</code></strong>, <strong><code>1</code></strong>, <strong><code>2</code></strong>, <strong><code>3</code></strong>, and&nbsp;<strong><code>4</code></strong> respectively.

It doesn&#39;t matter what values are set beyond&nbsp;the returned length.
</pre>

<p><strong>Clarification:</strong></p>

<p>Confused why the returned value is an integer but your answer is an array?</p>

<p>Note that the input array is passed in by <strong>reference</strong>, which means modification to the input array will be known to the caller as well.</p>

<p>Internally you can think of this:</p>

<pre>
// <strong>nums</strong> is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to <strong>nums</strong> in your function would be known by the caller.
// using the length returned by your function, it prints the first <strong>len</strong> elements.
for (int i = 0; i &lt; len; i++) {
&nbsp; &nbsp; print(nums[i]);
}</pre>


-----------


## Similar Problems

- [Easy] [Remove Element](remove-element)

- [Medium] [Remove Duplicates from Sorted Array II](remove-duplicates-from-sorted-array-ii)




## Solution:

[TOC]

## Solution

---
#### Approach 1: Two Pointers

**Algorithm**

Since the array is already sorted, we can keep two pointers $$i$$ and $$j$$, where $$i$$ is the slow-runner while $$j$$ is the fast-runner. As long as $$nums[i] = nums[j]$$, we increment $$j$$ to skip the duplicate.

When we encounter $$nums[j] \neq nums[i]$$, the duplicate run has ended so we must copy its value to $$nums[i + 1]$$. $$i$$ is then incremented and we repeat the same process again until $$j$$ reaches the end of array.

<iframe src="https://leetcode.com/playground/p8jPfpcx/shared" frameBorder="0" width="100%" height="242" name="p8jPfpcx"></iframe>

**Complexity analysis**

* Time complextiy : $$O(n)$$.
Assume that $$n$$ is the length of array. Each of $$i$$ and $$j$$ traverses at most $$n$$ steps.

* Space complexity : $$O(1)$$.
