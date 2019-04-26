# 0300 - Longest Increasing Subsequence

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Binary Search, Dynamic Programming | [Leetcode](https://leetcode.com/problems/longest-increasing-subsequence) | [solution](https://leetcode.com/problems/longest-increasing-subsequence/solution/)


-----------

<p>Given an unsorted array of integers, find the length of longest increasing subsequence.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[10,9,2,5,3,7,101,18]
</code><b>Output: </b>4 
<strong>Explanation: </strong>The longest increasing subsequence is <code>[2,3,7,101]</code>, therefore the length is <code>4</code>. </pre>

<p><strong>Note: </strong></p>

<ul>
	<li>There may be more than one LIS combination, it is only necessary for you to return the length.</li>
	<li>Your algorithm should run in O(<i>n<sup>2</sup></i>) complexity.</li>
</ul>

<p><b>Follow up:</b> Could you improve it to O(<i>n</i> log <i>n</i>) time complexity?</p>


-----------


## Similar Problems

- [Medium] [Increasing Triplet Subsequence](increasing-triplet-subsequence)

- [Hard] [Russian Doll Envelopes](russian-doll-envelopes)

- [Medium] [Maximum Length of Pair Chain](maximum-length-of-pair-chain)

- [Medium] [Number of Longest Increasing Subsequence](number-of-longest-increasing-subsequence)

- [Medium] [Minimum ASCII Delete Sum for Two Strings](minimum-ascii-delete-sum-for-two-strings)




## Solution:

[TOC]

## Solution

---
#### Approach 1: Brute Force

**Algorithm**

The simplest approach is to try to find all increasing subsequences and then returning the maximum length of longest increasing subsequence. In order to
do this, we make use of a recursive function $$\text{lengthofLIS}$$ which returns the length of the LIS possible from the current element(corresponding to $$curpos$$)
 onwards(including the current element). Inside each function call, we consider two cases:

1. The current element is larger than the previous element included in the LIS. In this case, we can include the current element in the LIS. Thus, we find out the
length of the LIS obtained by including it. Further, we also find out the length of LIS possible by not including the current element in the LIS. The value returned
by the current function call is, thus, the maximum out of the two lengths.

2. The current element is smaller than the previous element included in the LIS. In this case, we can't include the current element in the LIS. Thus, we find out only
the length of the LIS possible by not including the current element in the LIS, which is returned by the current function call.

<iframe src="https://leetcode.com/playground/UoMzWLi7/shared" frameBorder="0" width="100%" height="361" name="UoMzWLi7"></iframe>

**Complexity Analysis**

* Time complexity : $$O(2^n)$$. Size of recursion tree will be $$2^n$$.

* Space complexity : $$O(n^2)$$. $$memo$$ array of size $$n * n$$ is used.

---
#### Approach 2: Recursion with Memoization

**Algorithm**

In the previous approach, many recursive calls had to made again and again with the same parameters. This redundancy can be eliminated by storing the results obtained for
a particular call in a 2-d memoization array $$memo$$. $$memo[i][j]$$ represents the length of the LIS possible using $$nums[i]$$ as the previous element considered to
be included/not included in the LIS, with $$nums[j]$$ as the current element considered to be included/not included in the LIS. Here, $$nums$$ represents the given array.

<iframe src="https://leetcode.com/playground/GSwVQjkr/shared" frameBorder="0" width="100%" height="480" name="GSwVQjkr"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. Size of recursion tree can go upto $$n^2$$.

* Space complexity : $$O(n^2)$$. $$memo$$ array of $$n*n$$ is used.

---

#### Approach 3: Dynamic Programming

**Algorithm**

This method relies on the fact that the longest increasing subsequence possible upto the $$i^{th}$$  index in a given array is independent of the elements coming
later on in the array. Thus, if we know the length of the LIS upto $$i^{th}$$ index, we can figure out the length of the LIS possible by including the $$(i+1)^{th}$$ element
based on the elements with indices $$j$$ such that $$0 \leq j \leq (i + 1)$$.

We make use of a $$dp$$ array to store the required data. $$dp[i]$$ represents the length of the longest increasing subsequence possible considering the array elements upto the $$i^{th}$$
index only ,by necessarily including the $$i^{th}$$ element. In order to find out $$dp[i]$$, we need to try to append the current element($$nums[i]$$) in every possible increasing subsequences upto the $$(i-1)^{th}$$
index(including the $$(i-1)^{th}$$ index), such that the new sequence formed by adding the current element is also an increasing subsequence. Thus, we can easily determine
$$dp[i]$$ using:  

$$dp[i] = \text{max}(dp[j]) + 1, \forall 0\leq j < i$$

At the end, the maximum out of all the $$dp[i]$$'s to determine the final result.

$$LIS_{length}= \text{max}(dp[i]), \forall 0\leq i < n$$

The following animation illustrates the method:

<!--![LIS](../Figures/300_LIS1.gif)-->
!?!../Documents/300_LIS.json:1000,563!?!


<iframe src="https://leetcode.com/playground/EVGvmMas/shared" frameBorder="0" width="100%" height="412" name="EVGvmMas"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. Two loops of $$n$$ are there.

* Space complexity : $$O(n)$$. $$dp$$ array of size $$n$$ is used.

---
#### Approach 4: Dynamic Programming with Binary Search

**Algorithm**

In this approach, we scan the array from left to right. We also make use of a $$dp$$ array initialized with all 0's. This $$dp$$ array is meant to store the
increasing subsequence formed by including the currently encountered element.
 While traversing the $$nums$$ array, we keep on filling the $$dp$$ array with
the elements encountered so far. For the element corresponding to the $$j^{th}$$ index ($$nums[j]$$),
 we determine its correct position in the $$dp$$ array(say $$i^{th}$$ index) by making use of Binary Search(which can be used since the
  $$dp$$ array is storing increasing subsequence) and also insert it at the correct position. An important point to be noted is that for Binary Search, we consider
  only that portion of the $$dp$$ array in which we have made the updates by inserting some elements at their correct positions(which remains always sorted).
  Thus, only the elements upto the $$i^{th}$$ index
  in the $$dp$$ array can determine the position of the current element in it.
  Since, the element enters its correct position($$i$$) in an ascending order in the $$dp$$ array, the
  subsequence formed so far in it is surely an increasing subsequence. Whenever this position index $$i$$ becomes equal to the length of the LIS formed so far($$len$$),
  it means, we need to update the $$len$$ as $$len = len + 1$$.

  Note: $$dp$$ array does not result in longest increasing subsequence, but length of $$dp$$ array will give you length of LIS.

 Consider the example:

input: [0, 8, 4, 12, 2]

dp: [0]

dp: [0, 8]

dp: [0, 4]

dp: [0, 4, 12]

dp: [0 , 2, 12] which is not the longest increasing subsequence, but length of $$dp$$ array results in length of Longest Increasing Subsequence.

<iframe src="https://leetcode.com/playground/Kbvq2W3R/shared" frameBorder="0" width="100%" height="344" name="Kbvq2W3R"></iframe>

Note: Arrays.binarySearch() method returns index of the search key, if it is contained in the array, else it returns (-(insertion point) - 1). The insertion point is the point at which the key would be inserted into the array: the index of the first element greater than the key, or a.length if all elements in the array are less than the specified key.

**Complexity Analysis**

* Time complexity : $$O(n\log n)$$. Binary search takes $$\log n$$ time and it is called $$n$$ times.

* Space complexity : $$O(n)$$. $$dp$$ array of size $$n$$ is used.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
