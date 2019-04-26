# 0756 - Pyramid Transition Matrix

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Bit Manipulation, Depth-first Search | [Leetcode](https://leetcode.com/problems/pyramid-transition-matrix) | [solution](https://leetcode.com/problems/pyramid-transition-matrix/solution/)


-----------

<p>
We are stacking blocks to form a pyramid.  Each block has a color which is a one letter string, like `'Z'`.
</p><p>
For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`.  We are allowed to place the block there only if `(A, B, C)` is an allowed triple.
</p><p>
We start with a bottom row of <code>bottom</code>, represented as a single string.  We also start with a list of allowed triples <code>allowed</code>.  Each allowed triple is represented as a string of length 3.
</p><p>
Return true if we can build the pyramid all the way to the top, otherwise false.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
<b>Output:</b> true
<b>Explanation:</b>
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
<b>Output:</b> false
<b>Explanation:</b>
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>bottom</code> will be a string with length in range <code>[2, 8]</code>.</li>
<li><code>allowed</code> will have length in range <code>[0, 200]</code>.</li>
<li>Letters in all strings will be chosen from the set <code>{'A', 'B', 'C', 'D', 'E', 'F', 'G'}</code>.</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]


#### Approach #1: State to State Transition [Wrong Answer]

**Intuition and Algorithm**

We model the states that blocks can be in.  Each state is a binary number where the `k`th bit is set if the `k`th type of block is a possibility.  Then, we create a transition map `T[state1][state2] -> state` that takes a left state and a right state and outputs all possible parent states.

At the end, applying these transitions is straightforward.  However, this approach is not correct, because the transitions are not independent.  If for example we have states in a row `A, {B or C}, A`, and allowed triples `(A, B, D)`, `(C, A, D)`, then regardless of the choice of `{B or C}` we cannot create the next row of the pyramid.

<iframe src="https://leetcode.com/playground/FoBNczLu/shared" frameBorder="0" width="100%" height="429" name="FoBNczLu"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(2^{2\mathcal{A}}A + N^2)$$, where $$N$$ is the length of `bottom`, $$A$$ is the length of `allowed`, and $$\mathcal{A}$$ is the size of the alphabet.

* Space Complexity: $$O(2^{2\mathcal{A}})$$ in additional space complexity.

---
#### Approach #2: Depth-First Search [Accepted]

**Intuition**

We exhaustively try every combination of blocks.

**Algorithm**

We can work in either strings or integers, but we need to create a transition map `T` from the list of allowed triples.  This map `T[x][y] = {set of z}` will be all possible parent blocks for a left child of `x` and a right child of `y`.  When we work in strings, we use `Set`, and when we work in integers, we will use the set bits of the result integer.

Afterwards, to `solve` a row, we generate every possible combination of the next row and solve them.  If any of those new rows are solvable, we return `True`, otherwise `False`.

We can also cache intermediate results, saving us time.  This is illustrated in the comments for Python.  For Java, all caching is done with lines of code that mention the integer `R`.

<iframe src="https://leetcode.com/playground/W723Lgci/shared" frameBorder="0" width="100%" height="500" name="W723Lgci"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(\mathcal{A}^{N})$$, where $$N$$ is the length of `bottom`, and $$\mathcal{A}$$ is the size of the alphabet, and assuming we cache intermediate results.  We might try every sequence of letters for each row.  [The total complexity is because $$O(\sum_{k}^n \mathcal{A}^{k})$$ is a geometric series equal to $$O(\frac{\mathcal{A^{n+1}}-1}{\mathcal{A}-1})$$.]  Without intermediate caching, this would be $$O(\mathcal{A}^{N^2})$$.

* Space Complexity: $$O(N^2)$$ additional space complexity.

---

Analysis written by: [@awice](https://leetcode.com/awice).
