# 0022 - Generate Parentheses

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String, Backtracking | [Leetcode](https://leetcode.com/problems/generate-parentheses) | [solution](https://leetcode.com/problems/generate-parentheses/solution/)

-----------

<p>
Given <i>n</i> pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
</p>

<p>
For example, given <i>n</i> = 3, a solution set is:
</p>
<pre>
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
</pre>
-----------


## Similar Problems

- [Medium] [Letter Combinations of a Phone Number](letter-combinations-of-a-phone-number)

- [Easy] [Valid Parentheses](valid-parentheses)



## Thought:

We notice that the number of `(` is always large equal to the number of `)` at whatever pointer of a parenthese.

```python
START = '('
END = ')'


def rec(rs, N, starts=0, ends=0, s=''):
    if len(s) == N * 2:
        rs.append(s)
        return

    if starts < N:
        rec(rs, N, starts + 1, ends, s + START)

    if ends < starts:
        rec(rs, N, starts, ends + 1, s + END)


rs = []
rec(rs, 4)

for i in sorted(rs):
    print(i)
```

