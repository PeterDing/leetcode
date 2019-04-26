# 0678 - Valid Parenthesis String

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String | [Leetcode](https://leetcode.com/problems/valid-parenthesis-string) | [solution](https://leetcode.com/problems/valid-parenthesis-string/solution/)


-----------

<p>
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
<ol>
<li>Any left parenthesis <code>'('</code> must have a corresponding right parenthesis <code>')'</code>.</li>
<li>Any right parenthesis <code>')'</code> must have a corresponding left parenthesis <code>'('</code>.</li>
<li>Left parenthesis <code>'('</code> must go before the corresponding right parenthesis <code>')'</code>.</li>
<li><code>'*'</code> could be treated as a single right parenthesis <code>')'</code> or a single left parenthesis <code>'('</code> or an empty string.</li>
<li>An empty string is also valid.</li>
</ol>
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "()"
<b>Output:</b> True
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "(*)"
<b>Output:</b> True
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> "(*))"
<b>Output:</b> True
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The string size will be in the range [1, 100].</li>
</ol>
</p>

-----------


## Similar Problems

- [Hard] [Special Binary String](special-binary-string)




## Solution:

[TOC]

#### Approach #1: Brute Force [Time Limit Exceeded]

**Intuition and Algorithm**

For each asterisk, let's try both possibilities.

<iframe src="https://leetcode.com/playground/HHVFGh2C/shared" frameBorder="0" name="HHVFGh2C" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N * 3^{N})$$, where $$N$$ is the length of the string.  For each asterisk we try 3 different values.  Thus, we could be checking the validity of up to $$3^N$$ strings.  Then, each check of validity is $$O(N)$$.

* Space Complexity:  $$O(N)$$, the space used by our character array.

---
#### Approach #2: Dynamic Programming [Accepted]

**Intuition and Algorithm**

Let `dp[i][j]` be `true` if and only if the interval `s[i], s[i+1], ..., s[j]` can be made valid.  Then `dp[i][j]` is true only if:

* `s[i]` is `'*'`, and the interval `s[i+1], s[i+2], ..., s[j]` can be made valid;

* or, `s[i]` can be made to be `'('`, and there is some `k` in `[i+1, j]` such that `s[k]` can be made to be `')'`, plus the two intervals cut by `s[k]` (`s[i+1: k]` and `s[k+1: j+1]`) can be made valid;

<iframe src="https://leetcode.com/playground/c2qhBzko/shared" frameBorder="0" name="c2qhBzko" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^3)$$, where $$N$$ is the length of the string.  There are $$O(N^2)$$ states corresponding to entries of `dp`, and we do an average of $$O(N)$$ work on each state.

* Space Complexity:  $$O(N^2)$$, the space used to store intermediate results in `dp`.

---
#### Approach #3: Greedy [Accepted]

**Intuition**

When checking whether the string is valid, we only cared about the "`balance`": the number of extra, open left brackets as we parsed through the string.  For example, when checking whether '(()())' is valid, we had a balance of `1, 2, 1, 2, 1, 0` as we parse through the string: `'('` has 1 left bracket, `'(('` has 2, `'(()'` has 1, and so on.  This means that after parsing the first `i` symbols, (which may include asterisks,) we only need to keep track of what the `balance` could be.

For example, if we have string `'(***)'`, then as we parse each symbol, the set of possible values for the `balance` is `[1]` for `'('`; `[0, 1, 2]` for `'(*'`; `[0, 1, 2, 3]` for `'(**'`; `[0, 1, 2, 3, 4]` for `'(***'`, and `[0, 1, 2, 3]` for `'(***)'`.

Furthermore, we can prove these states always form a contiguous interval.  Thus, we only need to know the left and right bounds of this interval.  That is, we would keep those intermediate states described above as `[lo, hi] = [1, 1], [0, 2], [0, 3], [0, 4], [0, 3]`.

**Algorithm**

Let `lo, hi` respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.

If we encounter a left bracket (`c == '('`), then `lo++`, otherwise we could write a right bracket, so `lo--`.  If we encounter what can be a left bracket (`c != ')'`), then `hi++`, otherwise we must write a right bracket, so `hi--`.  If `hi < 0`, then the current prefix can't be made valid no matter what our choices are.  Also, we can never have less than `0` open left brackets.  At the end, we should check that we can have exactly 0 open left brackets.



<iframe src="https://leetcode.com/playground/AP7MmhXJ/shared" frameBorder="0" name="AP7MmhXJ" width="100%" height="258"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of the string.  We iterate through the string once.

* Space Complexity:  $$O(1)$$, the space used by our `lo` and `hi` pointers.  However, creating a new character array will take $$O(N)$$ space.

---

Analysis written by: [@awice](https://leetcode.com/awice)
