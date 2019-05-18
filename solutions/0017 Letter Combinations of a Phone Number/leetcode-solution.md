# 0017 - Letter Combinations of a Phone Number

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String, Backtracking | [Leetcode](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | [solution](https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/)


-----------

<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent.</p>

<p>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>

<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png" /></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: </strong>&quot;23&quot;
<strong>Output:</strong> [&quot;ad&quot;, &quot;ae&quot;, &quot;af&quot;, &quot;bd&quot;, &quot;be&quot;, &quot;bf&quot;, &quot;cd&quot;, &quot;ce&quot;, &quot;cf&quot;].
</pre>

<p><strong>Note:</strong></p>

<p>Although the above answer is in lexicographical order, your answer could be in any order you want.</p>


-----------


## Similar Problems

- [Medium] [Generate Parentheses](generate-parentheses)

- [Medium] [Combination Sum](combination-sum)

- [Easy] [Binary Watch](binary-watch)




## Solution:

[TOC]

## Solution

---

#### Approach 1: Backtracking

[Backtracking](https://en.wikipedia.org/wiki/Backtracking) 
is an algorithm for finding all
solutions by exploring all potential candidates.
If the solution candidate turns to be _not_ a solution 
(or at least not the _last_ one), 
backtracking algorithm discards it by making some changes 
on the previous step, *i.e.* _backtracks_ and then try again.

Here is a backtrack function `backtrack(combination, next_digits)`
which takes as arguments an ongoing letter combination 
and the next digits to check.

* If there is no more digits to check
that means that the current combination is done.
* If there are still digits to check :
    * Iterate over the letters mapping the next available digit.
        * Append the current letter to the current combination 
        `combination = combination + letter`.
        * Proceed to check next digits : 
        `backtrack(combination + letter, next_digits[1:])`.
        
!?!../Documents/17_LIS.json:1000,592!?!

<iframe src="https://leetcode.com/playground/26oBRSTE/shared" frameBorder="0" width="100%" height="500" name="26oBRSTE"></iframe>

**Complexity Analysis**

* Time complexity : $$\mathcal{O}(3^N \times 4^M)$$
where `N` is the number of digits in the input that maps to  3 letters 
(*e.g.* `2, 3, 4, 5, 6, 8`) and `M` is the number of digits in the input
that maps to 4 letters (*e.g.* `7, 9`),
and `N+M` is the total number digits in the input.
 
* Space complexity : $$\mathcal{O}(3^N \times 4^M)$$ since one has to keep
$$3^N \times 4^M$$ solutions.

Analysis written by @[liaison](https://leetcode.com/liaison/)
and @[andvary](https://leetcode.com/andvary/)
