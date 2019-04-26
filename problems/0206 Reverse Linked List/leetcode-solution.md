# 0206 - Reverse Linked List

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Linked List | [Leetcode](https://leetcode.com/problems/reverse-linked-list) | [solution](https://leetcode.com/problems/reverse-linked-list/solution/)


-----------

<p>Reverse a singly linked list.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL
<strong>Output:</strong> 5-&gt;4-&gt;3-&gt;2-&gt;1-&gt;NULL
</pre>

<p><b>Follow up:</b></p>

<p>A linked list can be reversed either iteratively or recursively. Could you implement both?</p>


-----------


## Similar Problems

- [Medium] [Reverse Linked List II](reverse-linked-list-ii)

- [Medium] [Binary Tree Upside Down](binary-tree-upside-down)

- [Easy] [Palindrome Linked List](palindrome-linked-list)




## Solution:

[TOC]

## Solution
---
#### Approach #1 (Iterative) [Accepted]

Assume that we have linked list `1 → 2 → 3 → Ø`, we would like to change it to `Ø ← 1 ← 2 ← 3`.

While you are traversing the list, change the current node's next pointer to point to its previous element. Since a node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. Do not forget to return the new head reference at the end!

```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}
```

**Complexity analysis**

* Time complexity : $$O(n)$$.
Assume that $$n$$ is the list's length, the time complexity is $$O(n)$$.

* Space complexity : $$O(1)$$.

---
#### Approach #2 (Recursive) [Accepted]

The recursive version is slightly trickier and the key is to work backwards. Assume that the rest of the list had already been reversed, now how do I reverse the front part? Let's assume the list is: n<sub>1</sub> → … → n<sub>k-1</sub> → n<sub>k</sub> → n<sub>k+1</sub> → … → n<sub>m</sub> → Ø

Assume from node n<sub>k+1</sub> to n<sub>m</sub> had been reversed and you are at node n<sub>k</sub>.

n<sub>1</sub> → … → n<sub>k-1</sub> → <b>n<sub>k</sub></b> → n<sub>k+1</sub> ← … ← n<sub>m</sub>

We want n<sub>k+1</sub>’s next node to point to n<sub>k</sub>.

So,

n<sub>k</sub>.next.next = n<sub>k</sub>;

Be very careful that n<sub>1</sub>'s next must point to Ø. If you forget about this, your linked list has a cycle in it. This bug could be caught if you test your code with a linked list of size 2.


```java
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}
```

**Complexity analysis**

* Time complexity : $$O(n)$$.
Assume that $$n$$ is the list's length, the time complexity is $$O(n)$$.

* Space complexity : $$O(n)$$.
The extra space comes from implicit stack space due to recursion. The recursion could go up to $$n$$ levels deep.
