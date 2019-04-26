# 0686 - Repeated String Match

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/repeated-string-match) | [solution](https://leetcode.com/problems/repeated-string-match/solution/)


-----------

<p>Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.</p>

<p>For example, with A = &quot;abcd&quot; and B = &quot;cdabcdab&quot;.</p>

<p>Return 3, because by repeating A three times (&ldquo;abcdabcdabcd&rdquo;), B is a substring of it; and B is not a substring of A repeated two times (&quot;abcdabcd&quot;).</p>

<p><b>Note:</b><br />
The length of <code>A</code> and <code>B</code> will be between 1 and 10000.</p>


-----------


## Similar Problems

- [Easy] [Repeated Substring Pattern](repeated-substring-pattern)




## Solution:

[TOC]

#### Approach #1: Ad-Hoc [Accepted]

**Intuition**

The question can be summarized as "What is the smallest `k` for which `B` is a substring of `A * k`?"  We can just try every `k`.

**Algorithm**

Imagine we wrote `S = A+A+A+...`.  If `B` is to be a substring of `S`, we only need to check whether some `S[0:], S[1:], ..., S[len(A) - 1:]` starts with `B`, as `S` is long enough to contain `B`, and `S` has period at most `len(A)`.

Now, suppose `q` is the least number for which `len(B) <= len(A * q)`.  We only need to check whether `B` is a substring of `A * q` or `A * (q+1)`.  If we try `k < q`, then `B` has larger length than `A * q` and therefore can't be a substring.  When `k = q+1`, `A * k` is already big enough to try all positions for `B`; namely, `A[i:i+len(B)] == B` for `i = 0, 1, ..., len(A) - 1`.

<iframe src="https://leetcode.com/playground/gTtmgvev/shared" frameBorder="0" name="gTtmgvev" width="100%" height="224"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N*(N+M))$$, where $$M, N$$ are the lengths of strings `A, B`.  We create two strings `A * q`, `A * (q+1)` which have length at most `O(M+N)`.  When checking whether `B` is a substring of `A`, this check takes naively the product of their lengths.

* Space complexity: As justified above, we created strings that used $$O(M+N)$$ space.

---

#### Approach #2: Rabin-Karp (Rolling Hash) [Accepted]

**Intuition**

As in *Approach #1*, we've reduced the problem to deciding whether B is a substring of some `A * k`.  Using the following technique, we can decide whether `B` is a substring in $$O(len(A) * k)$$ time.

**Algorithm**

For strings $$S$$, consider each $$S[i]$$ as some integer ASCII code.  Then for some prime $$p$$, consider the following function modulo some prime modulus $$\mathcal{M}$$:

$$\text{hash}(S) = \sum_{0 \leq i < len(S)} p^i * S[i]$$

Notably, $$\text{hash}(S[1:] + x) = \frac{(\text{hash}(S) - S[0])}{p} + p^{n-1} x$$.  This shows we can get the hash of every substring of `A * q` in time complexity linear to it's size.  (We will also use the fact that $$p^{-1} = p^{\mathcal{M}-2} \mod \mathcal{M}$$.)

However, hashes may collide haphazardly.  To be absolutely sure in theory, we should check the answer in the usual way.  The expected number of checks we make is in the order of $$1 + \frac{s}{\mathcal{M}}$$ where $$s$$ is the number of substrings we computed hashes for (assuming the hashes are equally distributed), which is effectively 1.

<iframe src="https://leetcode.com/playground/DKSFgXSr/shared" frameBorder="0" name="DKSFgXSr" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(M+N)$$ (at these sizes), where $$M, N$$ are the lengths of strings `A, B`.  As in *Approach #1*, we justify that `A * (q+1)` will be of length $$O(M + N)$$, and computing the rolling hashes was linear work.  We will also do a linear $$O(N)$$ final check of our answer $$1 + O(M) / \mathcal{M}$$ times.  In total, this is $$O(M+N + N(1 + \frac{M}{\mathcal{M}}))$$ work.  Since $$M \leq 10000 < \mathcal{M} = 10^9 + 7$$, we can consider this to be linear behavior.

* Space complexity:  $$O(1)$$.  Only integers were stored with additional memory.

---

Analysis written by: [@awice](https://leetcode.com/awice)
