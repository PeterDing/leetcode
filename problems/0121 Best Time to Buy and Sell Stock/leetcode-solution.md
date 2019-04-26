# 0121 - Best Time to Buy and Sell Stock

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Dynamic Programming | [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | [solution](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/)


-----------

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.</p>

<p>Note that you cannot sell a stock before you buy one.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
&nbsp;            Not 7-1 = 6, as selling price needs to be larger than buying price.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>


-----------


## Similar Problems

- [Easy] [Maximum Subarray](maximum-subarray)

- [Easy] [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii)

- [Hard] [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii)

- [Hard] [Best Time to Buy and Sell Stock IV](best-time-to-buy-and-sell-stock-iv)

- [Medium] [Best Time to Buy and Sell Stock with Cooldown](best-time-to-buy-and-sell-stock-with-cooldown)




## Solution:

[TOC]

## Solution

We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).

In formal terms, we need to find $$\max(prices[j] - prices[i])$$, for every $$i$$ and $$j$$ such that $$j > i$$.

---
#### Approach 1: Brute Force

<iframe src="https://leetcode.com/playground/enjmphvG/shared" frameBorder="0" width="100%" height="276" name="enjmphvG"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n^2)$$. Loop runs $$\dfrac{n (n-1)}{2}$$ times.

* Space complexity : $$O(1)$$. Only two variables - $$\text{maxprofit}$$ and $$\text{profit}$$ are used.
<br />
<br />
---
#### Approach 2: One Pass

**Algorithm**

Say the given array is:

[7, 1, 5, 3, 6, 4]

If we plot the numbers of the given array on a graph, we get:

![Profit Graph](https://leetcode.com/media/original_images/121_profit_graph.png)

The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley.
We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.

<iframe src="https://leetcode.com/playground/G8wkXsyB/shared" frameBorder="0" width="100%" height="276" name="G8wkXsyB"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. Only a single pass is needed.

* Space complexity : $$O(1)$$. Only two variables are used.
