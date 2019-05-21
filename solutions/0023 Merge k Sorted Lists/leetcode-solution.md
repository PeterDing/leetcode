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




## Solution:

[TOC]
## Solution

---
#### Approach 1: Brute Force

**Intuition & Algorithm**

- Traverse all the linked lists and collect the values of the nodes into an array.
- Sort and iterate over this array to get the proper value of nodes.
- Create a new sorted linked list and extend it with the new nodes.

As for sorting, you can refer [here](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html) for more about sorting algorithms.

<iframe src="https://leetcode.com/playground/kCxLKUfQ/shared" frameBorder="0" width="100%" height="327" name="kCxLKUfQ"></iframe>

**Complexity Analysis**

* Time complexity : $$O(N\log N)$$ where $$N$$ is the total number of nodes.
    - Collecting all the values costs $$O(N)$$ time.
    - A stable sorting algorithm costs $$O(N\log N)$$ time.
    - Iterating for creating the linked list costs $$O(N)$$ time.


* Space complexity : $$O(N)$$.
    - Sorting cost $$O(N)$$ space (depends on the algorithm you choose).
    - Creating a new linked list costs $$O(N)$$ space.
<br />
<br />
---

#### Approach 2: Compare one by one

**Algorithm**

- Compare every $$\text{k}$$ nodes (head of every linked list) and get the node with the smallest value.
- Extend the final sorted linked list with the selected nodes.

!?!../Documents/23_Merge_lists.json:1000,563!?!

**Complexity Analysis**

* Time complexity : $$O(kN)$$ where $$\text{k}$$ is the number of linked lists.
    - Almost every selection of node in final linked costs $$O(k)$$ ($$\text{k-1}$$ times comparison).
    - There are $$N$$ nodes in the final linked list.


* Space complexity :
    - $$O(n)$$ Creating a new linked list costs $$O(n)$$ space.
    - $$O(1)$$ It's not hard to apply in-place method - connect selected nodes instead of creating new nodes to fill the new linked list.
<br />
<br />
---
#### Approach 3: Optimize Approach 2 by Priority Queue

**Algorithm**

Almost the same as the one above but optimize the **comparison process** by **priority queue**. You can refer [here](https://en.wikipedia.org/wiki/Priority_queue) for more information about it.

<iframe src="https://leetcode.com/playground/wnXfryCD/shared" frameBorder="0" width="100%" height="412" name="wnXfryCD"></iframe>

**Complexity Analysis**

* Time complexity : $$O(N\log k)$$ where $$\text{k}$$ is the number of linked lists.
    - The comparison cost will be reduced to $$O(\log k)$$ for every pop and insertion to priority queue. But finding the node with the smallest value just costs $$O(1)$$ time.
    - There are $$N$$ nodes in the final linked list.


* Space complexity :
    - $$O(n)$$ Creating a new linked list costs $$O(n)$$ space.
    - $$O(k)$$ The code above present applies in-place method which cost $$O(1)$$ space. And the priority queue (often implemented with heaps) costs $$O(k)$$ space (it's far less than $$N$$ in most situations).
<br />
<br />
---

#### Approach 4: Merge lists one by one

**Algorithm**

Convert merge $$\text{k}$$ lists problem to merge 2 lists ($$\text{k-1}$$) times. Here is the [merge 2 lists](https://leetcode.com/problems/merge-two-sorted-lists/description/) problem page.


**Complexity Analysis**

* Time complexity : $$O(kN)$$ where $$\text{k}$$ is the number of linked lists.
    - We can merge two sorted linked list in $$O(n)$$ time where $$n$$ is the total number of nodes in two lists.
    - Sum up the merge process and we can get:  $$O(\sum_{i=1}^{k-1} (i*(\frac{N}{k}) + \frac{N}{k})) = O(kN)$$.


* Space complexity : $$O(1)$$
    - We can merge two sorted linked list in $$O(1)$$ space.
<br />
<br />
---

#### Approach 5: Merge with Divide And Conquer

**Intuition & Algorithm**

This approach walks alongside the one above but is improved a lot. We don't need to traverse most nodes many times repeatedly

  - Pair up $$\text{k}$$ lists and merge each pair.

  - After the first pairing, $$\text{k}$$ lists are merged into $$k/2$$ lists with average $$2N/k$$ length, then $$k/4$$, $$k/8$$ and so on.

  -  Repeat this procedure until we get the final sorted linked list.

Thus, we'll traverse almost $$N$$ nodes per pairing and merging, and repeat this procedure about $$\log_{2}{k}$$  times.

![Divide_and_Conquer](../Figures/23/23_divide_and_conquer_new.png)
{align = "center"}


<iframe src="https://leetcode.com/playground/8nnKQ4tP/shared" frameBorder="0" width="100%" height="500" name="8nnKQ4tP"></iframe>

**Complexity Analysis**

* Time complexity : $$O(N\log k)$$ where $$\text{k}$$ is the number of linked lists.
    - We can merge two sorted linked list in $$O(n)$$ time where $$n$$ is the total number of nodes in two lists.
    - Sum up the merge process and we can get: $$O\big(\sum_{i=1}^{log_{2}{k}}N \big)= O(N\log k)$$


* Space complexity : $$O(1)$$
    - We can merge two sorted linked lists in $$O(1)$$ space.
