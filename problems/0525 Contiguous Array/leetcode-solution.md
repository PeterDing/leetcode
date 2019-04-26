# 0525 - Contiguous Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table | [Leetcode](https://leetcode.com/problems/contiguous-array) | [solution](https://leetcode.com/problems/contiguous-array/solution/)


-----------

<p>Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. </p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [0,1]
<b>Output:</b> 2
<b>Explanation:</b> [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [0,1,0]
<b>Output:</b> 2
<b>Explanation:</b> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>
</p>

<p><b>Note:</b>
The length of the given binary array will not exceed 50,000.
</p>

-----------


## Similar Problems

- [Medium] [Maximum Size Subarray Sum Equals k](maximum-size-subarray-sum-equals-k)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

**Algorithm**

The brute force approach is really simple. We consider every possible subarray within the given array and count the number of zeros and ones in each subarray. Then, we find out the maximum size subarray with equal no. of zeros and ones out of them.

<iframe src="https://leetcode.com/playground/sPZqbexo/shared" frameBorder="0" name="sPZqbexo" width="100%" height="428"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. We consider every possible subarray by traversing over the complete array for every start point possible.

* Space complexity : $$O(1)$$. Only two variables $$zeroes$$ and $$ones$$ are required.

---
#### Approach #2 Using Extra Array [Accepted]

**Algorithm**

In this approach, we make use of a $$count$$ variable, which is used to store the relative number of ones and zeros encountered so far while traversing the array. The $$count$$ variable is incremented by one for every $$\text{1}$$ encountered and the same is decremented by one for every $$\text{0}$$ encountered.

We start traversing the array from the beginning. If at any moment, the $$count$$ becomes zero, it implies that we've encountered equal number of zeros and ones from the beginning till the current index of the array($$i$$). Not only this, another point to be noted is that  if we encounter the same $$count$$ twice while traversing the array, it means that the number of zeros and ones are equal between the indices corresponding to the equal $$count$$ values. The following figure illustrates the observation for the sequence `[0 0 1 0 0 0 1 1]`:

![Contiguous_Array](../Figures/535_Contiguous_Array.PNG)

In the above figure, the subarrays between (A,B), (B,C) and (A,C) (lying between indices corresponing to $$count = 2$$) have equal number of zeros and ones.

Another point to be noted is that the largest subarray is the one between the points (A, C). Thus, if we keep a track of the indices corresponding to the same $$count$$ values that lie farthest apart, we can determine the size of the largest subarray with equal no. of zeros and ones easily.

Now, the $$count$$ values can range between $$\text{-n}$$ to $$\text{+n}$$, with the extreme points corresponding to the complete array being filled with all 0's and all 1's respectively. Thus, we make use of an array $$arr$$(of size $$\text{2n+1}$$to keep a track of the various $$count$$'s encountered so far. We make an entry containing the current element's index ($$i$$) in the $$arr$$ for a new $$count$$ encountered everytime. Whenever, we come across the same $$count$$ value later while traversing the array, we determine the length of the subarray lying between the indices corresponding to the same $$count$$ values.

<iframe src="https://leetcode.com/playground/Nvw6WnPN/shared" frameBorder="0" name="Nvw6WnPN" width="100%" height="411"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. The complete array is traversed only once.

* Space complexity : $$O(n)$$. $$arr$$ array of size $$\text{2n+1}$$ is used.

---
#### Approach #3 Using HashMap [Accepted]

**Algorithm**

This approach relies on the same premise as the previous approach. But, we need not use an array of size $$\text{2n+1}$$, since it isn't necessary that we'll encounter all the $$count$$ values possible. Thus, we make use of a HashMap $$map$$ to store the entries in the form of $$(index, count)$$. We make an entry for a $$count$$ in the $$map$$ whenever the $$count$$ is encountered first, and later on use the correspoding index to find the length of the largest subarray with equal no. of zeros and ones when the same $$count$$ is encountered again.

The following animation depicts the process:
<!--![Contiguous_Array](../Figures/525_Contiguous_Array.gif)-->
!?!../Documents/525_Contiguous_Array.json:1000,563!?!

<iframe src="https://leetcode.com/playground/nG5CTUD8/shared" frameBorder="0" name="nG5CTUD8" width="100%" height="360"></iframe>
**Complexity Analysis**

* Time complexity : $$O(n)$$. The entire array is traversed only once.

* Space complexity : $$O(n)$$. Maximum size of the HashMap $$map$$ will be $$\text{n}$$, if all the elements are either 1 or 0.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
