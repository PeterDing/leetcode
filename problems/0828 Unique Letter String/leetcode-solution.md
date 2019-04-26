# 0828 - Unique Letter String

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Two Pointers | [Leetcode](https://leetcode.com/problems/unique-letter-string) | [solution](https://leetcode.com/problems/unique-letter-string/solution/)


-----------

<p>A character is unique in string <code>S</code> if it occurs exactly once in it.</p>

<p>For example, in string <code>S = &quot;LETTER&quot;</code>, the only unique characters are <code>&quot;L&quot;</code> and <code>&quot;R&quot;</code>.</p>

<p>Let&#39;s define <code>UNIQ(S)</code> as the number of unique characters in string <code>S</code>.</p>

<p>For example, <code>UNIQ(&quot;LETTER&quot;) =&nbsp; 2</code>.</p>

<p>Given a string <code>S</code> with only uppercases, calculate the sum of <code>UNIQ(substring)</code> over all non-empty substrings of <code>S</code>.</p>

<p>If there are two or more equal substrings at different positions in <code>S</code>, we consider them different.</p>

<p>Since the answer can be very large, return&nbsp;the answer&nbsp;modulo&nbsp;<code>10 ^ 9 + 7</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;ABC&quot;
<strong>Output: </strong>10
<strong>Explanation: </strong>All possible substrings are: &quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;AB&quot;,&quot;BC&quot; and &quot;ABC&quot;.
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;ABA&quot;
<strong>Output: </strong>8
<strong>Explanation: </strong>The same as example 1, except uni(&quot;ABA&quot;) = 1.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong> <code>0 &lt;= S.length &lt;= 10000</code>.</p>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Maintain Answer of Suffix [Accepted]

**Intuition**

We can think of substrings as two for-loops, for the left and right boundary of the substring.  To get a handle on this problem, let's try to answer the question: what is the answer over all substrings that start at index `i`?  Let's call this $$F(i)$$.  If we can compute this faster than linear (brute force), we have an approach.

Now let $$U$$ be the unique letters function, eg. $$U(\text{"LETTER"}) = 2$$.

The key idea is we can write $$U$$ as a sum of disjoint functions over each character.  Let $$U_{\text{"A"}}(x)$$ be $$1$$ if $$\text{"A"}$$ occurs exactly once in $$x$$, otherwise $$0$$, and so on with every letter.  Then $$U(x) = \sum_{c \in \mathcal{A}} U_c(x)$$, where $$\mathcal{A} = \{ \text{"A"}, \text{"B"}, \dots \}$$ is the alphabet.

**Algorithm**

This means we only need to answer the following question (26 times, one for each character): how many substrings have exactly one $$\text{"A"}$$?  If we knew that `S[10] = S[14] = S[20] = "A"` (and only those indexes have an `"A"`), then when `i = 8`, the answer is `4` (`j = 10, 11, 12, 13`); when `i = 12` the answer is `6` (`j = 14, 15, 16, 17, 18, 19`), and so on.

In total, $$F(0) = \sum_{c \in \mathcal{A}} \text{index}[c][1] - \text{index}[c][0]$$, where `index[c]` are the indices `i` (in order) where `S[i] == c` (and padded with `S.length` if out of bounds).  In the above example, `index["A"] = [10, 14, 20]`.

Now, we want the final answer of $$\sum_{i \geq 0} F(i)$$.  There is a two pointer approach: how does $$F(1)$$ differ from $$F(0)$$?  If for example `S[0] == "B"`, then most of the sum remains unchanged (specifically, $$\sum_{c \in \mathcal{A}, c \neq \text{"B"}} \text{index}[c][1] - \text{index}[c][0]$$), and only the $$c = \text{"B"}$$ part changes, from $$\text{index}[\text{"B"}][1] - \text{index}[\text{"B"}][0]$$ to $$\text{index}[\text{"B"}][2] - \text{index}[\text{"B"}][1]$$.

We can manage this in general by keeping track of `peek[c]`, which tells us the correct index `i = peek[c]` such that our current contribution by character `c` of $$F(i)$$ is `index[c][peek[c] + 1] - index[c][peek[c]]`.


<iframe src="https://leetcode.com/playground/fkvb227q/shared" frameBorder="0" width="100%" height="500" name="fkvb227q"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity: $$O(N)$$.

---
#### Approach #2: Split by Character [Accepted]

**Intuition**

As in *Approach #1*, we have $$U(x) = \sum_{c \in \mathcal{A}} U_c(x)$$, where $$\mathcal{A} = \{ \text{"A"}, \text{"B"}, \dots \}$$ is the alphabet, and we only need to answer the following question (26 times, one for each character): how many substrings have exactly one $$\text{"A"}$$?

**Algorithm**

Consider how many substrings have a specific $$\text{"A"}$$.  For example, let's say `S` only has three `"A"`'s, at '`S[10] = S[14] = S[20] = "A"`; and we want to know the number of substrings that contain `S[14]`.  The answer is that there are 4 choices for the left boundary of the substring `(11, 12, 13, 14)`, and 6 choices for the right boundary `(14, 15, 16, 17, 18, 19)`.  So in total, there are 24 substrings that have `S[14]` as their unique `"A"`.

Continuing our example, if we wanted to count the number of substrings that have `S[10]`, this would be `10 * 4` - note that when there is no more `"A"` characters to the left of `S[10]`, we have to count up to the left edge of the string.

We can add up all these possibilities to get our final answer.

<iframe src="https://leetcode.com/playground/qiRvovcd/shared" frameBorder="0" width="100%" height="395" name="qiRvovcd"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity: $$O(N)$$.  We could reduce this to $$O(\mathcal{A})$$ if we do not store all the indices, but compute the answer on the fly.

---

Analysis written by: [@awice](https://leetcode.com/awice).  Approach #2 inspired by [@lee215](http://leetcode.com/lee215).
