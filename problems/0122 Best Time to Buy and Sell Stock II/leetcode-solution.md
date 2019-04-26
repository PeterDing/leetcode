# 0122 - Best Time to Buy and Sell Stock II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Greedy | [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii) | [solution](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/)


-----------

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).</p>

<p><strong>Note:</strong> You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
&nbsp;            Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
&nbsp;            Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
&nbsp;            engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.</pre>


-----------


## Similar Problems

- [Easy] [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock)

- [Hard] [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii)

- [Hard] [Best Time to Buy and Sell Stock IV](best-time-to-buy-and-sell-stock-iv)

- [Medium] [Best Time to Buy and Sell Stock with Cooldown](best-time-to-buy-and-sell-stock-with-cooldown)

- [Medium] [Best Time to Buy and Sell Stock with Transaction Fee](best-time-to-buy-and-sell-stock-with-transaction-fee)




## Solution:

[TOC]

## Summary

We have to determine the maximum profit that can be obtained by making the transactions (no limit on the number of transactions done). For this we need to find out those sets of buying and selling prices which together lead to the maximization of profit.

## Solution
---

#### Approach 1: Brute Force

In this case, we simply calculate the profit corresponding to all the possible sets of transactions and find out the maximum profit out of them.

<iframe src="https://leetcode.com/playground/DQfAGPiL/shared" frameBorder="0" width="100%" height="463" name="DQfAGPiL"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^n)$$. Recursive function is called $$n^n$$ times.

* Space complexity : $$O(n)$$. Depth of recursion is $$n$$.
<br />
<br />
---
#### Approach 2: Peak Valley Approach

**Algorithm**

Say the given array is:

[7, 1, 5, 3, 6, 4].

If we plot the numbers of the given array on a graph, we get:

![Profit Graph](https://leetcode.com/media/original_images/122_maxprofit_1.PNG){:width="539px"}
{:align="center"}


If we analyze the graph, we notice that the points of interest are the consecutive valleys and peaks.

Mathematically speaking:
$$
Total Profit= \sum_{i}(height(peak_i)-height(valley_i))
$$

The key point is we need to consider every peak immediately following a valley to maximize the profit. In case we skip one of the peaks (trying to obtain more profit), we will end up losing the profit over one of the transactions leading to an overall lesser profit.

For example, in the above case, if we skip $$peak_i$$ and $$valley_j$$ trying to obtain more profit by considering points with more difference in heights, the net profit obtained will always be lesser than the one obtained by including them, since $$C$$ will always be lesser than $$A+B$$.


<iframe src="https://leetcode.com/playground/Yrs8F9na/shared" frameBorder="0" width="100%" height="361" name="Yrs8F9na"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Single pass.

* Space complexity : $$O(1)$$. Constant space required.
<br />
<br />
---
#### Approach 3: Simple One Pass

**Algorithm**

This solution follows the logic used in [Approach 2](#approach-2-peak-valley-approach) itself, but with only a slight variation. In this case, instead of looking for every peak following a valley, we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction. In the end,we will be using the peaks and valleys effectively, but we need not track the costs corresponding to the peaks and valleys along with the maximum profit, but we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one, and at the total sum we obtain will be the maximum profit. This approach will simplify the solution.
This can be made clearer by taking this example:

[1, 7, 2, 3, 6, 7, 6, 7]


The graph corresponding to this array is:

![Profit Graph](https://leetcode.com/media/original_images/122_maxprofit_2.PNG){:width="539px"}
{:align="center"}


From the above graph, we can observe that the sum $$A+B+C$$ is equal to the difference $$D$$ corresponding to the difference between the heights of the consecutive peak and valley.

<iframe src="https://leetcode.com/playground/ppWUGTaj/shared" frameBorder="0" width="100%" height="225" name="ppWUGTaj"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Single pass.

* Space complexity: $$O(1)$$. Constant space needed.
