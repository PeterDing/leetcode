# 0731 - My Calendar II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Ordered Map | [Leetcode](https://leetcode.com/problems/my-calendar-ii) | [solution](https://leetcode.com/problems/my-calendar-ii/solution/)


-----------

<p>Implement a <code>MyCalendarTwo</code> class to store your events. A new event can be added if adding the event will not cause a <b>triple</b> booking.</p>

<p>Your class will have one method, <code>book(int start, int end)</code>. Formally, this represents a booking on the half open interval <code>[start, end)</code>, the range of real numbers <code>x</code> such that <code>start &lt;= x &lt; end</code>.</p>

<p>A <i>triple booking</i> happens when <b>three</b> events have some non-empty intersection (ie., there is some time that is common to all 3 events.)</p>

<p>For each call to the method <code>MyCalendar.book</code>, return <code>true</code> if the event can be added to the calendar successfully without causing a <b>triple</b> booking. Otherwise, return <code>false</code> and do not add the event to the calendar.</p>
Your class will be called like this: <code>MyCalendar cal = new MyCalendar();</code> <code>MyCalendar.book(start, end)</code>

<p><b>Example 1:</b></p>

<pre>
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
<b>Explanation:</b> 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can&#39;t be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
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

- [Medium] [My Calendar I](my-calendar-i)

- [Hard] [My Calendar III](my-calendar-iii)




## Solution:

[TOC]

#### Approach #1: Brute Force [Accepted]

**Intuition**

Maintain a list of bookings and a list of double bookings.  When booking a new event `[start, end)`, if it conflicts with a double booking, it will have a triple booking and be invalid.  Otherwise, parts that overlap the calendar will be a double booking.

**Algorithm**

Evidently, two events `[s1, e1)` and `[s2, e2)` do *not* conflict if and only if one of them starts after the other one ends: either `e1 <= s2` OR `e2 <= s1`.  By De Morgan's laws, this means the events conflict when `s1 < e2` AND `s2 < e1`.

If our event conflicts with a double booking, it's invalid.  Otherwise, we add conflicts with the calendar to our double bookings, and add the event to our calendar.

<iframe src="https://leetcode.com/playground/joRUVwzm/shared" frameBorder="0" width="100%" height="395" name="joRUVwzm"></iframe>


**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the number of events booked.  For each new event, we process every previous event to decide whether the new event can be booked.  This leads to $$\sum_k^N O(k) = O(N^2)$$ complexity.

* Space Complexity: $$O(N)$$, the size of the `calendar`.

---
#### Approach #2: Boundary Count [Accepted]

**Intuition and Algorithm**

When booking a new event `[start, end)`, count `delta[start]++` and `delta[end]--`.  When processing the values of `delta` in sorted order of their keys, the running sum `active` is the number of events open at that time.  If the sum is 3 or more, that time is (at least) triple booked.

A Python implementation was not included for this approach because there is no analog to *TreeMap* available.

```java
class MyCalendarTwo {
    TreeMap<Integer, Integer> delta;

    public MyCalendarTwo() {
        delta = new TreeMap();
    }

    public boolean book(int start, int end) {
        delta.put(start, delta.getOrDefault(start, 0) + 1);
        delta.put(end, delta.getOrDefault(end, 0) - 1);

        int active = 0;
        for (int d: delta.values()) {
            active += d;
            if (active >= 3) {
                delta.put(start, delta.get(start) - 1);
                delta.put(end, delta.get(end) + 1);
                if (delta.get(start) == 0)
                    delta.remove(start);
                return false;
            }
        }
        return true;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the number of events booked.  For each new event, we traverse `delta` in $$O(N)$$ time.

* Space Complexity: $$O(N)$$, the size of `delta`.

---

Analysis written by: [@awice](https://leetcode.com/awice).  Solution in Approach #2 inspired by [@cchao](https://discuss.leetcode.com/topic/111276/simplified-winner-s-solution).
