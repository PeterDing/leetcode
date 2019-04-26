# 0654 - Maximum Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/maximum-binary-tree) | [solution](https://leetcode.com/problems/maximum-binary-tree/solution/)


-----------

<p>
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
<ol>
<li>The root is the maximum number in the array. </li>
<li>The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.</li>
<li>The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.</li> 
</ol>
</p>

<p>
Construct the maximum tree by the given array and output the root node of this tree.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [3,2,1,6,0,5]
<b>Output:</b> return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The size of the given array will be in the range [1,1000].</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Maximum Binary Tree II](maximum-binary-tree-ii)




## Solution:

[TOC]


## Solution

---
#### Approach 1: Recursive Solution

The current solution is very simple. We make use of a function `construct(nums, l, r)`, which returns the maximum binary tree consisting of numbers within the indices $$l$$ and $$r$$ in the given $$nums$$ array(excluding the $$r^{th}$$ element).

The algorithm consists of the following steps:

1. Start with the function call `construct(nums, 0, n)`. Here, $$n$$ refers to the number of elements in the given $$nums$$ array.

2. Find the index, $$max_i$$, of the largest element in the current range of indices $$(l:r-1)$$. Make this largest element, $$nums[max\_i]$$ as the local root node.

3. Determine the left child using `construct(nums, l, max_i)`. Doing this recursively finds the largest element in the subarray left to the current largest element.

4. Similarly, determine the right child using `construct(nums, max_i + 1, r)`.

5. Return the root node to the calling function.

<iframe src="https://leetcode.com/playground/WgEZm2za/shared" frameBorder="0" width="100%" height="429" name="WgEZm2za"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. The function `construct` is called $$n$$ times. At each level of the recursive tree, we traverse over all the $$n$$ elements to find the maximum element.  In the average case, there will be a $$\log n$$ levels leading to a complexity of $$O\big(n\log n\big)$$. In the worst case, the depth of the recursive tree can grow upto $$n$$, which happens in the case of a sorted $$nums$$ array, giving a complexity of $$O(n^2)$$.

* Space complexity : $$O(n)$$. The size of the $$set$$ can grow upto $$n$$ in the worst case. In the average case, the size will be $$\log n$$ for $$n$$ elements in $$nums$$, giving an average case complexity of $$O(\log n)$$

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
