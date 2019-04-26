# 0744 - Find Smallest Letter Greater Than Target

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Binary Search | [Leetcode](https://leetcode.com/problems/find-smallest-letter-greater-than-target) | [solution](https://leetcode.com/problems/find-smallest-letter-greater-than-target/solution/)


-----------

<p>
Given a list of sorted characters <code>letters</code> containing only lowercase letters, and given a target letter <code>target</code>, find the smallest element in the list that is larger than the given target.
</p><p>
Letters also wrap around.  For example, if the target is <code>target = 'z'</code> and <code>letters = ['a', 'b']</code>, the answer is <code>'a'</code>.
</p>

<p><b>Examples:</b><br />
<pre>
<b>Input:</b>
letters = ["c", "f", "j"]
target = "a"
<b>Output:</b> "c"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "c"
<b>Output:</b> "f"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "d"
<b>Output:</b> "f"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "g"
<b>Output:</b> "j"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "j"
<b>Output:</b> "c"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "k"
<b>Output:</b> "c"
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>letters</code> has a length in range <code>[2, 10000]</code>.</li>
<li><code>letters</code> consists of lowercase letters, and contains at least 2 unique letters.</li>
<li><code>target</code> is a lowercase letter.</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

#### Approach #1: Record Letters Seen [Accepted]

**Intuition and Algorithm**

Let's scan through `letters` and record if we see a letter or not.  We could do this with an array of size 26, or with a Set structure.

Then, for every next letter (starting with the letter that is one greater than the target), let's check if we've seen it.  If we have, it must be the answer.

<iframe src="https://leetcode.com/playground/auZQ7CwK/shared" frameBorder="0" width="100%" height="276" name="auZQ7CwK"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `letters`.  We scan every element of the array.

* Space Complexity: $$O(1)$$, the maximum size of `seen`.

---
#### Approach #2: Linear Scan [Accepted]

**Intuition and Algorithm**

Since `letters` are sorted, if we see something larger when scanning form left to right, it must be the answer.  Otherwise, (since `letters` is non-empty), the answer is `letters[0]`.

<iframe src="https://leetcode.com/playground/RvMYaXpq/shared" frameBorder="0" width="100%" height="174" name="RvMYaXpq"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `letters`.  We scan every element of the array.

* Space Complexity: $$O(1)$$, as we maintain only pointers.

---
#### Approach #3: Binary Search [Accepted]

**Intuition and Algorithm**

Like in *Approach #2*, we want to find something larger than target in a sorted array.  This is ideal for a *binary search*: Let's find the rightmost position to insert `target` into `letters` so that it remains sorted.

Our binary search (a typical one) proceeds in a number of rounds.  At each round, let's maintain the *loop invariant* that the answer must be in the interval `[lo, hi]`.  Let `mi = (lo + hi) / 2`.  If `letters[mi] <= target`, then we must insert it in the interval `[mi + 1, hi]`.  Otherwise, we must insert it in the interval `[lo, mi]`.

At the end, if our insertion position says to insert `target` into the last position `letters.length`, we return `letters[0]` instead.  This is what the modulo operation does.

<iframe src="https://leetcode.com/playground/bQDjgxiu/shared" frameBorder="0" width="100%" height="242" name="bQDjgxiu"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(\log N)$$, where $$N$$ is the length of `letters`.  We peek only at $$\log N$$ elements in the array.

* Space Complexity: $$O(1)$$, as we maintain only pointers.

---

Analysis written by: [@awice](https://leetcode.com/awice).
