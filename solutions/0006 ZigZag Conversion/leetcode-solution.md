# 0006 - ZigZag Conversion

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String | [Leetcode](https://leetcode.com/problems/zigzag-conversion) | [solution](https://leetcode.com/problems/zigzag-conversion/solution/)


-----------

<p>The string <code>&quot;PAYPALISHIRING&quot;</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>&quot;PAHNAPLSIIGYIR&quot;</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>
string convert(string s, int numRows);</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 3
<strong>Output:</strong> &quot;PAHNAPLSIIGYIR&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows =&nbsp;4
<strong>Output:</strong>&nbsp;&quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>

P     I    N
A   L S  I G
Y A   H R
P     I</pre>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---

#### Approach 1: Sort by Row

**Intuition**

By iterating through the string from left to right, we can easily determine which row in the Zig-Zag pattern that a character belongs to.

**Algorithm**

We can use $$\text{min}( \text{numRows}, \text{len}(s))$$ lists to represent the non-empty rows of the Zig-Zag Pattern.

Iterate through $$s$$ from left to right, appending each character to the appropriate row. The appropriate row can be tracked using two variables: the current row and the current direction.

The current direction changes only when we moved up to the topmost row or moved down to the bottommost row.

<iframe src="https://leetcode.com/playground/F7ATKV4h/shared" frameBorder="0" width="100%" height="446" name="F7ATKV4h"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(n)$$, where $$n == \text{len}(s)$$
* Space Complexity: $$O(n)$$

<br/>

---

#### Approach 2: Visit by Row

**Intuition**

Visit the characters in the same order as reading the Zig-Zag pattern line by line.

**Algorithm**

Visit all characters in row 0 first, then row 1, then row 2, and so on...

For all whole numbers $$k$$,

- Characters in row $$0$$ are located at indexes $$k \; (2 \cdot \text{numRows} - 2)$$
- Characters in row $$\text{numRows}-1$$ are located at indexes $$k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1$$
- Characters in inner row $$i$$ are located at indexes $$k \; (2 \cdot \text{numRows}-2)+i$$ and $$(k+1)(2 \cdot \text{numRows}-2)- i$$.

<iframe src="https://leetcode.com/playground/Deg3hGi4/shared" frameBorder="0" width="100%" height="395" name="Deg3hGi4"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(n)$$, where $$n == \text{len}(s)$$. Each index is visited once.
* Space Complexity: $$O(n)$$. For the cpp implementation, $$O(1)$$ if return string is not considered extra space.
