# 0327 - Count of Range Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Binary Search, Divide and Conquer, Sort, Binary Indexed Tree, Segment Tree | [Leetcode](https://leetcode.com/problems/count-of-range-sum) | [solution](https://leetcode.com/problems/count-of-range-sum/solution/)


-----------

<p>Given an integer array <code>nums</code>, return the number of range sums that lie in <code>[lower, upper]</code> inclusive.<br />
Range sum <code>S(i, j)</code> is defined as the sum of the elements in <code>nums</code> between indices <code>i</code> and <code>j</code> (<code>i</code> &le; <code>j</code>), inclusive.</p>

<p><b>Note:</b><br />
A naive algorithm of <i>O</i>(<i>n</i><sup>2</sup>) is trivial. You MUST do better than that.</p>

<p><b>Example:</b></p>

<pre>
<strong>Input: </strong><i>nums</i> = <code>[-2,5,-1]</code>, <i>lower</i> = <code>-2</code>, <i>upper</i> = <code>2</code>,
<strong>Output: </strong>3 
<strong>Explanation: </strong>The three ranges are : <code>[0,0]</code>, <code>[2,2]</code>, <code>[0,2]</code> and their respective sums are: <code>-2, -1, 2</code>.
</pre>

-----------


## Similar Problems

- [Hard] [Count of Smaller Numbers After Self](count-of-smaller-numbers-after-self)

- [Hard] [Reverse Pairs](reverse-pairs)




## Thought:
