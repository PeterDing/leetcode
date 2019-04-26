# 0237 - Delete Node in a Linked List

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Linked List | [Leetcode](https://leetcode.com/problems/delete-node-in-a-linked-list) | [solution](https://leetcode.com/problems/delete-node-in-a-linked-list/solution/)


-----------

<p>Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.</p>

<p>Given linked list --&nbsp;head =&nbsp;[4,5,1,9], which looks like following:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/28/237_example.png" style="margin-top: 5px; margin-bottom: 5px; width: 300px; height: 49px;" /></p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> head = [4,5,1,9], node = 5
<strong>Output:</strong> [4,1,9]
<strong>Explanation: </strong>You are given the second node with value 5, the linked list should become 4 -&gt; 1 -&gt; 9 after calling your function.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [4,5,1,9], node = 1
<strong>Output:</strong> [4,5,9]
<strong>Explanation: </strong>You are given the third node with value 1, the linked list should become 4 -&gt; 5 -&gt; 9 after calling your function.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The linked list will have at least two elements.</li>
	<li>All of the nodes&#39; values will be unique.</li>
	<li>The given node&nbsp;will not be the tail and it will always be a valid node of the linked list.</li>
	<li>Do not return anything from your function.</li>
</ul>


-----------


## Similar Problems

- [Easy] [Remove Linked List Elements](remove-linked-list-elements)




## Solution:

## Solution

#### Approach: Swap with Next Node [Accepted]

The usual way of deleting a node `node` from a linked list is to modify the `next` pointer of the node *before* it, to point to the node *after* it.

<img src= "https://leetcode.com/media/original_images/237_LinkedList.png" width="400" />

Since we do not have access to the node *before* the one we want to delete, we cannot modify the `next` pointer of that node in any way. Instead, we have to replace the value of the node we want to delete with the value in the node after it, and then delete the node after it.

<img src="https://leetcode.com/media/original_images/237_LinkedList2.png" width="400" />

<img src="https://leetcode.com/media/original_images/237_LinkedList3.png" width="400" />

<img src="https://leetcode.com/media/original_images/237_LinkedList4.png" width="330" />

Because we know that the node we want to delete is not the tail of the list, we can guarantee that this approach is possible.

**Java**

```java
public void deleteNode(ListNode node) {
    node.val = node.next.val;
    node.next = node.next.next;
}
```

**Complexity Analysis**

Time and space complexity are both $$O(1)$$.

Analysis written by: @noran
