# 0086 - Partition List

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Linked List, Two Pointers | [Leetcode](https://leetcode.com/problems/partition-list) | [solution](https://leetcode.com/problems/partition-list/solution/)


-----------

<p>Given a linked list and a value <em>x</em>, partition it such that all nodes less than <em>x</em> come before nodes greater than or equal to <em>x</em>.</p>

<p>You should preserve the original relative order of the nodes in each of the two partitions.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> head = 1-&gt;4-&gt;3-&gt;2-&gt;5-&gt;2, <em>x</em> = 3
<strong>Output:</strong> 1-&gt;2-&gt;2-&gt;4-&gt;3-&gt;5
</pre>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution

The problem wants us to reform the linked list structure, such that the
elements lesser that a certain value `x`, come before the elements greater or
equal to `x`. This essentially means in this reformed list, there would be a
point in the linked list `before` which all the elements would be smaller than
`x` and `after` which all the elements would be greater or equal to `x`.
Let's call this point as the `JOINT`.

<center>
<img src="../Figures/86/86_Partition_List_1.png" width="700"/>
</center>

Reverse engineering the question tells us that if we break the reformed list
at the `JOINT`, we will get two smaller linked lists, one with lesser elements
and the other with elements greater or equal to `x`. In the solution, our main aim
is to create these two linked lists and join them.

#### Approach 1: Two Pointer Approach

**Intuition**

We can take two pointers `before` and `after` to keep track of the two linked
lists as described above. These two pointers could be
used two create two separate lists and then these lists could be combined to
form the desired reformed list.

**Algorithm**

1. Initialize two pointers `before` and `after`. In the implementation we have
initialized these two with a dummy `ListNode`. This helps to reduce the number
of conditional checks we would need otherwise. You can try an implementation
where you don't initialize with a dummy node and see it yourself!

    <center>
    <img src="../Figures/86/86_Partition_List_2.png" width="400"/>
    </center>
    <center>Dummy Node Initialization</center><br/>

2. Iterate the original linked list, using the `head` pointer.
3. If the node's value pointed by `head` is *lesser* than `x`, the node should
be part of the `before` list. So we move it to `before` list.

    <center>
    <img src="../Figures/86/86_Partition_List_3.png" width="700"/>
    </center>

4. Else, the node should be part of `after` list. So we move it to `after` list.

    <center>
    <img src="../Figures/86/86_Partition_List_4.png" width="700"/>
    </center>

5. Once we are done with all the nodes in the original linked list, we would
have two list `before` and `after`. The original list nodes are either part of
`before` list or `after` list, depending on its value.

    <center>
    <img src="../Figures/86/86_Partition_List_5.png" width="700"/>
    </center>

    *`Note:` Since we traverse the original linked list from left to right,
    at no point would the order of nodes change relatively in the two lists. Another important thing to note here is that we show the original linked list intact in the above diagrams. However, in the implementation, we remove the nodes from the original linked list and attach them in the before or after list. We don't utilize any additional space. We simply move the nodes from the original list around.*

6. Now, these two lists `before` and `after` can be combined to form the reformed list.

    <center>
    <img src="../Figures/86/86_Partition_List_6.png" width="700"/>
    </center>

We did a dummy node initialization at the start to make implementation
easier, you don't want that to be part of the returned list, hence just
move ahead one node in both the lists while combining the two list. Since both
before and after have an extra node at the front.

<iframe src="https://leetcode.com/playground/EjKysw9Z/shared" frameBorder="0" width="100%" height="500" name="EjKysw9Z"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of nodes in the original
linked list and we iterate the original list.
* Space Complexity: $$O(1)$$, we have not utilized any extra space, the point to
note is that we are reforming the original list, by moving the original nodes, we
have not used any extra space as such.

---
Analysis written by: [@godayaldivya](https://leetcode.com/godayaldivya/).
