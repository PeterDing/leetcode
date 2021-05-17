# 0024 - Swap Nodes in Pairs

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Linked List | [Leetcode](https://leetcode.com/problems/swap-nodes-in-pairs) | [solution](https://leetcode.com/problems/swap-nodes-in-pairs/solution/)

-----------

<p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head.</p>

<p>You may <strong>not</strong> modify the values in the list&#39;s nodes, only nodes itself may be changed.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
Given <code>1-&gt;2-&gt;3-&gt;4</code>, you should return the list as <code>2-&gt;1-&gt;4-&gt;3</code>.
</pre>


-----------


## Similar Problems

- [Hard] [Reverse Nodes in k-Group](reverse-nodes-in-k-group)



## Thought:

Procedure:

e -> a -> b -> c

1. e -> b
2. a -> c
3. b -> a
