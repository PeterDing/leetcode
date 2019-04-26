# 0690 - Employee Importance

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table, Depth-first Search, Breadth-first Search | [Leetcode](https://leetcode.com/problems/employee-importance) | [solution](https://leetcode.com/problems/employee-importance/solution/)


-----------

<p>You are given a data structure of employee information, which includes the employee&#39;s <b>unique id</b>, his <b>importance value</b> and his <b>direct</b> subordinates&#39; id.</p>

<p>For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is <b>not direct</b>.</p>

<p>Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
<b>Output:</b> 11
<b>Explanation:</b>
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>One employee has at most one <b>direct</b> leader and may have several subordinates.</li>
	<li>The maximum number of employees won&#39;t exceed 2000.</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Easy] [Nested List Weight Sum](nested-list-weight-sum)




## Solution:

[TOC]

#### Approach #1: Depth-First Search [Accepted]

**Intuition and Algorithm**

Let's use a hashmap `emap = {employee.id -> employee}` to query employees quickly.

Now to find the total importance of an employee, it will be the importance of that employee, plus the total importance of each of that employee's subordinates.  This is a straightforward depth-first search.

<iframe src="https://leetcode.com/playground/NX7sm9qW/shared" frameBorder="0" width="100%" height="310" name="NX7sm9qW"></iframe>


**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of employees.  We might query each employee in `dfs`.

* Space Complexity: $$O(N)$$, the size of the implicit call stack when evaluating `dfs`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
