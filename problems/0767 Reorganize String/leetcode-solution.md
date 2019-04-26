# 0767 - Reorganize String

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String, Heap, Greedy, Sort | [Leetcode](https://leetcode.com/problems/reorganize-string) | [solution](https://leetcode.com/problems/reorganize-string/solution/)


-----------

<p>Given a string <code>S</code>, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.</p>

<p>If possible, output any possible result.&nbsp; If not possible, return the empty string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;aab&quot;
<strong>Output:</strong> &quot;aba&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;aaab&quot;
<strong>Output:</strong> &quot;&quot;
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>S</code> will consist of lowercase letters and have length in range <code>[1, 500]</code>.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Hard] [Rearrange String k Distance Apart](rearrange-string-k-distance-apart)

- [Medium] [Task Scheduler](task-scheduler)




## Solution:

[TOC]

---
#### Approach #1: Sort by Count [Accepted]

**Intuition**

If we should make no two `'a'`s adjacent, it is natural to write `"aXaXaXa..."` where `"X"` is some letter.  For now, let's assume that the task is possible (ie. the answer is not `""`.)

Let's sort the string `S`, so all of the same kind of letter occur in continuous *blocks*.  Then when writing in the following interleaving pattern, like `S[3], S[0], S[4], S[1], S[5], S[2]`, adjacent letters never touch.  (The specific interleaving pattern is that we start writing at index 1 and step by 2; then start from index 0 and step by 2.)

The exception to this rule is if `N` is odd, and then when interleaving like `S[2], S[0], S[3], S[1], S[4]`, we might fail incorrectly if there is a block of the same 3 letters starting at `S[0]` or `S[1]`.  To prevent failing erroneously in this case, we need to make sure that the most common letters all occur at the end.

Finally, it is easy to see that if `N` is the length of the string, and the count of some letter is greater than `(N+1) / 2`, the task is impossible.

**Algorithm**

Find the count of each character, and use it to sort the string by count.

If at some point the number of occurrences of some character is greater than `(N + 1) / 2`, the task is impossible.

Otherwise, interleave the characters in the order described above.

<iframe src="https://leetcode.com/playground/HYKSoqaR/shared" frameBorder="0" width="100%" height="480" name="HYKSoqaR"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(\mathcal{A}(N + \log{\mathcal{A}}))$$, where $$N$$ is the length of $$S$$, and $$\mathcal{A}$$ is the size of the alphabet.  In Java, our implementation is $$O(N + \mathcal{A} \log {\mathcal{A}})$$.  If $$\mathcal{A}$$ is fixed, this complexity is $$O(N)$$.

* Space Complexity: $$O(N)$$.  In Java, our implementation is $$O(N + \mathcal{A})$$.

---
#### Approach #2: Greedy with Heap [Accepted]

**Intuition**

One consequence of the reasoning in *Approach #1*, is that a greedy approach that tries to write the most common letter (that isn't the same as the previous letter written) will work.

The reason is that the task is only impossible if the frequency of a letter exceeds `(N+1) / 2`.  Writing the most common letter followed by the second most common letter keeps this invariant.

A heap is a natural structure to repeatedly return the current top 2 letters with the largest remaining counts.

**Approach**

We store a heap of (count, letter).  [In Python, our implementation stores negative counts.]

We pop the top two elements from the heap (representing different letters with positive remaining count), and then write the most frequent one that isn't the same as the most recent one written.  After, we push the correct counts back onto the heap.

Actually, we don't even need to keep track of the most recent one written.  If it is possible to organize the string, the letter written second can never be written first in the very next writing.

At the end, we might have one element still on the heap, which must have a count of one.  If we do, we'll add that to the answer too.

**Proof of Invariant**

The invariant mentioned in the *[Intuition]* section seems true when playing with it, but here is a proof.  Let $$C_i$$ be the count of each letter yet to be written, and $$N$$ be the number of letters left to write.  We want to show this procedure maintains the invariant $$2 * \max\limits_i(C_i) \leq N+1$$.

Say $$C'_i$$ are the counts after one writing step.

* If $$\max(C_i) > \text{3rdmax}(C_i)$$, then $$\max(C'_i) \leq \max(C_i) - 1$$, and so $$2\max(C'_i) \leq 2\max(C_i) - 2 \leq N-1$$ as desired.

* If $$M = \max(C_i) = \text{3rdmax}(C_i)$$, then $$3M \leq N$$.  Also, because $$M \geq 1$$, $$N \geq 3$$.  Then, $$2M \leq \frac{2N}{3} \leq N-1$$ as desired.

This completes the proof of this invariant.

<iframe src="https://leetcode.com/playground/Emwok2sq/shared" frameBorder="0" width="100%" height="500" name="Emwok2sq"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N \log{\mathcal{A}}))$$, where $$N$$ is the length of $$S$$, and $$\mathcal{A}$$ is the size of the alphabet.  If $$\mathcal{A}$$ is fixed, this complexity is $$O(N)$$.

* Space Complexity: $$O(\mathcal{A})$$.  If $$\mathcal{A}$$ is fixed, this complexity is $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
