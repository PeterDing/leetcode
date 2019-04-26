# 0691 - Stickers to Spell Word

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming, Backtracking | [Leetcode](https://leetcode.com/problems/stickers-to-spell-word) | [solution](https://leetcode.com/problems/stickers-to-spell-word/solution/)


-----------

<p>
We are given N different types of stickers.  Each sticker has a lowercase English word on it.
</p><p>
You would like to spell out the given <code>target</code> string by cutting individual letters from your collection of stickers and rearranging them.
</p><p>
You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
</p><p>
What is the minimum number of stickers that you need to spell out the <code>target</code>?  If the task is impossible, return -1.
</p>

<p><b>Example 1:</b></p>
<p>Input:<pre>
["with", "example", "science"], "thehat"
</pre></p>

<p>Output:<pre>
3
</pre></p>

<p>Explanation:<pre>
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
</pre></p>

<p><b>Example 2:</b></p>
<p>Input:<pre>
["notice", "possible"], "basicbasic"
</pre></p>

<p>Output:<pre>
-1
</pre></p>

<p>Explanation:<pre>
We can't form the target "basicbasic" from cutting letters from the given stickers.
</pre></p>

<p><b>Note:</b>
<li><code>stickers</code> has length in the range <code>[1, 50]</code>.</li>
<li><code>stickers</code> consists of lowercase English words (without apostrophes).</li>
<li><code>target</code> has length in the range <code>[1, 15]</code>, and consists of lowercase English letters.</li>
<li>In all test cases, all words were chosen <u>randomly</u> from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.</li>
<li>The time limit may be more challenging than usual.  It is expected that a 50 sticker test case can be solved within 35ms on average.</li>
</p>

-----------


## Similar Problems

- [Easy] [Ransom Note](ransom-note)




## Solution:

[TOC]

#### Approach 1: Optimized Exhaustive Search

<br>

**Intuition**

A natural answer is to exhaustively search combinations of stickers.  Because the data is randomized, there are many heuristics available to us that will make this faster.

* For all stickers, we can ignore any letters that are not in the target word.

* When our candidate answer won't be smaller than an answer we have already found, we can stop searching this path.

* We should try to have our exhaustive search bound the answer as soon as possible, so the effect described in the above point happens more often.

* When a sticker dominates another, we shouldn't include the dominated sticker in our sticker collection.  [Here, we say a sticker `A` dominates `B` if `A.count(letter) >= B.count(letter)` for all letters.]

<br>

**Algorithm**

Firstly, for each sticker, let's create a count of that sticker (a mapping `letter -> sticker.count(letter)`) that does not consider letters not in the target word.  Let `A` be an array of these counts.  Also, let's create `t_count`, a count of our `target` word.

Secondly, let's remove dominated stickers.  Because dominance is a transitive relation, we only need to check if a sticker is not dominated by any other sticker once - the ones that aren't dominated are included in our collection.

We are now ready to begin our exhaustive search.  A call to `search(ans)` denotes that we want to decide the minimum number of stickers we can used in `A` to satisfy the target count `t_count`.  `ans` will store the currently formed answer, and `best` will store the current best answer.

If our current answer can't beat our current best answer, we should stop searching.  Also, if there are no stickers left and our target is satisfied, we should update our answer.

Otherwise, we want to know the maximum number of this sticker we can use.  For example, if this sticker is `'abb'` and our target is `'aaabbbbccccc'`, then we could use a maximum of 3 stickers.  This is the maximum of `math.ceil(target.count(letter) / sticker.count(letter))`, taken over all `letter`s in `sticker`.  Let's call this quantity `used`.

After, for the sticker we are currently considering, we try to use `used` of them, then `used - 1`, `used - 2` and so on.  The reason we do it in this order is so that we can arrive at a value for `best` more quickly, which will stop other branches of our exhaustive search from continuing.

The Python version of this solution showcases using `collections.Counter` as a way to simplify some code sections, whereas the Java solution sticks to arrays.

<iframe src="https://leetcode.com/playground/KP3fS7G3/shared" frameBorder="0" name="KP3fS7G3" width="100%" height="515"></iframe>

<br>

**Complexity Analysis**

* Time Complexity: Let $$N$$ be the number of stickers, and $$T$$ be the number of letters in the target word.  A bound for time complexity is $$O(N^{T+1} T^2)$$: for each sticker, we'll have to try using it up to $$T+1$$ times, and updating our target count costs $$O(T)$$, which we do up to $$T$$ times.  Alternatively, since the answer is bounded at $$T$$, we can prove that we can only search up to $$\binom{N+T-1}{T-1}$$ times.  This would be $$O(\binom{N+T-1}{T-1} T^2)$$.

* Space Complexity: $$O(N+T)$$, to store `stickersCount`, `targetCount`, and handle the recursive callstack when calling `search`.

<br>

---
#### Approach 2: Dynamic Programming

<br>

**Intuition**

Suppose we need `dp[state]` stickers to satisfy all `target[i]`'s for which the `i`-th bit of `state` is set.  We would like to know `dp[(1 << len(target)) - 1]`.

<br>

**Algorithm**

For each `state`, let's work with it as `now` and look at what happens to it after applying a sticker.  For each letter in the sticker that can satisfy an unset bit of `state`, we set the bit (`now |= 1 << i`).  At the end, we know `now` is the result of applying that sticker to `state`, and we update our `dp` appropriately.

When using Python, we will need some extra techniques from *Approach #1* to pass in time.

<iframe src="https://leetcode.com/playground/JTZ2SYco/shared" frameBorder="0" name="JTZ2SYco" width="100%" height="515"></iframe>

<br>


**Complexity Analysis**

* Time Complexity: $$O(2^T * S * T)$$ where $$S$$ be the total number of letters in all stickers, and $$T$$ be the number of letters in the target word.  We can examine each loop carefully to arrive at this conclusion.

* Space Complexity: $$O(2^T)$$, the space used by `dp`.

<br>

---

Analysis written by: [@awice](https://leetcode.com/awice).  [Approach #2](https://leetcode.com/contest/leetcode-weekly-contest-53/ranking) inspired by [@dreamoon](https://leetcode.com/dreamoon).
