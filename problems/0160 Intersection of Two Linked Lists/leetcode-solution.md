# 0160 - Intersection of Two Linked Lists

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Linked List | [Leetcode](https://leetcode.com/problems/intersection-of-two-linked-lists) | [solution](https://leetcode.com/problems/intersection-of-two-linked-lists/solution/)


-----------

<p>Write a program to find the node at which the intersection of two singly linked lists begins.</p>

<p>For example, the following two linked lists:</p>
<a href="https://assets.leetcode.com/uploads/2018/12/13/160_statement.png" target="_blank"><img alt="" src="https://assets.leetcode.com/uploads/2018/12/13/160_statement.png" style="margin-top: 10px; margin-bottom: 10px; width: 400px; height: 130px;" /></a>

<p>begin to intersect at node c1.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png" target="_blank"><img alt="" src="https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png" style="margin-top: 10px; margin-bottom: 10px; width: 400px; height: 130px;" /></a>

<pre>
<strong>Input: </strong>intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
<strong>Output:</strong> Reference of the node with value = 8
<strong>Input Explanation:</strong> The intersected node&#39;s value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.</pre>

<p>&nbsp;</p>

<p><strong>Example 2:</strong></p>
<a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png" target="_blank"><img alt="" src="https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png" style="margin-top: 10px; margin-bottom: 10px; width: 350px; height: 136px;" /></a>

<pre>
<strong>Input: </strong>intersectVal&nbsp;= 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
<strong>Output:</strong> Reference of the node with value = 2
<strong>Input Explanation:</strong>&nbsp;The intersected node&#39;s value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
</pre>

<p>&nbsp;</p>

<p><strong>Example 3:</strong></p>
<a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png" target="_blank"><img alt="" src="https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png" style="margin-top: 10px; margin-bottom: 10px; width: 200px; height: 126px;" /></a>

<pre>
<strong>Input: </strong>intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
<strong>Output:</strong> null
<strong>Input Explanation:</strong> From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
<strong>Explanation:</strong> The two lists do not intersect, so return null.
</pre>

<p>&nbsp;</p>

<p><b>Notes:</b></p>

<ul>
	<li>If the two linked lists have no intersection at all, return <code>null</code>.</li>
	<li>The linked lists must retain their original structure after the function returns.</li>
	<li>You may assume there are no cycles anywhere in the entire linked structure.</li>
	<li>Your code should preferably run in O(n) time and use only O(1) memory.</li>
</ul>


-----------


## Similar Problems

- [Easy] [Minimum Index Sum of Two Lists](minimum-index-sum-of-two-lists)




## Solution:

[TOC]

## Solution

---
#### Approach 1: Brute Force

For each node a<sub>i</sub> in list A, traverse the entire list B and check if any node in list B coincides with a<sub>i</sub>.

**Complexity Analysis**

* Time complexity : $$O(mn)$$.

* Space complexity : $$O(1)$$.
<br />
<br />
---
#### Approach 2: Hash Table

Traverse list A and store the address / reference to each node in a hash set. Then check every node b<sub>i</sub> in list B: if b<sub>i</sub> appears in the hash set, then b<sub>i</sub> is the intersection node.

**Complexity Analysis**

* Time complexity : $$O(m+n)$$.

* Space complexity : $$O(m)$$ or $$O(n)$$.
<br />
<br />
---
#### Approach 3: Two Pointers

- Maintain two pointers $$pA$$ and $$pB$$ initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
- When $$pA$$ reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when $$pB$$ reaches the end of a list, redirect it the head of A.
- If at any point $$pA$$ meets $$pB$$, then $$pA$$/$$pB$$ is the intersection node.
- To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), $$pB$$ would reach the end of the merged list first, because $$pB$$ traverses exactly 2 nodes less than $$pA$$ does. By redirecting $$pB$$ to head A, and $$pA$$ to head B, we now ask $$pB$$ to travel exactly 2 more nodes than $$pA$$ would. So in the second iteration, they are guaranteed to reach the intersection node at the same time.
- If two lists have intersection, then their last nodes must be the same one. So when $$pA$$/$$pB$$ reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.

**Complexity Analysis**

* Time complexity : $$O(m+n)$$.

* Space complexity : $$O(1)$$.
