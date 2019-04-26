# 0729 - My Calendar I

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/my-calendar-i) | [solution](https://leetcode.com/problems/my-calendar-i/solution/)


-----------

<p>Implement a <code>MyCalendar</code> class to store your events. A new event can be added if adding the event will not cause a double booking.</p>

<p>Your class will have the method, <code>book(int start, int end)</code>. Formally, this represents a booking on the half open interval <code>[start, end)</code>, the range of real numbers <code>x</code> such that <code>start &lt;= x &lt; end</code>.</p>

<p>A <i>double booking</i> happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)</p>

<p>For each call to the method <code>MyCalendar.book</code>, return <code>true</code> if the event can be added to the calendar successfully without causing a double booking. Otherwise, return <code>false</code> and do not add the event to the calendar.</p>
Your class will be called like this: <code>MyCalendar cal = new MyCalendar();</code> <code>MyCalendar.book(start, end)</code>

<p><b>Example 1:</b></p>

<pre>
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
<b>Explanation:</b> 
The first event can be booked.  The second can&#39;t because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li>The number of calls to <code>MyCalendar.book</code> per test case will be at most <code>1000</code>.</li>
	<li>In calls to <code>MyCalendar.book(start, end)</code>, <code>start</code> and <code>end</code> are integers in the range <code>[0, 10^9]</code>.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [My Calendar II](my-calendar-ii)

- [Hard] [My Calendar III](my-calendar-iii)




## Solution:

[TOC]

#### Approach #1: Brute Force [Accepted]

**Intuition**

When booking a new event `[start, end)`, check if every current event conflicts with the new event.  If none of them do, we can book the event.

**Algorithm**

We will maintain a list of interval *events* (not necessarily sorted).  Evidently, two events `[s1, e1)` and `[s2, e2)` do *not* conflict if and only if one of them starts after the other one ends: either `e1 <= s2` OR `e2 <= s1`.  By De Morgan's laws, this means the events conflict when `s1 < e2` AND `s2 < e1`.

<iframe src="https://leetcode.com/playground/RbxQb2Zj/shared" frameBorder="0" width="100%" height="310" name="RbxQb2Zj"></iframe>


**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the number of events booked.  For each new event, we process every previous event to decide whether the new event can be booked.  This leads to $$\sum_k^N O(k) = O(N^2)$$ complexity.

* Space Complexity: $$O(N)$$, the size of the `calendar`.

---
#### Approach #2: Balanced Tree [Accepted]

**Intuition**

If we maintained our events in *sorted* order, we could check whether an event could be booked in $$O(\log N)$$ time (where $$N$$ is the number of events already booked) by binary searching for where the event should be placed.  We would also have to insert the event in our sorted structure.

**Algorithm**

We need a data structure that keeps elements sorted and supports fast insertion.  In Java, a `TreeMap` is the perfect candidate.  In Python, we can build our own binary tree structure.

For Java, we will have a `TreeMap` where the keys are the start of each interval, and the values are the ends of those intervals.  When inserting the interval `[start, end)`, we check if there is a conflict on each side with neighboring intervals: we would like `calendar.get(prev)) <= start <= end <= next` for the booking to be valid (or for `prev` or `next` to be null respectively.)

For Python, we will create a binary tree.  Each node represents some interval `[self.start, self.end)` while `self.left, self.right` represents nodes that are smaller or larger than the current node.

<iframe src="https://leetcode.com/playground/huRxLsMu/shared" frameBorder="0" width="100%" height="500" name="huRxLsMu"></iframe>

**Complexity Analysis**

* Time Complexity (Java): $$O(N \log N)$$, where $$N$$ is the number of events booked.  For each new event, we search that the event is legal in $$O(\log N)$$ time, then insert it in $$O(1)$$ time.

* Time Complexity (Python): $$O(N^2)$$ worst case, with $$O(N \log N)$$ on random data.  For each new event, we insert the event into our binary tree.  As this tree may not be balanced, it may take a linear number of steps to add each event.

* Space Complexity: $$O(N)$$, the size of the data structures used.

---

Analysis written by: [@awice](https://leetcode.com/awice).  Solutions in Approach #2 inspired by [@shawngao](https://discuss.leetcode.com/topic/111205/java-8-liner-treemap) and  [@persianPanda](https://discuss.leetcode.com/topic/111203/binary-search-tree-python).
