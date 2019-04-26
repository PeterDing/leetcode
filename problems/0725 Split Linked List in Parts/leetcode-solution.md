# 0725 - Split Linked List in Parts

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Linked List | [Leetcode](https://leetcode.com/problems/split-linked-list-in-parts) | [solution](https://leetcode.com/problems/split-linked-list-in-parts/solution/)


-----------

<p>Given a (singly) linked list with head node <code>root</code>, write a function to split the linked list into <code>k</code> consecutive linked list "parts".
</p><p>
The length of each part should be as equal as possible: no two parts should have a size differing by more than 1.  This may lead to some parts being null.
</p><p>
The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.
</p><p>
Return a List of ListNode's representing the linked list parts that are formed.
</p>

Examples
1->2->3->4, k = 5 // 5 equal parts
[ [1], 
[2],
[3],
[4],
null ]

<p><b>Example 1:</b><br />
<pre style="white-space: pre-line">
<b>Input:</b> 
root = [1, 2, 3], k = 5
<b>Output:</b> [[1],[2],[3],[],[]]
<b>Explanation:</b>
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
<b>Output:</b> [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
<b>Explanation:</b>
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>root</code> will be in the range <code>[0, 1000]</code>.</li>
<li>Each value of a node in the input will be an integer in the range <code>[0, 999]</code>.</li>
<li><code>k</code> will be an integer in the range <code>[1, 50]</code>.</li>
</p>

-----------


## Similar Problems

- [Medium] [Rotate List](rotate-list)

- [Medium] [Odd Even Linked List](odd-even-linked-list)




## Solution:

[TOC]

#### Approach #1: Create New Lists [Accepted]

**Intuition and Algorithm**

If there are $$N$$ nodes in the linked list `root`, then there are $$N / k$$ items in each part, plus the first $$N \% k$$ parts have an extra item.  We can count $$N$$ with a simple loop.

Now for each part, we have calculated how many nodes that part will have: `width + (i < remainder ? 1 : 0)`.  We create a new list and write the part to that list.

Our solution showcases constructs of the form `a = b = c`.  Note that this syntax behaves differently for different languages.

<iframe src="https://leetcode.com/playground/mPv7qf7R/shared" frameBorder="0" width="100%" height="463" name="mPv7qf7R"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N + k)$$, where $$N$$ is the number of nodes in the given list.  If $$k$$ is large, it could still require creating many new empty lists.

* Space Complexity: $$O(max(N, k))$$, the space used in writing the answer.

---
#### Approach #2: Split Input List [Accepted]

**Intuition and Algorithm**

As in *Approach #1*, we know the size of each part.  Instead of creating new lists, we will split the input list directly and return a list of pointers to nodes in the original list as appropriate.

Our solution proceeds similarly.  For a part of size `L = width + (i < remainder ? 1 : 0)`, instead of stepping `L` times, we will step `L-1` times, and our final time will also sever the link between the last node from the previous part and the first node from the next part.

<iframe src="https://leetcode.com/playground/RmD7xooU/shared" frameBorder="0" width="100%" height="500" name="RmD7xooU"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N + k)$$, where $$N$$ is the number of nodes in the given list.  If $$k$$ is large, it could still require creating many new empty lists.

* Space Complexity: $$O(k)$$, the additional space used in writing the answer.

---

Analysis written by: [@awice](https://leetcode.com/awice).
