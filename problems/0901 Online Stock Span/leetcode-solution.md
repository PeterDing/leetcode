# 0901 - Online Stock Span

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Stack | [Leetcode](https://leetcode.com/problems/online-stock-span) | [solution](https://leetcode.com/problems/online-stock-span/solution/)


-----------

<p>Write a class <code>StockSpanner</code> which collects daily price quotes for some stock, and returns the <em>span</em>&nbsp;of that stock&#39;s price for the current day.</p>

<p>The span of the stock&#39;s price today&nbsp;is defined as the maximum number of consecutive days (starting from today and going backwards)&nbsp;for which the price of the stock was less than or equal to today&#39;s price.</p>

<p>For example, if the price of a stock over the next 7 days were <code>[100, 80, 60, 70, 60, 75, 85]</code>, then the stock spans would be <code>[1, 1, 1, 2, 1, 4, 6]</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;StockSpanner&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;]</span>, <span id="example-input-1-2">[[],[100],[80],[60],[70],[60],[75],[85]]</span>
<strong>Output: </strong><span id="example-output-1">[null,1,1,1,2,1,4,6]</span>
<strong>Explanation: </strong>
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today&#39;s price of 75) were less than or equal to today&#39;s price.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>Calls to <code>StockSpanner.next(int price)</code> will have <code>1 &lt;= price &lt;= 10^5</code>.</li>
	<li>There will be at most <code>10000</code> calls to <code>StockSpanner.next</code>&nbsp;per test case.</li>
	<li>There will be at most <code>150000</code> calls to <code>StockSpanner.next</code> across all test cases.</li>
	<li>The total&nbsp;time limit for this problem has been reduced by 75% for&nbsp;C++, and 50% for all other languages.</li>
</ol>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Stack

**Intuition**

Clearly, we need to focus on how to make each query faster than a linear scan.  In a typical case, we get a new element like `7`, and there are some previous elements like `11, 3, 9, 5, 6, 4`.  Let's try to create some relationship between this query and the next query.

If (after getting `7`) we get an element like `2`, then the answer is `1`.  So in general, whenever we get a smaller element, the answer is 1.

If we get an element like `8`, the answer is 1 plus the previous answer (for `7`), as the `8` "stops" on the same value that `7` does (namely, `9`).

If we get an element like `10`, the answer is 1 plus the previous answer, plus the answer for `9`.

Notice throughout this evaluation, we only care about elements that occur in increasing order - we "shortcut" to them.  That is, from adding an element like `10`, we cut to `7` [with "weight" 4], then to `9` [with weight 2], then cut to `11` [with weight 1].

A stack is the ideal data structure to maintain what we care about efficiently.

**Algorithm**

Let's maintain a weighted stack of decreasing elements.  The size of the weight will be the total number of elements skipped.  For example, `11, 3, 9, 5, 6, 4, 7` will be `(11, weight=1), (9, weight=2), (7, weight=4)`.

When we get a new element like `10`, this helps us count the previous values faster by popping weighted elements off the stack.  The new stack at the end will look like `(11, weight=1), (10, weight=7)`.

<iframe src="https://leetcode.com/playground/5aJytT6D/shared" frameBorder="0" width="100%" height="395" name="5aJytT6D"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(Q)$$, where $$Q$$ is the number of calls to `StockSpanner.next`.  In total, there are $$Q$$ pushes to the stack, and at most $$Q$$ pops.

* Space Complexity:  $$O(Q)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
