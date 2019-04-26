# 0701 - Insert into a Binary Search Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/insert-into-a-binary-search-tree) | [solution](https://leetcode.com/problems/insert-into-a-binary-search-tree/solution/)


-----------

<p>Given the root node of a binary search tree (BST) and a value to be inserted into the tree,&nbsp;insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.</p>

<p>Note that there may exist&nbsp;multiple valid ways for the&nbsp;insertion, as long as the tree remains a BST after insertion. You can return any of them.</p>

<p>For example,&nbsp;</p>

<pre>
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
</pre>

<p>You can return this binary search tree:</p>

<pre>
         4
       /   \
      2     7
     / \   /
    1   3 5
</pre>

<p>This tree is also valid:</p>

<pre>
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
</pre>


-----------


## Similar Problems

- [Easy] [Search in a Binary Search Tree](search-in-a-binary-search-tree)




## Solution:

[TOC]

## Solution

--- 

#### Intuition

One of the huge BST advantages over the [heap](https://en.wikipedia.org/wiki/Heap_(data_structure)#Implementation) 
is a [search](https://leetcode.com/problems/search-in-a-binary-search-tree/) 
for _arbitrary_ element in $$\mathcal{O}(\log N)$$ time even in the worst case.
Here we'll see that the insert time is $$\mathcal{O}(\log N)$$ too,
both for the average and worst cases. 
To compare with the [heap](https://en.wikipedia.org/wiki/Heap_(data_structure)#Implementation) again :
the average heap insert is $$\mathcal{O}(1)$$, and the worst heap insert is
 $$\mathcal{O}(N)$$.

The problem solution is very simple - one could always insert new node as a child of the leaf.
To define which leaf to use, one could follow the standard BST logic :

- If `val > node.val` - go to insert into the right subtree.

- If `val < node.val` - go to insert into the left subtree.

![bla](../Figures/701/insert.png)

<br />
<br />


---
#### Approach 1: Recursion

The recursion implementation is very straightforward :

- If `root` is null - return `TreeNode(val)`.

- If `val > root.val` - go to insert into the right subtree.

- If `val < root.val` - go to insert into the left subtree.

- Return `root`.

!?!../Documents/701_LIS.json:1000,420!?!

<iframe src="https://leetcode.com/playground/xfMJKaeK/shared" frameBorder="0" width="100%" height="259" name="xfMJKaeK"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(\log N)$$. 

    Let's compute time complexity with the help of 
    [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) 
    $$T(N) = aT\left(\frac{N}{b}\right) + \Theta(N^d)$$.
    The equation represents dividing the problem 
    up into $$a$$ subproblems of size $$\frac{N}{b}$$ in $$\Theta(N^d)$$ time. 
    Here at step there is only one subproblem `a = 1`, its size 
    is a half of the initial problem `b = 2`, 
    and all this happens in a constant time `d = 0`, as for
    the binary search.
    That means that $$\log_b{a} = d$$ and hence we're dealing with 
    [case 2](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)#Case_2_example)
    that results in $$\mathcal{O}(n^{\log_b{a}} \log^{d + 1} N)$$
    = $$\mathcal{O}(\log N)$$ time complexity.
    
* Space complexity : $$\mathcal{O}(\log N)$$ to keep the recursion stack.

<br />
<br />


---
#### Approach 2: Iteration

The recursion above could be converted into the iteration

<iframe src="https://leetcode.com/playground/CSYR7FLU/shared" frameBorder="0" width="100%" height="497" name="CSYR7FLU"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(\log N)$$. 

    Let's compute time complexity with the help of 
    [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) 
    $$T(N) = aT\left(\frac{N}{b}\right) + \Theta(N^d)$$.
    The equation represents dividing the problem 
    up into $$a$$ subproblems of size $$\frac{N}{b}$$ in $$\Theta(N^d)$$ time. 
    Here at step there is only one subproblem `a = 1`, its size 
    is a half of the initial problem `b = 2`, 
    and all this happens in a constant time `d = 0`, as for
    the binary search.
    That means that $$\log_b{a} = d$$ and hence we're dealing with 
    [case 2](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)#Case_2_example)
    that results in $$\mathcal{O}(n^{\log_b{a}} \log^{d + 1} N)$$
    = $$\mathcal{O}(\log N)$$ time complexity.
    
* Space complexity : $$\mathcal{O}(1)$$ since it's a constant space
solution.

Analysis written by @[liaison](https://leetcode.com/liaison/)
and @[andvary](https://leetcode.com/andvary/)
