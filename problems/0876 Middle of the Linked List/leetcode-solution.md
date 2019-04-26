# 0876 - Middle of the Linked List

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Linked List | [Leetcode](https://leetcode.com/problems/middle-of-the-linked-list) | [solution](https://leetcode.com/problems/middle-of-the-linked-list/solution/)


-----------

<p>Given a non-empty, singly&nbsp;linked list with head node <code>head</code>, return&nbsp;a&nbsp;middle node of linked list.</p>

<p>If there are two middle nodes, return the second middle node.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4,5]</span>
<strong>Output: </strong>Node 3 from this list (Serialization: <span id="example-output-1">[3,4,5]</span>)
The returned node has value 3.  (The judge&#39;s serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,3,4,5,6]</span>
<strong>Output: </strong>Node 4 from this list (Serialization: <span id="example-output-2">[4,5,6]</span>)
Since the list has two middle nodes with values 3 and 4, we return the second one.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of nodes in the given list will be between <code>1</code>&nbsp;and <code>100</code>.</li>
</ul>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Output to Array

**Intuition and Algorithm**

Put every node into an array `A` in order.  Then the middle node is just `A[A.length // 2]`, since we can retrieve each node by index.

<iframe src="https://leetcode.com/playground/fsou5N8T/shared" frameBorder="0" width="100%" height="242" name="fsou5N8T"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given list.

* Space Complexity:  $$O(N)$$, the space used by `A`.
<br />
<br />


---
#### Approach 2: Fast and Slow Pointer

**Intuition and Algorithm**

When traversing the list with a pointer `slow`, make another pointer `fast` that traverses twice as fast.  When `fast` reaches the end of the list, `slow` must be in the middle.

<iframe src="https://leetcode.com/playground/brPhWpn3/shared" frameBorder="0" width="100%" height="259" name="brPhWpn3"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the given list.

* Space Complexity:  $$O(1)$$, the space used by `slow` and `fast`.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
