# 0287 - Find the Duplicate Number

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Two Pointers, Binary Search | [Leetcode](https://leetcode.com/problems/find-the-duplicate-number) | [solution](https://leetcode.com/problems/find-the-duplicate-number/solution/)


-----------

<p>Given an array <i>nums</i> containing <i>n</i> + 1 integers where each integer is between 1 and <i>n</i> (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>[1,3,4,2,2]</code>
<b>Output:</b> 2
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [3,1,3,4,2]
<b>Output:</b> 3</pre>

<p><b>Note:</b></p>

<ol>
	<li>You <b>must not</b> modify the array (assume the array is read only).</li>
	<li>You must use only constant, <i>O</i>(1) extra space.</li>
	<li>Your runtime complexity should be less than <em>O</em>(<em>n</em><sup>2</sup>).</li>
	<li>There is only one duplicate number in the array, but it could be repeated more than once.</li>
</ol>


-----------


## Similar Problems

- [Hard] [First Missing Positive](first-missing-positive)

- [Easy] [Single Number](single-number)

- [Medium] [Linked List Cycle II](linked-list-cycle-ii)

- [Easy] [Missing Number](missing-number)

- [Easy] [Set Mismatch](set-mismatch)




## Solution:

[TOC]

#### Note #####

The first two approaches mentioned do not satisfy the constraints given in
the prompt, but they are solutions that you might be likely to come up with
during a technical interview. As an interviewer, I personally would _not_
expect someone to come up with the cycle detection solution unless they have
heard it before.

#### Proof ####

Proving that at least one duplicate must exist in `nums` is simple
application of the
[pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle).
Here, each number in `nums` is a "pigeon" and each distinct number that can
appear in `nums` is a "pigeonhole". Because there are $$n+1$$ numbers are
$$n$$ distinct possible numbers, the pigeonhole principle implies that at
least one of the numbers is duplicated.

#### Approach #1 Sorting [Accepted]

**Intuition**

If the numbers are sorted, then any duplicate numbers will be adjacent in the
sorted array.

**Algorithm**

Given the intuition, the algorithm follows fairly simply. First, we sort the
array, and then we compare each element to the previous element. Because
there is exactly one duplicated element in the array, we know that the array
is of at least length 2, and we can return the duplicate element as soon as
we find it.

<iframe src="https://leetcode.com/playground/bQGYqfgj/shared" frameBorder="0" width="100%" height="259" name="bQGYqfgj"></iframe>

**Complexity Analysis**

* Time complexity : $$O(nlgn)$$

    The `sort` invocation costs $$O(nlgn)$$ time in Python and Java, so it
    dominates the subsequent linear scan.

* Space complexity : $$O(1)$$ (or $$O(n)$$)

    Here, we sort `nums` in place, so the memory footprint is constant. If we
    cannot modify the input array, then we must allocate linear space for a
    copy of `nums` and sort that instead.

---

#### Approach #2 Set [Accepted]

**Intuition**

If we store each element as we iterate over the array, we can simply check
each element as we iterate over the array.

**Algorithm**

In order to achieve linear time complexity, we need to be able to insert
elements into a data structure (and look them up) in constant time. A `Set`
satisfies these constraints nicely, so we iterate over the array and insert
each element into `seen`. Before inserting it, we check whether it is already
there. If it is, then we found our duplicate, so we return it.

<iframe src="https://leetcode.com/playground/jP4YUkB7/shared" frameBorder="0" width="100%" height="276" name="jP4YUkB7"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$

    `Set` in both Python and Java rely on underlying hash tables, so
    insertion and lookup have amortized constant time complexities. The
    algorithm is therefore linear, as it consists of a `for` loop that
    performs constant work $$n$$ times.

* Space complexity : $$O(n)$$

    In the worst case, the duplicate element appears twice, with one of its
    appearances at array index $$n-1$$. In this case, `seen` will contain
    $$n-1$$ distinct values, and will therefore occupy $$O(n)$$ space.

---

#### Approach #3 Floyd's Tortoise and Hare (Cycle Detection) [Accepted]

**Intuition**

If we interpret `nums` such that for each pair of index $$i$$ and value
$$v_i$$, the "next" value $$v_j$$ is at index $$v_i$$, we can reduce this
problem to cycle detection. See the solution to
[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/solution/)
for more details.

**Algorithm**

First off, we can easily show that the constraints of the problem imply that
a cycle _must_ exist. Because each number in `nums` is between $$1$$ and
$$n$$, it will necessarily point to an index that exists. Therefore, the list
can be traversed infinitely, which implies that there is a cycle.
Additionally, because $$0$$ cannot appear as a value in `nums`, `nums[0]`
cannot be part of the cycle. Therefore, traversing the array in this manner
from `nums[0]` is equivalent to traversing a cyclic linked list. Given this,
the problem can be solved just like
[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/).

To see the algorithm in action, check out the animation below:

!?!../Documents/287_Find_the_Duplicate_Number.json:1280,720!?!

<iframe src="https://leetcode.com/playground/RMBz6AQR/shared" frameBorder="0" width="100%" height="412" name="RMBz6AQR"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$

    For detailed analysis, refer to 
    [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/solution/#approach-2-floyds-tortoise-and-hare-accepted).
    

* Space complexity : $$O(1)$$

    For detailed analysis, refer to 
    [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/solution/#approach-2-floyds-tortoise-and-hare-accepted).
    

---

Analysis and solutions written by: [@emptyset](https://leetcode.com/emptyset)
