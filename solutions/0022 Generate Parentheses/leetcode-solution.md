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




## Solution:

[TOC]

#### Approach 1: Brute Force

**Intuition**

We can generate all $$2^{2n}$$ sequences of `'('` and `')'` characters.  Then, we will check if each one is valid.

**Algorithm**

To generate all sequences, we use a recursion.  All sequences of length `n` is just `'('` plus all sequences of length `n-1`, and then `')'` plus all sequences of length `n-1`.

To check whether a sequence is valid, we keep track of `balance`, the net number of opening brackets minus closing brackets.  If it falls below zero at any time, or doesn't end in zero, the sequence is invalid - otherwise it is valid.

<iframe src="https://leetcode.com/playground/eDRvbWjL/shared" frameBorder="0" width="100%" height="500" name="eDRvbWjL"></iframe>

**Complexity Analysis**

* Time Complexity : $$O(2^{2n}n)$$.  For each of $$2^{2n}$$ sequences, we need to create and validate the sequence, which takes $$O(n)$$ work.

* Space Complexity : $$O(2^{2n}n)$$.  Naively, every sequence could be valid.  See [Approach 3](#approach-3-closure-number) for development of a tighter asymptotic bound.
<br />
<br />
---
#### Approach 2: Backtracking

**Intuition and Algorithm**

Instead of adding `'('` or `')'` every time as in [Approach 1](#approach-1-brute-force), let's only add them when we know it will remain a valid sequence.  We can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of `n`) left to place.  And we can start a closing bracket if it would not exceed the number of opening brackets.

<iframe src="https://leetcode.com/playground/npPa38Mh/shared" frameBorder="0" width="100%" height="378" name="npPa38Mh"></iframe>

**Complexity Analysis**

Our complexity analysis rests on understanding how many elements there are in `generateParenthesis(n)`.  This analysis is outside the scope of this article, but it turns out this is the `n`-th Catalan number $$\dfrac{1}{n+1}\binom{2n}{n}$$, which is bounded asymptotically by $$\dfrac{4^n}{n\sqrt{n}}$$.

* Time Complexity : $$O(\dfrac{4^n}{\sqrt{n}})$$.  Each valid sequence has at most `n` steps during the backtracking procedure.

* Space Complexity : $$O(\dfrac{4^n}{\sqrt{n}})$$, as described above, and using $$O(n)$$ space to store the sequence.
<br />
<br />
---

#### Approach 3: Closure Number

**Intuition**

To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count.

Consider the *closure number* of a valid parentheses sequence `S`: the least `index >= 0` so that `S[0], S[1], ..., S[2*index+1]` is valid.  Clearly, every parentheses sequence has a unique *closure number*.  We can try to enumerate them individually.

**Algorithm**

For each closure number `c`, we know the starting and ending brackets must be at index `0` and `2*c + 1`. Then, the `2*c` elements between must be a valid sequence, plus the rest of the elements must be a valid sequence.

<iframe src="https://leetcode.com/playground/Z3ZYfRAo/shared" frameBorder="0" width="100%" height="293" name="Z3ZYfRAo"></iframe>

**Complexity Analysis**

* Time and Space Complexity : $$O(\dfrac{4^n}{\sqrt{n}})$$.  The analysis is similar to [Approach 2](#approach-2-backtracking).
