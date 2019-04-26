# 0094 - Binary Tree Inorder Traversal

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table, Stack, Tree | [Leetcode](https://leetcode.com/problems/binary-tree-inorder-traversal) | [solution](https://leetcode.com/problems/binary-tree-inorder-traversal/solution/)


-----------

<p>Given a binary tree, return the <em>inorder</em> traversal of its nodes&#39; values.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,null,2,3]
   1
    \
     2
    /
   3

<strong>Output:</strong> [1,3,2]</pre>

<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>


-----------


## Similar Problems

- [Medium] [Validate Binary Search Tree](validate-binary-search-tree)

- [Medium] [Binary Tree Preorder Traversal](binary-tree-preorder-traversal)

- [Hard] [Binary Tree Postorder Traversal](binary-tree-postorder-traversal)

- [Medium] [Binary Search Tree Iterator](binary-search-tree-iterator)

- [Medium] [Kth Smallest Element in a BST](kth-smallest-element-in-a-bst)

- [Hard] [Closest Binary Search Tree Value II](closest-binary-search-tree-value-ii)

- [Medium] [Inorder Successor in BST](inorder-successor-in-bst)

- [Medium] [Convert Binary Search Tree to Sorted Doubly Linked List](convert-binary-search-tree-to-sorted-doubly-linked-list)

- [Easy] [Minimum Distance Between BST Nodes](minimum-distance-between-bst-nodes)




## Solution:

[TOC]

## Solution

---
#### Approach 1: Recursive Approach

The first method to solve this problem is using recursion.
This is the classical method and is straightforward. We can define a helper function to implement recursion.

<iframe src="https://leetcode.com/playground/stzQZusR/shared" frameBorder="0" width="100%" height="378" name="stzQZusR"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. The time complexity is $$O(n)$$ because the recursive function is $$T(n) = 2 \cdot T(n/2)+1$$.

* Space complexity : The worst case space required is $$O(n)$$, and in the average case it's $$O(\log n)$$ where $$ n$$ is number of nodes.
<br />
<br />
---
#### Approach 2: Iterating method using Stack

The strategy is very similiar to the first method, the different is using stack.

Here is an illustration:

!?!../Documents/94_Binary.json:1000,563!?!

<iframe src="https://leetcode.com/playground/C9344qJ6/shared" frameBorder="0" width="100%" height="344" name="C9344qJ6"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$.

* Space complexity : $$O(n)$$.
<br />
<br />
---
#### Approach 3: Morris Traversal


In this method, we have to use a new data structure-Threaded Binary Tree, and the strategy is as follows:


>Step 1: Initialize current as root
>
>Step 2: While current is not NULL,
>
>     If current does not have left child
>
>         a. Add current’s value
>
>         b. Go to the right, i.e., current = current.right
>
>     Else
>
>         a. In current's left subtree, make current the right child of the rightmost node
>
>         b. Go to this left child, i.e., current = current.left


For example:
```

          1
        /   \
       2     3
      / \   /
     4   5 6

```
First, 1 is the root, so initialize 1 as current, 1 has left child which is 2, the current's left subtree is

```
         2
        / \
       4   5
```
 So in this subtree, the rightmost node is 5, then make the current(1) as the right child of 5. Set current = cuurent.left (current = 2).
The tree now looks like:
```
         2
        / \
       4   5
            \
             1
              \
               3
              /
             6
```
For current 2, which has left child 4, we can continue with thesame process as we did above
```
        4
         \
          2
           \
            5
             \
              1
               \
                3
               /
              6
```
 then add 4 because it has no left child, then add 2, 5, 1, 3 one by one, for node 3 which has left child 6, do the same as above.
Finally, the inorder taversal is [4,2,5,1,6,3].

For more details, please check
[Threaded binary tree](https://en.wikipedia.org/wiki/Threaded_binary_tree) and
[Explaination of Morris Method](https://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion)


<iframe src="https://leetcode.com/playground/osLqwuNN/shared" frameBorder="0" width="100%" height="446" name="osLqwuNN"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. To prove that the time complexity is $$O(n)$$,
the biggest problem lies in finding the time complexity of finding the predecessor nodes of all the nodes in the binary tree.
Intuitively, the complexity is $$O(n\log n)$$, because to find the predecessor node for a single node related to the height of the tree.
But in fact, finding the predecessor nodes for all nodes only needs $$O(n)$$ time. Because a binary Tree with $$n$$ nodes has $$n-1$$ edges, the whole processing for each edges up to 2 times, one is to locate a node, and the other is to find the predecessor node.
So the complexity is $$O(n)$$.

* Space complexity : $$O(n)$$. Arraylist of size $$n$$ is used.
