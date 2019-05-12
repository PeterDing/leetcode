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

<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows =&nbsp;4
<strong>Output:</strong>&nbsp;&quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>

<pre>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>
-----------


## Similar Problems




## Thought:

We can find the first row index of each element ei for giving n row.

e0

e1 = e0 + (n-1)*2

ei = e(i-1) +  (n-1)*2

The index of second row elements are:

(e0 + 1, e1 - 1) | (e1 + 1, e2 - 1) | ….

The index of j row elements are:

( e0 + (j - 1), e1 - (j - 1) ) | (e1 + (j - 1), e2 - (j - 1) ) | ….