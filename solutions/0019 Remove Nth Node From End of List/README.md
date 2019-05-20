# 0019 - Remove Nth Node From End of List

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Linked List, Two Pointers | [Leetcode](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | [solution](https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/)

-----------

<p>Given a linked list, remove the <em>n</em>-th node from the end of list and return its head.</p>

<p><strong>Example:</strong></p>

<pre>
Given linked list: <strong>1-&gt;2-&gt;3-&gt;4-&gt;5</strong>, and <strong><em>n</em> = 2</strong>.

After removing the second node from the end, the linked list becomes <strong>1-&gt;2-&gt;3-&gt;5</strong>.
</pre>

<p><strong>Note:</strong></p>

<p>Given <em>n</em> will always be valid.</p>

<p><strong>Follow up:</strong></p>

<p>Could you do this in one pass?</p>

-----------


## Similar Problems



## Thought:

- Two steps

1. Find the length of array, N.
2. Remove the nth node from end.



- One step

1. Use two pointers, p1, p2.
2. the distance of p1 and p2 is less equal n.
3. If at next iter p2 reach the end using i step, then the nth node is p1 + i