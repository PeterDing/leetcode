# 0707 - Design Linked List

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Linked List, Design | [Leetcode](https://leetcode.com/problems/design-linked-list) | [solution](https://leetcode.com/problems/design-linked-list/solution/)


-----------

<p>Design your&nbsp;implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly&nbsp;linked list should have two attributes: <code>val</code>&nbsp;and <code>next</code>. <code>val</code> is the value of the current node, and <code>next</code>&nbsp;is&nbsp;a&nbsp;pointer/reference to the next node. If you want to use the doubly linked list,&nbsp;you will need&nbsp;one more attribute <code>prev</code> to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.</p>

<p>Implement these functions in your linked list class:</p>

<ul>
	<li>get(index) : Get the value of&nbsp;the <code>index</code>-th&nbsp;node in the linked list. If the index is invalid, return <code>-1</code>.</li>
	<li>addAtHead(val) : Add a node of value <code>val</code>&nbsp;before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.</li>
	<li>addAtTail(val) : Append a node of value <code>val</code>&nbsp;to the last element of the linked list.</li>
	<li>addAtIndex(index, val) : Add a node of value <code>val</code>&nbsp;before the <code>index</code>-th&nbsp;node in the linked list.&nbsp;If <code>index</code>&nbsp;equals&nbsp;to the length of&nbsp;linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.</li>
	<li>deleteAtIndex(index) : Delete&nbsp;the <code>index</code>-th&nbsp;node in the linked list, if the index is valid.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1-&gt;2-&gt;3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1-&gt;3
linkedList.get(1);&nbsp;&nbsp;&nbsp;         // returns 3
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>All values will be in the range of <code>[1, 1000]</code>.</li>
	<li>The number of operations will be in the range of&nbsp;<code>[1, 1000]</code>.</li>
	<li>Please do not use the built-in LinkedList library.</li>
</ul>


-----------


## Similar Problems




## Thought:
