# 0034 - Find First and Last Position of Element in Sorted Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Binary Search | [Leetcode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) | [solution](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/)


-----------

<p>Given an array of integers <code>nums</code> sorted in ascending order, find the starting and ending position of a given <code>target</code> value.</p>

<p>Your algorithm&#39;s runtime complexity must be in the order of <em>O</em>(log <em>n</em>).</p>

<p>If the target is not found in the array, return <code>[-1, -1]</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 8
<strong>Output:</strong> [3,4]</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 6
<strong>Output:</strong> [-1,-1]</pre>


-----------


## Similar Problems

- [Easy] [First Bad Version](first-bad-version)




## Solution:

[TOC]

#### Approach 1: Linear Scan

**Intuition**

Checking every index for `target` exhausts the search space, so it must work.

**Algorithm**

First, we do a linear scan of `nums` from the left, `break`ing when we find
an instance of `target`. If we never `break`, then `target` is not present,
so we can return the "error code" of `[-1, -1]` early. Given that we did find
a valid left index, we can do a second linear scan, but this time from the
right. In this case, the first instance of `target` encountered will be the
rightmost one (and because a leftmost one exists, there is guaranteed to also
be a rightmost one). We then simply return a list containing the two located
indices.

<iframe src="https://leetcode.com/playground/3Qq9cbHX/shared" frameBorder="0" width="100%" height="500" name="3Qq9cbHX"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$

    This brute-force approach examines each of the `n` elements of `nums` exactly twice, so the overall runtime is linear.

* Space complexity : $$O(1)$$

    The linear scan method allocates a fixed-size array and a few integers, so it has a constant-size memory footprint.

<br />

---

#### Approach 2: Binary Search

**Intuition**

Because the array is sorted, we can use binary search to locate the left
and rightmost indices.

**Algorithm**

The overall algorithm works fairly similarly to the linear scan approach,
except for the subroutine used to find the left and rightmost indices
themselves. Here, we use a modified binary search to search a sorted array,
with a few minor adjustments. First, because we are locating the leftmost (or
rightmost) index containing `target` (rather than returning `true` iff we
find `target`), the algorithm does not terminate as soon as we find a match.
Instead, we continue to search until `lo == hi` and they contain some index
at which `target` can be found.

The other change is the introduction of the `left` parameter, which is a
boolean indicating what to do in the event that `target == nums[mid]`; if
`left` is `true`, then we "recurse" on the left subarray on ties. Otherwise,
we go right. To see why this is correct, consider the situation where we find
`target` at index `i`. The leftmost `target` cannot occur at any index
greater than `i`, so we never need to consider the right subarray. The same
argument applies to the rightmost index.

The first animation below shows the process for finding the leftmost index,
and the second shows the process for finding the index right of the rightmost
index.

!?!../Documents/34_Search_for_a_Range_left.json:1280,720!?!

!?!../Documents/34_Search_for_a_Range_right.json:1280,720!?!

<iframe src="https://leetcode.com/playground/3J9unhAP/shared" frameBorder="0" width="100%" height="500" name="3J9unhAP"></iframe>

**Complexity Analysis**

* Time complexity : $$O(\log_{10}(n))$$

    Because binary search cuts the search space roughly in half on each
    iteration, there can be at most $$\lceil \log_{10}(n) \rceil$$ iterations. Binary
    search is invoked twice, so the overall complexity is logarithmic.

* Space complexity : $$O(1)$$

    All work is done in place, so the overall memory usage is constant.
