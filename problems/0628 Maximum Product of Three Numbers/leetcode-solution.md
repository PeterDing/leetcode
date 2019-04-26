# 0628 - Maximum Product of Three Numbers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Math | [Leetcode](https://leetcode.com/problems/maximum-product-of-three-numbers) | [solution](https://leetcode.com/problems/maximum-product-of-three-numbers/solution/)


-----------

<p>Given an integer array, find three numbers whose product is maximum and output the maximum product.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [1,2,3]
<b>Output:</b> 6
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [1,2,3,4]
<b>Output:</b> 24
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The length of the given array will be in range [3,10<sup>4</sup>] and all elements are in the range [-1000, 1000].</li>
	<li>Multiplication of any three numbers in the input won&#39;t exceed the range of 32-bit signed integer.</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Maximum Product Subarray](maximum-product-subarray)




## Solution:

[TOC]

## Solution

---
#### Approach 1: Brute Force

The simplest solution is to consider every triplet out of the given $$nums$$ array and check their product and find out the maximum product out of them.

**Complexity Analysis**

* Time complexity : $$O(n^3)$$. We need to consider every triplet from $$nums$$ array of length $$n$$.

* Space complexity : $$O(1)$$. Constant extra space is used.
<br>
<br>

---
#### Approach 2: Using Sorting

**Algorithm**

Another solution could be to sort the given $$nums$$ array(in ascending order) and find out the product of the last three numbers. 

But, we can note that this product will be maximum only if all the numbers in $$nums$$ array are positive. But, in the given problem statement, negative elements could exist as well. 

Thus, it could also be possible that two negative numbers lying at the left extreme end could also contribute to lead to a larger product if the third number in the triplet being considered is the largest positive number in the $$nums$$ array. 

Thus, either the product $$nums[0] \times nums[1] \times nums[n-1]$$ or $$nums[n-3] \times nums[n-2] \times nums[n-1]$$ will give the required result. Thus, we need to find the larger one from out of these values.

<iframe src="https://leetcode.com/playground/82yt6W5b/shared" frameBorder="0" width="100%" height="157" name="82yt6W5b"></iframe>

**Complexity Analysis**

* Time complexity : $$O\big(n\log n\big)$$. Sorting the $$nums$$ array takes $$n\log n$$ time.

* Space complexity : $$O(\log n)$$. Sorting takes $$O(\log n)$$ space.
<br>
<br>

---
#### Approach 3: Single Scan

**Algorithm**

We need not necessarily sort the given $$nums$$ array to find the maximum product. Instead, we can only find the required 2 smallest values($$min1$$ and $$min2$$) and the three largest values($$max1, max2, max3$$) in the $$nums$$ array, by iterating over the $$nums$$ array only once. 

At the end, again we can find out the larger value out of $$min1 \times min2 \times max1$$ and $$max1 \times max2 \times max3$$ to find the required maximum product.

<iframe src="https://leetcode.com/playground/x2EL5tXQ/shared" frameBorder="0" width="100%" height="480" name="x2EL5tXQ"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Only one iteration over the $$nums$$ array of length $$n$$ is required.

* Space complexity : $$O(1)$$. Constant extra space is used.
<br>
<br>

---

Analysis written by: [@vinod23](https://leetcode.com/vinod23)
