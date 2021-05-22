# 0027 - Remove Element

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Two Pointers | [Leetcode](https://leetcode.com/problems/remove-element) | [solution](https://leetcode.com/problems/remove-element/solution/)


-----------

<p>Given an array <em>nums</em> and a value <em>val</em>, remove all instances of that value <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> and return the new length.</p>

<p>Do not allocate extra space for another array, you must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p>The order of elements can be changed. It doesn&#39;t matter what you leave beyond the new length.</p>

<p><strong>Example 1:</strong></p>

<pre>
Given <em>nums</em> = <strong>[3,2,2,3]</strong>, <em>val</em> = <strong>3</strong>,

Your function should return length = <strong>2</strong>, with the first two elements of <em>nums</em> being <strong>2</strong>.

It doesn&#39;t matter what you leave beyond the returned length.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
Given <em>nums</em> = <strong>[0,1,2,2,3,0,4,2]</strong>, <em>val</em> = <strong>2</strong>,

Your function should return length = <strong><code>5</code></strong>, with the first five elements of <em><code>nums</code></em> containing&nbsp;<strong><code>0</code></strong>, <strong><code>1</code></strong>, <strong><code>3</code></strong>, <strong><code>0</code></strong>, and&nbsp;<strong>4</strong>.

Note that the order of those five elements can be arbitrary.

It doesn&#39;t matter what values are set beyond&nbsp;the returned length.</pre>

<p><strong>Clarification:</strong></p>

<p>Confused why the returned value is an integer but your answer is an array?</p>

<p>Note that the input array is passed in by <strong>reference</strong>, which means modification to the input array will be known to the caller as well.</p>

<p>Internally you can think of this:</p>

<pre>
// <strong>nums</strong> is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to <strong>nums</strong> in your function would be known by the caller.
// using the length returned by your function, it prints the first <strong>len</strong> elements.
for (int i = 0; i &lt; len; i++) {
&nbsp; &nbsp; print(nums[i]);
}</pre>


-----------


## Similar Problems

- [Easy] [Remove Duplicates from Sorted Array](remove-duplicates-from-sorted-array)

- [Easy] [Remove Linked List Elements](remove-linked-list-elements)

- [Easy] [Move Zeroes](move-zeroes)




## Solution:

[TOC]

## Summary

This is a pretty easy problem, but one may get confused by the term "in-place" and thought it is impossible to remove an element from the array without making a copy of the array.

## Hints

1. Try two pointers.
2. Did you use the property of "the order of elements can be changed"?
3. What happens when the elements to remove are rare?

## Solution
---
#### Approach 1: Two Pointers

**Intuition**

Since question asked us to remove all elements of the given value in-place, we have to handle it with $$O(1)$$ extra space. How to solve it? We can keep two pointers $$i$$ and $$j$$, where $$i$$ is the slow-runner while $$j$$ is the fast-runner.

**Algorithm**

When $$nums[j]$$ equals to the given value, skip this element by incrementing $$j$$. As long as $$nums[j] \neq val$$, we copy $$nums[j]$$ to $$nums[i]$$ and increment both indexes at the same time. Repeat the process until $$j$$ reaches the end of the array and the new length is $$i$$.

This solution is very similar to the solution to [Remove Duplicates from Sorted Array](https://leetcode.com/articles/remove-duplicates-from-sorted-array/).

<iframe src="https://leetcode.com/playground/AhMXwwbK/shared" frameBorder="0" width="100%" height="225" name="AhMXwwbK"></iframe>

**Complexity analysis**

* Time complexity : $$O(n)$$.
Assume the array has a total of $$n$$ elements, both $$i$$ and $$j$$ traverse at most $$2n$$ steps.

* Space complexity : $$O(1)$$.
<br />
<br />
---

#### Approach 2: Two Pointers - when elements to remove are rare

**Intuition**

Now consider cases where the array contains few elements to remove. For example, $$nums = [1,2,3,5,4], val = 4$$. The previous algorithm will do unnecessary copy operation of the first four elements. Another example is $$nums = [4,1,2,3,5], val = 4$$. It seems unnecessary to move elements $$[1,2,3,5]$$ one step left as the problem description mentions that the order of elements could be changed.

**Algorithm**

When we encounter $$nums[i] = val$$, we can swap the current element out with the last element and dispose the last one. This essentially reduces the array's size by 1.

Note that the last element that was swapped in could be the value you want to remove itself. But don't worry, in the next iteration we will still check this element.

<iframe src="https://leetcode.com/playground/Kxx4DqUL/shared" frameBorder="0" width="100%" height="293" name="Kxx4DqUL"></iframe>

**Complexity analysis**

* Time complexity : $$O(n)$$.
Both $$i$$ and $$n$$ traverse at most $$n$$ steps. In this approach, the number of assignment operation is equal to the number of elements to remove. So it is more efficient if elements to remove are rare.

* Space complexity : $$O(1)$$.
