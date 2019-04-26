# 0647 - Palindromic Substrings

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String, Dynamic Programming | [Leetcode](https://leetcode.com/problems/palindromic-substrings) | [solution](https://leetcode.com/problems/palindromic-substrings/solution/)


-----------

<p>Given a string, your task is to count how many palindromic substrings in this string.</p>

<p>The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;abc&quot;
<b>Output:</b> 3
<b>Explanation:</b> Three palindromic strings: &quot;a&quot;, &quot;b&quot;, &quot;c&quot;.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;aaa&quot;
<b>Output:</b> 6
<b>Explanation:</b> Six palindromic strings: &quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;aa&quot;, &quot;aa&quot;, &quot;aaa&quot;.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The input string length won&#39;t exceed 1000.</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Longest Palindromic Substring](longest-palindromic-substring)

- [Medium] [Longest Palindromic Subsequence](longest-palindromic-subsequence)

- [Medium] [Palindromic Substrings](palindromic-substrings)




## Solution:

[TOC]

---
#### Approach #1: Expand Around Center [Accepted]

**Intuition**

Let `N` be the length of the string.  The middle of the palindrome could be in one of `2N - 1` positions: either at letter or between two letters.

For each center, let's count all the palindromes that have this center.  Notice that if `[a, b]` is a palindromic interval (meaning `S[a], S[a+1], ..., S[b]` is a palindrome), then `[a+1, b-1]` is one too.

**Algorithm**

For each possible palindrome center, let's expand our candidate palindrome on the interval `[left, right]` as long as we can.  The condition for expanding is `left >= 0 and right < N and S[left] == S[right]`.  That means we want to count a new palindrome `S[left], S[left+1], ..., S[right]`.

<iframe src="https://leetcode.com/playground/EEGE8AYR/shared" frameBorder="0" width="100%" height="310" name="EEGE8AYR"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$ where $$N$$ is the length of `S`.  Each expansion might do $$O(N)$$ work.

* Space Complexity: $$O(1)$$.

---
#### Approach #2: Manacher's Algorithm [Accepted]

**Intuition**

Manacher's algorithm is a textbook algorithm that finds in linear time, the maximum size palindrome for any possible palindrome center.  If we had such an algorithm, finding the answer is straightforward.

What follows is a discussion of why this algorithm works.

**Algorithm**

Our loop invariants will be that `center, right` is our knowledge of the palindrome with the largest right-most boundary with `center < i`, centered at `center` with right-boundary `right`.  Also, `i > center`, and we've already computed all `Z[j]`'s for `j < i`.

When `i < right`, we reflect `i` about `center` to be at some coordinate `j = 2 * center - i`.  Then, limited to the interval with radius `right - i` and center `i`, the situation for `Z[i]` is the same as for `Z[j]`.

For example, if at some time `center = 7, right = 13, i = 10`, then for a string like `A = '@#A#B#A#A#B#A#$'`, the `center` is at the `'#'` between the two middle `'A'`'s, the right boundary is at the last `'#'`, `i` is at the last `'B'`, and `j` is at the first `'B'`.

Notice that limited to the interval `[center - (right - center), right]` (the interval with center `center` and right-boundary `right`), the situation for `i` and `j` is a reflection of something we have already computed.  Since we already know `Z[j] = 3`, we can quickly find `Z[i] = min(right - i, Z[j]) = 3`.

Now, why is this algorithm linear?  The while loop only checks the condition more than once when `Z[i] = right - i`.  In that case, for each time `Z[i] += 1`, it increments `right`, and `right` can only be incremented up to `2*N+2` times.

Finally, we sum up `(v+1) / 2` for each `v in Z`.  Say the longest palindrome with some given center C has radius R.  Then, the substring with center C and radius R-1, R-2, R-3, ..., 0 are also palindromes.  Example:  `abcdedcba` is a palindrome with center `e`, radius 4:  but `e`, `ded`, `cdedc`, `bcdedcb`, and `abcdedcba` are all palindromes.

We are dividing by 2 because we were using half-lengths instead of lengths.  For example we actually had the palindrome `a#b#c#d#e#d#c#b#a`, so our length is twice as big.

<iframe src="https://leetcode.com/playground/ttFoRCjg/shared" frameBorder="0" width="100%" height="500" name="ttFoRCjg"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the length of `S`.  As discussed above, the complexity is linear.

* Space Complexity: $$O(N)$$, the size of `A` and `Z`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
