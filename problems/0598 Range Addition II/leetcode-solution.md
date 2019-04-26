# 0598 - Range Addition II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/range-addition-ii) | [solution](https://leetcode.com/problems/range-addition-ii/solution/)


-----------

<p>Given an m * n matrix <b>M</b> initialized with all <b>0</b>'s and several update operations.</p>
<p>Operations are represented by a 2D array, and each operation is represented by an array with two <b>positive</b> integers <b>a</b> and <b>b</b>, which means <b>M[i][j]</b> should be <b>added by one</b> for all <b>0 <= i < a</b> and <b>0 <= j < b</b>. </p>
<p>You need to count and return the number of maximum integers in the matrix after performing all the operations.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
m = 3, n = 3
operations = [[2,2],[3,3]]
<b>Output:</b> 4
<b>Explanation:</b> 
Initially, M = 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M = 
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M = 
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The range of m and n is [1,40000].</li>
<li>The range of a is [1,m], and the range of b is [1,n].</li>
<li>The range of operations size won't exceed 10,000.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Range Addition](range-addition)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

The simplest method is to create a actual 2-D array of size $$m$$x$$n$$($$arr$$), perform all the operations one by one on the given range of elements, and then count the number of maximum elements. Now, we know that all the operations performed always include the element at index $$(0,0)$$. Thus, the element $$arr[0][0]$$ will always be the maximum. After performing all the operations, we can count the number of elements equal to $$arr[0][0]$$ to get the required count of the maximum elements.

<iframe src="https://leetcode.com/playground/awQVAxR8/shared" frameBorder="0" name="awQVAxR8" width="100%" height="411"></iframe>

**Complexity Analysis**

* Time complexity : $$O(x*m*n)$$. Array is updated $$x$$ times, where $$x$$ represents number of times operation is preformed i.e. $$ops.length$$.

* Space complexity : $$O(m*n)$$. Array of size $$m*n$$ is used.

---
#### Approach #2 Single Pass [Accepted]

**Algorithm**

As per the given problem statement, all the operations are performed on a rectangular sub-matrix of the initial all 0's $$M$$ matrix. The upper left corner of each such rectangle is given by the index $$(0, 0)$$ and the lower right corner for an operation $$[i, j]$$ is given by the index $$(i, j)$$. 

The maximum element will be the one on which all the operations have been performed. The figure below shows an example of two operations being performed on the initial $$M$$ array. 

![Range_Addition](../Figures/598_Range_Addition2.PNG)

From this figure, we can observe that the maximum elements will be the ones which lie in the intersection region of the rectangles representing the operations. Further, we can observe that to count the number of elements lying in this intersection region, we don't actually need to perform the operations, but we need to determine the lower right cornerof the intersecting region only. This corner is given by $$\big(x, y\big) = \big(\text{min}(op[0], \text{min}(op[1])\big)$$, where $$\text{min}(op[i])$$ reprsents the minimum value of $$op[i]$$ from among all the $$op[i]$$'s in the given set of operations.

Thus, the resultant count of elements lying in the intersection is given by: $$x$$x$$y$$.

<iframe src="https://leetcode.com/playground/eUWGJ45b/shared" frameBorder="0" name="eUWGJ45b" width="100%" height="224"></iframe>

**Complexity Analysis**

* Time complexity : $$O(x)$$. Single traversal of all operations is done. $$x$$ refers to the number of operations.

* Space complexity : $$O(1)$$. No extra space is used.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
