# 0738 - Monotone Increasing Digits

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Greedy | [Leetcode](https://leetcode.com/problems/monotone-increasing-digits) | [solution](https://leetcode.com/problems/monotone-increasing-digits/solution/)


-----------

<p>
Given a non-negative integer <code>N</code>, find the largest number that is less than or equal to <code>N</code> with monotone increasing digits.
</p><p>
(Recall that an integer has <i>monotone increasing digits</i> if and only if each pair of adjacent digits <code>x</code> and <code>y</code> satisfy <code>x <= y</code>.)
</p><p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> N = 10
<b>Output:</b> 9
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> N = 1234
<b>Output:</b> 1234
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> N = 332
<b>Output:</b> 299
</pre>
</p>

<p><b>Note:</b>
<code>N</code> is an integer in the range <code>[0, 10^9]</code>.
</p>

-----------


## Similar Problems

- [Medium] [Remove K Digits](remove-k-digits)




## Solution:

[TOC]

#### Approach #1: Greedy [Accepted]

**Intuition**

Let's construct the answer digit by digit.

If the current answer is say, `123`, and the next digit is `5`, then the answer must be at least `123555...5`, since the digits in the answer must be monotonically increasing.  If this is larger than `N`, then it's impossible.

**Algorithm**

For each digit of `N`, let's build the next digit of our answer `ans`.  We'll find the smallest possible digit `d` such that `ans + (d repeating) > N` when comparing by string; that means `d-1` must have satisfied `ans + (d-1 repeating) <= N`, and so we'll add `d-1` to our answer.  If we don't find such a digit, we can add a `9` instead.

<iframe src="https://leetcode.com/playground/FBLCwPuk/shared" frameBorder="0" width="100%" height="429" name="FBLCwPuk"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(D^2)$$, where $$D \approx \log N$$ is the number of digits in $$N$$.  We do $$O(D)$$ work building and comparing each candidate, and we do this $$O(D)$$ times.

* Space Complexity: $$O(D)$$, the size of the answer and the temporary string we are comparing.

---
#### Approach #2: Truncate After Cliff [Accepted]

**Intuition**

One initial thought that comes to mind is we can always have a candidate answer of `d999...9` (a digit `0 <= d <= 9` followed by some number of nines.)  For example if `N = 432543654`, we could always have an answer of at least `399999999`.

We can do better.  For example, when the number is `123454321`, we could have a candidate of `123449999`.  It seems like a decent strategy is to take a monotone increasing prefix of `N`, then decrease the number before the "cliff" (the index where adjacent digits decrease for the first time) if it exists, and replace the rest of the characters with `9`s.

When does that strategy fail?  If `N = 333222`, then our strategy would give us the candidate answer of `332999` - but this isn't monotone increasing.  However, since we are looking at all indexes before the original first occurrence of a cliff, the only place where a cliff could exist, is next to where we just decremented a digit.

Thus, we can repair our strategy, by successfully morphing our answer `332999 -> 329999 -> 299999` with a linear scan.

**Algorithm**

We'll find the first cliff `S[i-1] > S[i]`.  Then, while the cliff exists, we'll decrement the appropriate digit and move `i` back.  Finally, we'll make the rest of the digits `9`s and return our work.

We can prove our algorithm is correct because every time we encounter a cliff, the digit we decrement has to decrease by at least 1.  Then, the largest possible selection for the rest of the digits is all nines, which is always going to be monotone increasing with respect to the other digits occurring earlier in the number.

<iframe src="https://leetcode.com/playground/yeDAMaRm/shared" frameBorder="0" width="100%" height="242" name="yeDAMaRm"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(D)$$, where $$D \approx \log N$$ is the number of digits in $$N$$.  Each step in the algorithm is a linear scan of the digits.

* Space Complexity: $$O(D)$$, the size of the answer.

---

Analysis written by: [@awice](https://leetcode.com/awice).
