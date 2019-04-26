# 0714 - Best Time to Buy and Sell Stock with Transaction Fee

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Dynamic Programming, Greedy | [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) | [solution](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/)


-----------

<p>Your are given an array of integers <code>prices</code>, for which the <code>i</code>-th element is the price of a given stock on day <code>i</code>; and a non-negative integer <code>fee</code> representing a transaction fee.</p>
<p>You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)</p>
<p>Return the maximum profit you can make.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> prices = [1, 3, 2, 8, 4, 9], fee = 2
<b>Output:</b> 8
<b>Explanation:</b> The maximum profit can be achieved by:
<li>Buying at prices[0] = 1</li><li>Selling at prices[3] = 8</li><li>Buying at prices[4] = 4</li><li>Selling at prices[5] = 9</li>The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
</pre>
</p>

<p><b>Note:</b>
<li><code>0 < prices.length <= 50000</code>.</li>
<li><code>0 < prices[i] < 50000</code>.</li>
<li><code>0 <= fee < 50000</code>.</li>
</p>

-----------


## Similar Problems

- [Easy] [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii)




## Solution:

[TOC]


#### Approach #1: Dynamic Programming [Accepted]

**Intuition and Algorithm**

At the end of the `i`-th day, we maintain `cash`, the maximum profit we could have if we did not have a share of stock, and `hold`, the maximum profit we could have if we owned a share of stock.

To transition from the `i`-th day to the `i+1`-th day, we either sell our stock `cash = max(cash, hold + prices[i] - fee)` or buy a stock `hold = max(hold, cash - prices[i])`.  At the end, we want to return `cash`.  We can transform `cash` first without using temporary variables because selling and buying on the same day can't be better than just continuing to hold the stock.

**Python**
```python
class Solution(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
```

**Java**
```java
class Solution {
    public int maxProfit(int[] prices, int fee) {
        int cash = 0, hold = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            cash = Math.max(cash, hold + prices[i] - fee);
            hold = Math.max(hold, cash - prices[i]);
        }
        return cash;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of prices.

* Space Complexity: $$O(1)$$, the space used by `cash` and `hold`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
