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




## Thought:

We use backtraking strategy.

Consider this, we has a list which composes of strings that the input number '12' formed, as A = ['ab', 'cc', …].

Then, we iterate all the chars from the next number as '3' to map to the list A + a char, A + next char.