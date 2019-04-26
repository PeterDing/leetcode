# 0162 - Find Peak Element

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Binary Search | [Leetcode](https://leetcode.com/problems/find-peak-element) | [solution](https://leetcode.com/problems/find-peak-element/solution/)


-----------

<p>A peak element is an element that is greater than its neighbors.</p>

<p>Given an input array <code>nums</code>, where <code>nums[i] &ne; nums[i+1]</code>, find a peak element and return its index.</p>

<p>The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.</p>

<p>You may imagine that <code>nums[-1] = nums[n] = -&infin;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <strong>nums</strong> = <code>[1,2,3,1]</code>
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 is a peak element and your function should return the index number 2.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <strong>nums</strong> = <code>[</code>1,2,1,3,5,6,4]
<strong>Output:</strong> 1 or 5 
<strong>Explanation:</strong> Your function can return either index number 1 where the peak element is 2, 
&nbsp;            or index number 5 where the peak element is 6.
</pre>

<p><strong>Note:</strong></p>

<p>Your solution should be in logarithmic complexity.</p>


-----------


## Similar Problems

- [Easy] [Peak Index in a Mountain Array](peak-index-in-a-mountain-array)




## Solution:

[TOC]


## Solution

---
#### Approach 1: Linear Scan

In this approach, we make use of the fact that two consecutive numbers $$nums[j]$$ and $$nums[j + 1]$$ are never equal. Thus, we can traverse over the $$nums$$ array starting from the beginning. Whenever, we find a number $$nums[i]$$, we only need to check if it is larger than the next number $$nums[i+1]$$ for determining if $$nums[i]$$ is the peak element. The reasoning behind this can be understood by taking the following three cases which cover every case into which any problem can be divided.


Case 1. All the numbers appear in a descending order. In this case, the first element corresponds to the peak element. We start off by checking if the current element is larger than the next one. The first element satisfies this criteria, and is hence identified as the peak correctly. In this case, we didn't reach a point where we needed to compare $$nums[i]$$ with $$nums[i-1]$$ also, to determine if it is the peak element or not.

![Graph](../Figures/162/Find_Peak_Case1.PNG)
{:align="center"}

Case 2. All the elements appear in ascending order. In this case, we keep on comparing $$nums[i]$$ with $$nums[i+1]$$ to determine if $$nums[i]$$ is the peak element or not. None of the elements satisfy this criteria, indicating that we are currently on a rising slope and not on a peak. Thus, at the end, we need to return the last element as the peak element, which turns out to be correct. In this case also, we need not compare $$nums[i]$$ with $$nums[i-1]$$, since being on the rising slope is a sufficient condition to ensure that $$nums[i]$$ isn't the peak element.

![Graph](../Figures/162/Find_Peak_Case2.PNG)
{:align="center"}

Case 3. The peak appears somewhere in the middle. In this case, when we are traversing on the rising edge, as in Case 2, none of the elements will satisfy $$nums[i] > nums[i + 1]$$. We need not compare $$nums[i]$$ with $$nums[i-1]$$ on the rising slope as discussed above. When we finally reach the peak element, the condition $$nums[i] > nums[i + 1]$$ is satisfied. We again, need not compare $$nums[i]$$ with $$nums[i-1]$$. This is because, we could reach $$nums[i]$$ as the current element only when the check $$nums[i] > nums[i + 1]$$ failed for the previous($$(i-1)^{th}$$ element, indicating that $$nums[i-1] < nums[i]$$. Thus, we are able to identify the peak element correctly in this case as well.

![Graph](../Figures/162/Find_Peak_Case3.PNG)
{:align="center"}

<iframe src="https://leetcode.com/playground/MLfS4Quj/shared" frameBorder="0" width="100%" height="208" name="MLfS4Quj"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. We traverse the $$nums$$ array of size $$n$$ once only.

* Space complexity : $$O(1)$$. Constant extra space is used.
<br />
<br />
---
#### Approach 2: Recursive Binary Search

**Algorithm**

We can view any given sequence in $$nums$$ array as alternating ascending and descending sequences. By making use of this, and the fact that we can return any peak as the result, we can make use of Binary Search to find the required peak element.

In case of simple Binary Search, we work on a sorted sequence of numbers and try to find out the required number by reducing the search space at every step. In this case, we use a modification of this simple Binary Search to our advantage. We start off by finding the middle element, $$mid$$ from the given $$nums$$ array. If this element happens to be lying in a descending sequence of numbers. or a local falling slope(found by comparing $$nums[i]$$ to its right neighbour), it means that the peak will always lie towards the left of this element. Thus, we reduce the search space to the left of $$mid$$(including itself) and perform the same process on left subarray.

If the middle element, $$mid$$ lies in an ascending sequence of numbers, or a rising slope(found by comparing $$nums[i]$$ to its right neighbour), it obviously implies that the peak lies towards the right of this element. Thus, we reduce the search space to the right of $$mid$$ and perform the same process on the right subarray.

In this way, we keep on reducing the search space till we eventually reach a state where only one element is remaining in the search space. This single element is the peak element.

To see how it works, let's consider the three cases discussed above again.

Case 1. In this case, we firstly find $$3$$ as the middle element. Since it lies on a falling slope, we reduce the search space to `[1, 2, 3]`. For this subarray, $$2$$ happens to be the middle element, which again lies on a falling slope, reducing the search space to `[1, 2]`. Now, $$1$$ acts as the middle element and it lies on a falling slope, reducing the search space to `[1]` only. Thus, $$1$$ is returned as the peak correctly.

!?!../Documents/Find_Peak_Case1.json:1000,563!?!

Case 2. In this case, we firstly find $$3$$ as the middle element. Since it lies on a rising slope, we reduce the search space to `[4, 5]`. Now, $$4$$ acts as the middle element for this subarray and it lies on a rising slope, reducing the search space to `[5]` only. Thus, $$5$$ is returned as the peak correctly.

!?!../Documents/Find_Peak_Case2.json:1000,563!?!

Case 3. In this case, the peak lies somewhere in the middle. The first middle element is $$4$$. It lies on a rising slope, indicating that the peak lies towards its right. Thus, the search space is reduced to `[5, 1]`. Now, $$5$$ happens to be the on a falling slope(relative to its right neighbour), reducing the search space to `[5]` only. Thus, $$5$$ is identified as the peak element correctly.

!?!../Documents/Find_Peak_Case3.json:1000,563!?!

<iframe src="https://leetcode.com/playground/3MGjFqJ4/shared" frameBorder="0" width="100%" height="276" name="3MGjFqJ4"></iframe>

**Complexity Analysis**

* Time complexity : $$O\big(log_2(n)\big)$$. We reduce the search space in half at every step. Thus, the total search space will be consumed in $$log_2(n)$$ steps. Here, $$n$$ refers to the size of $$nums$$ array.

* Space complexity : $$O\big(log_2(n)\big)$$. We reduce the search space in half at every step. Thus, the total search space will be consumed in $$log_2(n)$$ steps. Thus, the depth of recursion tree will go upto $$log_2(n)$$.
<br />
<br />
---
#### Approach 3: Iterative Binary Search

**Algorithm**

The binary search discussed in the previous approach used a recursive method. We can do the same process in an iterative fashion also. This is done in the current approach.

<iframe src="https://leetcode.com/playground/EnevWycv/shared" frameBorder="0" width="100%" height="276" name="EnevWycv"></iframe>

**Complexity Analysis**

* Time complexity : $$O\big(log_2(n)\big)$$. We reduce the search space in half at every step. Thus, the total search space will be consumed in $$log_2(n)$$ steps. Here, $$n$$ refers to the size of $$nums$$ array.

* Space complexity : $$O(1)$$. Constant extra space is used.
