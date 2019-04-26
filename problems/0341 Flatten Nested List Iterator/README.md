# 0341 - Flatten Nested List Iterator

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Stack, Design | [Leetcode](https://leetcode.com/problems/flatten-nested-list-iterator) | [solution](https://leetcode.com/problems/flatten-nested-list-iterator/solution/)


-----------

<p>Given a nested list of integers, implement an iterator to flatten it.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,1],2,[1,1]]</span>
<strong>Output: </strong><span id="example-output-1">[1,1,2,1,1]
</span><strong>Explanation: </strong>By calling <i>next</i> repeatedly until <i>hasNext</i> returns false, 
&nbsp;            the order of elements returned by <i>next</i> should be: <code>[1,1,2,1,1]</code>.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,[4,[6]]]</span>
<strong>Output: </strong><span id="example-output-2">[1,4,6]
</span><strong>Explanation: </strong>By calling <i>next</i> repeatedly until <i>hasNext</i> returns false, 
&nbsp;            the order of elements returned by <i>next</i> should be: <code>[1,4,6]</code>.
</pre>
</div>
</div>


-----------


## Similar Problems

- [Medium] [Flatten 2D Vector](flatten-2d-vector)

- [Medium] [Zigzag Iterator](zigzag-iterator)

- [Medium] [Mini Parser](mini-parser)

- [Medium] [Array Nesting](array-nesting)




## Thought:
