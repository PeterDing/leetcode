# 0376 - Wiggle Subsequence

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming, Greedy | [Leetcode](https://leetcode.com/problems/wiggle-subsequence) | [solution](https://leetcode.com/problems/wiggle-subsequence/solution/)


-----------

<p>A sequence of numbers is called a <strong>wiggle sequence</strong> if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.</p>

<p>For example, <code>[1,7,4,9,2,5]</code> is a wiggle sequence because the differences <code>(6,-3,5,-7,3)</code> are alternately positive and negative. In contrast, <code>[1,4,7,2,5]</code> and <code>[1,7,4,5,5]</code> are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.</p>

<p>Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,7,4,9,2,5]</span>
<strong>Output: </strong><span id="example-output-1">6
<strong>Explanation:</strong> </span>The entire sequence is a wiggle sequence.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,17,5,10,13,15,10,5,16,8]</span>
<strong>Output: </strong><span id="example-output-2">7
</span><span id="example-output-1"><strong>Explanation: </strong></span>There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,2,3,4,5,6,7,8,9]</span>
<strong>Output: </strong><span id="example-output-3">2</span></pre>

<p><b>Follow up:</b><br />
Can you do it in O(<i>n</i>) time?</p>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Summary

We need to find the length of the longest wiggle subsequence. A wiggle subsequence consists of a subsequence with numbers which appears in alternating ascending / descending order.


## Solution
#### Approach #1 Brute Force [Time Limit Exceeded]

Here, we can find the length of every possible wiggle subsequence and find the maximum length out of them. To implement this, we use a recursive function, $$\text{calculate}(\text{nums}, \text{index}, \text{isUp})$$ which takes the array $$\text{nums}$$, the $$\text{index}$$ from which we need to find the length of the longest wiggle subsequence, boolean variable $$\text{isUp}$$ to tell whether we need to find an increasing wiggle or decreasing wiggle respectively. If the function $$\text{calculate}$$ is called after an increasing wiggle, we need to find the next decreasing wiggle with the same function. If the function $$\text{calculate}$$ is called after a decreasing wiggle, we need to find the next increasing wiggle with the same function.


<iframe src="https://leetcode.com/playground/JXWefkVB/shared" frameBorder="0" name="JXWefkVB" width="100%" height="326"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n!)$$. $$\text{calculate}()$$ will be called maximum $$n!$$ times.
* Space complexity : $$O(n)$$. Recursion of depth $$n$$ is used.

---
#### Approach #2  Dynamic Programming [Accepted]

**Algorithm**

To understand this approach, take two arrays for dp named $$up$$ and $$down$$.

Whenever we pick up any element of the array to be a part of the wiggle subsequence, that element could be a part of a rising wiggle or a falling wiggle depending upon which element we have taken prior to it.

$$up[i]$$ refers to the length of the longest wiggle subsequence obtained so far considering $$i^{th}$$ element as the last element of the wiggle subsequence and ending with a rising wiggle.

Similarly, $$down[i]$$ refers to the length of the longest wiggle subsequence obtained so far considering $$i^{th}$$ element as the last element of the wiggle subsequence and ending with a falling wiggle.

$$up[i]$$ will be updated every time we find a rising wiggle ending with the $$i^{th}$$ element. Now, to find $$up[i]$$, we need to consider the maximum out of all the previous wiggle subsequences ending with a falling wiggle i.e. $$down[j]$$, for every $$j&lt;i$$ and $$nums[i]&gt;nums[j]$$. Similarly, $$down[i]$$ will be updated.



<iframe src="https://leetcode.com/playground/5DeX9SiP/shared" frameBorder="0" name="5DeX9SiP" width="100%" height="360"></iframe>
**Complexity Analysis**

* Time complexity : $$O(n^2)$$. Loop inside a loop.
* Space complexity : $$O(n)$$. Two arrays of the same length are used for dp.

---
#### Approach #3 Linear Dynamic Programming [Accepted]

**Algorithm**

Any element in the array could correspond to only one of the three possible states:

1. up position, it means $$nums[i] > nums[i-1]$$
2. down position, it means $$nums[i] < nums[i-1]$$
3. equals to position, $$nums[i] == nums[i-1]$$

The updates are done as:

If $$nums[i] > nums[i-1]$$, that means it wiggles up. The element before it must be a down position. So $$up[i] = down[i-1] + 1$$, $$down[i]$$ remains the same as $$down[i-1]$$.
If $$nums[i] < nums[i-1]$$, that means it wiggles down. The element before it must be a up position. So $$down[i] = up[i-1] + 1$$, $$up[i]$$ remains the same as $$up[i-1]$$.
If $$nums[i] == nums[i-1]$$, that means it will not change anything becaue it didn't wiggle at all. So both $$down[i]$$ and $$up[i]$$ remain the same as $$down[i-1]$$ and $$up[i-1]$$.

At the end, we can find the larger out of $$up[length-1]$$ and $$down[length-1]$$ to find the max. wiggle subsequence length, where $$length$$ refers to the number of elements in the given array.

The process can be illustrated with the following example:

<!--![Wiggle gif](https://leetcode.com/media/original_images/376_Wiggle_Subsequence.gif)-->
!?!../Documents/376_Wiggle.json:1000,563!?!

<iframe src="https://leetcode.com/playground/iKGkFpFG/shared" frameBorder="0" name="iKGkFpFG" width="100%" height="428"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Only one pass over the array length.
* Space complexity : $$O(n)$$. Two arrays of the same length are used for dp.

---

#### Approach #4 Space-Optimized Dynamic Programming [Accepted]

**Algorithm**

This approach relies on the same concept as [Approach #3](https://leetcode.com/articles/wiggle-subsequence/#approach-3-linear-dynamic-programming-accepted). But we can observe that in the DP approach, for updating elements $$up[i]$$ and $$down[i]$$, we need only the elements $$up[i-1]$$ and $$down[i-1]$$. Thus, we can save space by not using the whole array, but only the last elements.


<iframe src="https://leetcode.com/playground/hUCEjR4D/shared" frameBorder="0" name="hUCEjR4D" width="100%" height="292"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Only one pass over the array length.
* Space complexity : $$O(1)$$. Constant space is used.

---

#### Approach #5 Greedy Approach [Accepted]

**Algorithm**

We need not necessarily need dp to solve this problem. This problem is equivalent to finding the number of alternating max. and min. peaks in the array. Since, if we choose any other intermediate number to be a part of the current wiggle subsequence, the maximum length of that wiggle subsequence will always be less than or equal to the one obtained by choosing only the consecutive max. and min. elements.

This can be clarified by looking at the following figure:
![Wiggle Peaks](https://leetcode.com/media/original_images/376_Wiggle_Subsequence.PNG)

From the above figure, we can see that if we choose **C** instead of **D** as the 2nd point in the wiggle subsequence, we can't include the point **E**. Thus, we won't obtain the maximum length wiggle subsequence.

Thus, to solve this problem, we maintain a variable $$\text{prevdiff}$$, where $$\text{prevdiff}$$ is used to indicate whether the current subsequence of numbers lies in an increasing or decreasing wiggle. If $$\text{prevdiff} > 0$$, it indicates that we have found the increasing wiggle and are looking for a decreasing wiggle now. Thus, we update the length of the found subsequence when $$\text{diff}$$ ($$nums[i]-nums[i-1]$$) becomes negative. Similarly, if $$\text{prevdiff} < 0$$, we will update the count when $$\text{diff}$$ ($$nums[i]-nums[i-1]$$) becomes positive.

When the complete array has been traversed, we get the required count, which represents the length of the longest wiggle subsequence.


<iframe src="https://leetcode.com/playground/AqoaR5Ks/shared" frameBorder="0" name="AqoaR5Ks" width="100%" height="326"></iframe>
**Complexity Analysis**

* Time complexity : $$O(n)$$. We traverse the given array once.

* Space complexity : $$O(1)$$. No extra space is used.

---

Analysis written by: [@vinod23](https://leetcode.com/vinod23)
