# 0643 - Maximum Average Subarray I

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/maximum-average-subarray-i) | [solution](https://leetcode.com/problems/maximum-average-subarray-i/solution/)


-----------

<p>Given an array consisting of <code>n</code> integers, find the contiguous subarray of given length <code>k</code> that has the maximum average value. And you need to output the maximum average value.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [1,12,-5,-6,50,3], k = 4
<b>Output:</b> 12.75
<b>Explanation:</b> Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>1 &lt;= <code>k</code> &lt;= <code>n</code> &lt;= 30,000.</li>
	<li>Elements of the given array will be in the range [-10,000, 10,000].</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Hard] [Maximum Average Subarray II](maximum-average-subarray-ii)




## Solution:

[TOC]

 
## Solution

---
#### Approach #1 Cumulative Sum [Accepted]

**Algorithm**

We know that in order to obtain the averages of subarrays with length $$k$$, we need to obtain the sum of these $$k$$ length subarrays. One of the methods of obtaining this sum is to make use of a cumulative sum array, $$sum$$, which is populated only once. Here, $$sum[i]$$ is used to store the sum of the elements of the given $$nums$$ array from the first element upto the element at the $$i^{th}$$ index.

Once the $$sum$$ array has been filled up, in order to find the sum of elements from the index $$i$$ to $$i+k$$, all we need to do is to use: $$sum[i] - sum[i-k]$$. Thus, now, by doing one more iteration over the $$sum$$ array, we can determine the maximum average possible from the subarrays of length $$k$$.

The following animation illustrates the process for a simple example.

!?!../Documents/643_Maximum_Average.json:1000,563!?!

<iframe src="https://leetcode.com/playground/dJyoFWQo/shared" frameBorder="0" name="dJyoFWQo" width="100%" height="275"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. We iterate over the $$nums$$ array of length $$n$$ once to fill the $$sum$$ array. Then, we iterate over $$n-k$$ elements of $$sum$$ to determine the required result.

* Space complexity : $$O(n)$$. We make use of a $$sum$$ array of length $$n$$ to store the cumulative sum.

---


#### Approach #2 Sliding Window [Accepted]

**Algorithm**

Instead of creating a cumulative sum array first, and then traversing over it to determine the required sum, we can simply traverse over $$nums$$ just once, and on the go keep on determining the sums possible for the subarrays of length $$k$$. To understand the idea, assume that we already know the sum of elements from index $$i$$ to index $$i+k$$, say it is $$x$$.

Now, to determine the sum of elements from the index $$i+1$$ to the index $$i+k+1$$, all we need to do is to subtract the element $$nums[i]$$ from $$x$$ and to add the element $$nums[i+k+1]$$ to $$x$$. We can carry out our process based on this idea and determine the maximum possible average.

<iframe src="https://leetcode.com/playground/uABxt2Z8/shared" frameBorder="0" name="uABxt2Z8" width="100%" height="292"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. We iterate over the given $$nums$$ array of length $$n$$ once only.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
