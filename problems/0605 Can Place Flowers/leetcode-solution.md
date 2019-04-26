# 0605 - Can Place Flowers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/can-place-flowers) | [solution](https://leetcode.com/problems/can-place-flowers/solution/)


-----------

<p>Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.</p>

<p>Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number <b>n</b>, return if <b>n</b> new flowers can be planted in it without violating the no-adjacent-flowers rule.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> flowerbed = [1,0,0,0,1], n = 1
<b>Output:</b> True
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> flowerbed = [1,0,0,0,1], n = 2
<b>Output:</b> False
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The input array won't violate no-adjacent-flowers rule.</li>
<li>The input array size is in the range of [1, 20000].</li>
<li><b>n</b> is a non-negative integer which won't exceed the input array size.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Teemo Attacking](teemo-attacking)

- [Medium] [Asteroid Collision](asteroid-collision)




## Solution:

[TOC]

## Solution

---
#### Approach #1 Single Scan [Accepted]

The solution is very simple. We can find out the extra maximum number of flowers, $$count$$, that can be planted for the given $$flowerbed$$ arrangement. To do so, we can traverse over all the elements of the $$flowerbed$$ and find out those elements which are 0(implying an empty position). For every such element, we check if its both adjacent positions are also empty. If so, we can plant a flower at the current position without violating the no-adjacent-flowers-rule. For the first and last elements, we need not check the previous and the next adjacent positions respectively.

If the $$count$$ obtained is greater than or equal to $$n$$, the required number of flowers to be planted, we can plant $$n$$ flowers in the empty spaces, otherwise not.

<iframe src="https://leetcode.com/playground/Dbm5A5CN/shared" frameBorder="0" name="Dbm5A5CN" width="100%" height="292"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. A single scan of the $$flowerbed$$ array of size $$n$$ is done.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
#### Approach #2 Optimized [Accepted]

**Algorithm**

Instead of finding the maximum value of $$count$$ that can be obtained, as done in the last approach, we can stop the process of checking the positions for planting the flowers as soon as $$count$$ becomes equal to $$n$$. Doing this leads to an optimization of the first approach. If $$count$$ never becomes equal to $$n$$, $$n$$ flowers can't be planted at the empty positions.

<iframe src="https://leetcode.com/playground/GtCBiouS/shared" frameBorder="0" name="GtCBiouS" width="100%" height="326"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. A single scan of the $$flowerbed$$ array of size $$n$$ is done.

* Space complexity : $$O(1)$$. Constant extra space is used.

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
