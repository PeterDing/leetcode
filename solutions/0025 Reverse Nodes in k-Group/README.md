# 0025 - Reverse Nodes in k-Group

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Linked List | [Leetcode](https://leetcode.com/problems/reverse-nodes-in-k-group) | [solution](https://leetcode.com/problems/reverse-nodes-in-k-group/solution/)

-----------

<p>Given a linked list, reverse the nodes of a linked list <em>k</em> at a time and return its modified list.</p>

<p><em>k</em> is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of <em>k</em> then left-out nodes in the end should remain as it is.</p>

<ul>
</ul>

<p><strong>Example:</strong></p>

<p>Given this linked list: <code>1-&gt;2-&gt;3-&gt;4-&gt;5</code></p>

<p>For <em>k</em> = 2, you should return: <code>2-&gt;1-&gt;4-&gt;3-&gt;5</code></p>

<p>For <em>k</em> = 3, you should return: <code>3-&gt;2-&gt;1-&gt;4-&gt;5</code></p>

<p><strong>Note:</strong></p>

<ul>
	<li>Only constant extra memory is allowed.</li>
	<li>You may not alter the values in the list&#39;s nodes, only nodes itself may be changed.</li>
</ul>


-----------


## Similar Problems

- [Medium] [Swap Nodes in Pairs](swap-nodes-in-pairs)




## Thought:

Procedure:

X -> a -> b -> e -> f -> Y

1. Reverse a -> b -> e -> f

   1. Use 3 pointer, as p1, p2, p3 point to a, b, e.

      b -> a, then move p1 to back of p3 and point to f (p3.next)

   2. reversive

2. p1 = X.next, X -> p3
3. p1 -> Y
4. done