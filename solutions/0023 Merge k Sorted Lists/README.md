# 0023 - Merge k Sorted Lists

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Linked List, Divide and Conquer, Heap | [Leetcode](https://leetcode.com/problems/merge-k-sorted-lists) | [solution](https://leetcode.com/problems/merge-k-sorted-lists/solution/)

-----------

<p>Merge <em>k</em> sorted linked lists and return it as one sorted list. Analyze and describe its complexity.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
&nbsp; 1-&gt;4-&gt;5,
&nbsp; 1-&gt;3-&gt;4,
&nbsp; 2-&gt;6
]
<strong>Output:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>


-----------


## Similar Problems

- [Easy] [Merge Two Sorted Lists](merge-two-sorted-lists)

- [Medium] [Ugly Number II](ugly-number-ii)



## Thought:

- Merge one by one

We merge these list one by one.

Namely, we firstly merge K_i and K_i+1 as K_i+1, then recursively.

We notice the O is max(len(K_i), len(K_i+1)) after merging two list.

So, the O is sum(len(K_i)) after merging k lists.

- Improve merging one by one

We merge the k lists using diving and conquer.

(K_1, K_2) merged as K_2, (K_3, K_4) as K_4, ….

Then, (K_2, K_4) merge.

O(sum(len(K_i)) * logK)