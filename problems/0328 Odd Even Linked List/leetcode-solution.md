# 0328 - Odd Even Linked List

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Linked List | [Leetcode](https://leetcode.com/problems/odd-even-linked-list) | [solution](https://leetcode.com/problems/odd-even-linked-list/solution/)


-----------

<p>Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.</p>

<p>You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong><code>1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL</code>
<strong>Output: </strong><code>1-&gt;3-&gt;5-&gt;2-&gt;4-&gt;NULL</code>
</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input: </strong>2<code>-&gt;1-&gt;3-&gt;5-&gt;6-&gt;4-&gt;7-&gt;NULL</code>
<strong>Output: </strong><code>2-&gt;3-&gt;6-&gt;7-&gt;1-&gt;5-&gt;4-&gt;NULL</code>
</pre>

<p><b>Note:</b></p>

<ul>
	<li>The relative order inside both the even and odd groups should remain as it was in the input.</li>
	<li>The first node is considered odd, the second node even and so on ...</li>
</ul>


-----------


## Similar Problems

- [Medium] [Split Linked List in Parts](split-linked-list-in-parts)




## Solution:

## Solution

**Intuition**

Put the odd nodes in a linked list and the even nodes in another. Then link the evenList to the tail of the oddList.

**Algorithm**

The solution is very intuitive. But it is not trivial to write a concise and bug-free code.

A well-formed `LinkedList` need two pointers head and tail to support operations at both ends. The variables `head` and `odd` are the head pointer and tail pointer of one `LinkedList` we call oddList; the variables `evenHead` and `even` are the head pointer and tail pointer of another `LinkedList` we call evenList. The algorithm traverses the original LinkedList and put the odd nodes into the oddList and the even nodes into the evenList. To traverse a LinkedList we need at least one pointer as an iterator for the current node. But here the pointers `odd` and `even` not only serve as the tail pointers but also act as the iterators of the original list.

The best way of solving any linked list problem is to visualize it either in your mind or on a piece of paper. An illustration of our algorithm is following:

![Illustration of odd even linked list](../Figures/328_Odd_Even.svg "Odd Even Linked List"){:width="539px"}
{:align="center"}

*Figure 1. Step by step example of the odd and even linked list.*
{:align="center"}


<iframe src="https://leetcode.com/playground/hwsGSV9j/shared" frameBorder="0" width="100%" height="293" name="hwsGSV9j"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. There are total $$n$$ nodes and we visit each node once.

* Space complexity : $$O(1)$$. All we need is the four pointers.
