# 0002 - Add Two Numbers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Linked List, Math | [Leetcode](https://leetcode.com/problems/add-two-numbers) | [solution](https://leetcode.com/problems/add-two-numbers/solution/)

-----------

<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The digits are stored in <b>reverse order</b> and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> (2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)
<b>Output:</b> 7 -&gt; 0 -&gt; 8
<b>Explanation:</b> 342 + 465 = 807.
</pre>


-----------


## Similar Problems

- [Medium] [Multiply Strings](multiply-strings)

- [Easy] [Add Binary](add-binary)

- [Easy] [Sum of Two Integers](sum-of-two-integers)

- [Easy] [Add Strings](add-strings)

- [Medium] [Add Two Numbers II](add-two-numbers-ii)

- [Easy] [Add to Array-Form of Integer](add-to-array-form-of-integer)




## Thought:

```python
r = 0

for ls, index in enumerate(lists):
    while ls.next:
    	r += ls.val * (index ** 10)
        ls = ls.next
return r
```

Done.