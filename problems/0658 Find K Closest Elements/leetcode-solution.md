# 0658 - Find K Closest Elements

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Binary Search | [Leetcode](https://leetcode.com/problems/find-k-closest-elements) | [solution](https://leetcode.com/problems/find-k-closest-elements/solution/)


-----------

<p>
Given a sorted array, two integers <code>k</code> and <code>x</code>, find the <code>k</code> closest elements to <code>x</code> in the array.  The result should also be sorted in ascending order.
If there is a tie,  the smaller elements are always preferred.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,2,3,4,5], k=4, x=3
<b>Output:</b> [1,2,3,4]
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2,3,4,5], k=4, x=-1
<b>Output:</b> [1,2,3,4]
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The value k is positive and will always be smaller than the length of the sorted array.</li>
<li> Length of the given array is positive and will not exceed 10<sup>4</sup></li>
<li> Absolute value of elements in the array and x will not exceed 10<sup>4</sup></li>
</ol>
</p>

<hr />

<p>
<b><font color="red">UPDATE (2017/9/19):</font></b><br />
The <i>arr</i> parameter had been changed to an <b>array of integers</b> (instead of a list of integers). <b><i>Please reload the code definition to get the latest changes</i></b>.
</p>

-----------


## Similar Problems

- [Easy] [Guess Number Higher or Lower](guess-number-higher-or-lower)

- [Medium] [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii)

- [Hard] [Find K-th Smallest Pair Distance](find-k-th-smallest-pair-distance)




## Solution:

[TOC]


## Solution

---
#### Approach 1: Using Collection.sort()

**Algorithm**

Intuitively, we can sort the elements in list `arr` by their absolute difference values to the target `x`. Then the sublist of the first k elements is the result after sorting the elements by the natural order.

<iframe src="https://leetcode.com/playground/pPUrT4oY/shared" frameBorder="0" width="100%" height="157" name="pPUrT4oY"></iframe>

Note: This solution is inspired by [@compton_scatter](https://discuss.leetcode.com/user/compton_scatter).

**Complexity Analysis**

* Time complexity : $$O(n\log n)$$. Collections.sort() uses binary sort so it has a $$O(n\log n)$$ complexity.

* Space complexity : $$O(k)$$. The in-place sorting does not consume any extra space. However, generating a k length sublist will take some space.
<br>
<br>

---
#### Approach 2: Binary Search and Two Pointers

**Algorithm**

The original array has been sorted so we can take this advantage by the following steps.
1. If the target `x` is less or equal than the first element in the sorted array, the first `k` elements are the result.
2. Similarly, if the target `x` is more or equal than the last element in the sorted array, the last `k` elements are the result.
3. Otherwise, we can use binary search to find the `index` of the element, which is equal (when this list has `x`) or a little bit larger than `x` (when this list does not have it). Then set `low` to its left `k-1` position, and `high` to the right `k-1` position of this `index` as a start. The desired k numbers must in this rang [index-k-1, index+k-1]. So we can shrink this range to get the result using the following rules.
    * If `low` reaches the lowest index `0` or the `low` element is closer to `x` than the `high` element, decrease the `high` index.
    * If `high` reaches to the highest index `arr.size()-1` or it is nearer to `x` than the `low` element, increase the `low` index.
    * The looping ends when there are exactly k elements in [low, high], the subList of which is the result.

<iframe src="https://leetcode.com/playground/kS5bGpg6/shared" frameBorder="0" width="100%" height="480" name="kS5bGpg6"></iframe>

**Complexity Analysis**

* Time complexity : $$O(\log n +k)$$. $$O(\log n)$$ is for the time of binary search, while $$O(k)$$ is for shrinking the index range to k elements.

* Space complexity : $$O(k)$$. It is to generate the required sublist.


Analysis written by: [@Mr.Bin](https://discuss.leetcode.com/user/mr-bin)
