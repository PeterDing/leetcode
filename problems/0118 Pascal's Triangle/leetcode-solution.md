# 0118 - Pascal's Triangle

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/pascals-triangle) | [solution](https://leetcode.com/problems/pascals-triangle/solution/)


-----------

<p>Given a non-negative integer&nbsp;<em>numRows</em>, generate the first <em>numRows</em> of Pascal&#39;s triangle.</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" /><br />
<small>In Pascal&#39;s triangle, each number is the sum of the two numbers directly above it.</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 5
<strong>Output:</strong>
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
</pre>


-----------


## Similar Problems

- [Easy] [Pascal's Triangle II](pascals-triangle-ii)




## Solution:

[TOC]

#### Approach 1: Dynamic Programming

**Intuition**

If we have the a row of Pascal's triangle, we can easily compute the next
row by each pair of adjacent values.

**Algorithm**

Although the algorithm is very simple, the iterative approach to constructing
Pascal's triangle can be classified as dynamic programming because we
construct each row based on the previous row.

First, we generate the overall `triangle` list, which will store each row as
a sublist. Then, we check for the special case of $$0$$, as we would otherwise
return $$[1]$$. If $$numRows > 0$$, then we initialize `triangle` with $$[1]$$
as its first row, and proceed to fill the rows as follows:

!?!../Documents/118_Pascals_Triangle.json:1280,720!?!

<iframe src="https://leetcode.com/playground/idrxbCSN/shared" frameBorder="0" width="100%" height="500" name="idrxbCSN"></iframe>

**Complexity Analysis**

* Time complexity : $$O(numRows^2)$$

    Although updating each value of `triangle` happens in constant time, it
    is performed $$O(numRows^2)$$ times. To see why, consider how many
    overall loop iterations there are. The outer loop obviously runs
    $$numRows$$ times, but for each iteration of the outer loop, the inner
    loop runs $$rowNum$$ times. Therefore, the overall number of `triangle` updates
    that occur is $$1 + 2 + 3 + \ldots + numRows$$, which, according to Gauss' formula,
    is

    $$
    \begin{aligned}
        \frac{numRows(numRows+1)}{2} &= \frac{numRows^2 + numRows}{2} \\
        &= \frac{numRows^2}{2} + \frac{numRows}{2} \\
        &= O(numRows^2)
    \end{aligned}
    $$

* Space complexity : $$O(numRows^2)$$

    Because we need to store each number that we update in `triangle`, the
    space requirement is the same as the time complexity.
