# 0083 - Remove Duplicates from Sorted List

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Linked List | [Leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list) | [solution](https://leetcode.com/problems/remove-duplicates-from-sorted-list/solution/)


-----------

<p>Given a sorted linked list, delete all duplicates such that each element appear only <em>once</em>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;1-&gt;2
<strong>Output:</strong> 1-&gt;2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;3
<strong>Output:</strong> 1-&gt;2-&gt;3
</pre>


-----------


## Similar Problems

- [Medium] [Remove Duplicates from Sorted List II](remove-duplicates-from-sorted-list-ii)




## Solution:

## Solution
---

#### Approach 1: Straight-Forward Approach

**Algorithm**

This is a simple problem that merely tests your ability to manipulate list node pointers. Because the input list is sorted, we can determine if a node is a duplicate by comparing its value to the node *after* it in the list. If it is a duplicate, we change the ````next```` pointer of the current node so that it skips the next node and points directly to the one after the next node.

<iframe src="https://leetcode.com/playground/KHvbA6CF/shared" frameBorder="0" width="100%" height="242" name="KHvbA6CF"></iframe>


**Complexity Analysis**

* Time complexity : $$O(n)$$. Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is $$O(n)$$, where $$n$$ is the number of nodes in the list.

* Space complexity : $$O(1)$$. No additional space is used.

**Correctness**

We can prove the correctness of this code by defining a *loop invariant*. A loop invariant is condition that is true before and after every iteration of the loop. In this case, a loop invariant that helps us prove correctness is this:

> All nodes in the list up to the pointer `current` do not contain duplicate elements.

We can prove that this condition is indeed a loop invariant by induction. Before going into the loop, `current` points to the head of the list. Therefore, the part of the list up to `current` contains only the head. And so it can not contain any duplicate elements. Now suppose `current` is now pointing to some node in the list (but not the last element), and the part of the list up to `current` contains no duplicate elements. After another loop iteration, one of two things happen.

1. `current.next` was a duplicate of `current`. In this case, the duplicate node at `current.next` is deleted, and `current` stays pointing to the same node as before. Therefore, the condition still holds; there are still no duplicates up to `current`.

2. `current.next` was not a duplicate of `current` (and, because the list is sorted, `current.next` is also not a duplicate of any other element appearing *before* `current`). In this case, `current` moves forward one step to point to `current.next`. Therefore, the condition still holds; there are no duplicates up to `current`.


At the last iteration of the loop, `current` must point to the last element, because afterwards, `current.next = null`. Therefore, after the loop ends, all elements up to the last element do not contain duplicates.
