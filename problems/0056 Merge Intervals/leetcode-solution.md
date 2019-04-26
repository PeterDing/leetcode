# 0056 - Merge Intervals

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Sort | [Leetcode](https://leetcode.com/problems/merge-intervals) | [solution](https://leetcode.com/problems/merge-intervals/solution/)


-----------

<p>Given a collection of intervals, merge all overlapping intervals.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.</pre>

<p><strong>NOTE:</strong>&nbsp;input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</p>


-----------


## Similar Problems

- [Hard] [Insert Interval](insert-interval)

- [Easy] [Meeting Rooms](meeting-rooms)

- [Medium] [Meeting Rooms II](meeting-rooms-ii)

- [Medium] [Teemo Attacking](teemo-attacking)

- [Medium] [Add Bold Tag in String](add-bold-tag-in-string)

- [Hard] [Range Module](range-module)

- [Hard] [Employee Free Time](employee-free-time)

- [Medium] [Partition Labels](partition-labels)

- [Medium] [Interval List Intersections](interval-list-intersections)




## Solution:

[TOC]

## Solution

---

#### Approach 1: Connected Components

**Intuition**

If we draw a graph (with intervals as nodes) that contains undirected edges
between all pairs of intervals that overlap, then all intervals in each
*connected component* of the graph can be merged into a single interval.

**Algorithm**

With the above intuition in mind, we can represent the graph as an adjacency
list, inserting directed edges in both directions to simulate undirected
edges. Then, to determine which connected component each node is it, we
perform graph traversals from arbitrary unvisited nodes until all nodes have
been visited. To do this efficiently, we store visited nodes in a `Set`,
allowing for constant time containment checks and insertion. Finally, we
consider each connected component, merging all of its intervals by
constructing a new `Interval` with `start` equal to the minimum start among
them and `end` equal to the maximum end.

This algorithm is correct simply because it is basically the brute force
solution. We compare every interval to every other interval, so we know
exactly which intervals overlap. The reason for the connected component
search is that two intervals may not directly overlap, but might overlap
indirectly via a third interval. See the example below to see this more
clearly.

![Components Example](../Figures/56/component.png)
{:align="center"}

Although (1, 5) and (6, 10) do not directly overlap, either would overlap
with the other if first merged with (4, 7). There are two connected
components, so if we merge their nodes, we expect to get the following two
merged intervals:

(1, 10), (15, 20)


<iframe src="https://leetcode.com/playground/FdD8vWwU/shared" frameBorder="0" width="100%" height="500" name="FdD8vWwU"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$

    Building the graph costs $$O(V + E) = O(V) + O(E) = O(n) + O(n^2) = O(n^2)$$
    time, as in the worst case all intervals are mutually overlapping.
    Traversing the graph has the same cost (although it might appear higher
    at first) because our `visited` set guarantees that each node will be
    visited exactly once. Finally, because each node is part of exactly one
    component, the merge step costs $$O(V) = O(n)$$ time. This all adds up as
    follows:

    $$
        O(n^2) + O(n^2) + O(n) = O(n^2)
    $$

* Space complexity : $$O(n^2)$$

    As previously mentioned, in the worst case, all intervals are mutually
    overlapping, so there will be an edge for every pair of intervals.
    Therefore, the memory footprint is quadratic in the input size.

<br />

---

#### Approach 2: Sorting

**Intuition**

If we sort the intervals by their `start` value, then each set of intervals
that can be merged will appear as a contiguous "run" in the sorted list.

**Algorithm**

First, we sort the list as described. Then, we insert the first interval into
our `merged` list and continue considering each interval in turn as follows:
If the current interval begins *after* the previous interval ends, then they
do not overlap and we can append the current interval to `merged`. Otherwise,
they do overlap, and we merge them by updating the `end` of the previous
interval if it is less than the `end` of the current interval.

A simple proof by contradiction shows that this algorithm always produces the
correct answer. First, suppose that the algorithm at some point fails to
merge two intervals that should be merged. This would imply that there exists
some triple of indices $$i$$, $$j$$, and $$k$$ in a list of intervals
$$ints$$ such that $$i < j < k$$ and ($$ints[i]$$, $$ints[k]$$) can be
merged, but neither ($$ints[i]$$, $$ints[j]$$) nor ($$ints[j]$$, $$ints[k]$$)
can be merged. From this scenario follow several inequalities:

$$
\begin{aligned}
    ints[i].end < ints[j].start \\
    ints[j].end < ints[k].start \\
    ints[i].end \geq ints[k].start \\
\end{aligned}
$$

We can chain these inequalities (along with the following inequality, implied
by the well-formedness of the intervals: $$ints[j].start \leq ints[j].end$$) to
demonstrate a contradiction:

$$
\begin{aligned}
    ints[i].end < ints[j].start \leq ints[j].end < ints[k].start \\
    ints[i].end \geq ints[k].start
\end{aligned}
$$

Therefore, all mergeable intervals must occur in a contiguous run of the
sorted list.

![Sorting Example](../Figures/56/sort.png)
{:align="center"}


Consider the example above, where the intervals are sorted, and then all
mergeable intervals form contiguous blocks.

<iframe src="https://leetcode.com/playground/Zum7wj5V/shared" frameBorder="0" width="100%" height="500" name="Zum7wj5V"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n\log{}n)$$

    Other than the `sort` invocation, we do a simple linear scan of the list,
    so the runtime is dominated by the $$O(nlgn)$$ complexity of sorting.

* Space complexity : $$O(1)$$ (or $$O(n)$$)

    If we can sort `intervals` in place, we do not need more than constant
    additional space. Otherwise, we must allocate linear space to store a
    copy of `intervals` and sort that.
