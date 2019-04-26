# 0753 - Cracking the Safe

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math, Depth-first Search | [Leetcode](https://leetcode.com/problems/cracking-the-safe) | [solution](https://leetcode.com/problems/cracking-the-safe/solution/)


-----------

<p>
There is a box protected by a password.  The password is <code>n</code> digits, where each letter can be one of the first <code>k</code> digits <code>0, 1, ..., k-1</code>.
</p><p>
You can keep inputting the password, the password will automatically be matched against the last <code>n</code> digits entered.
</p><p>
For example, assuming the password is <code>"345"</code>, I can open it when I type <code>"012345"</code>, but I enter a total of 6 digits.
</p><p>
Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> n = 1, k = 2
<b>Output:</b> "01"
<b>Note:</b> "10" will be accepted too.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> n = 2, k = 2
<b>Output:</b> "00110"
<b>Note:</b> "01100", "10011", "11001" will be accepted too.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>n</code> will be in the range <code>[1, 4]</code>.</li>
<li><code>k</code> will be in the range <code>[1, 10]</code>.</li>
<li><code>k^n</code> will be at most <code>4096</code>.</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

#### Approach #1: Hierholzer's Algorithm [Accepted]

**Intuition**

We can think of this problem as the problem of finding an Euler path (a path visiting every edge exactly once) on the following graph: there are $$k^{n-1}$$ nodes with each node having $$k$$ edges.

For example, when `k = 4, n = 3`, the nodes are `'00', '01', '02', ..., '32', '33'` and each node has 4 edges `'0', '1', '2', '3'`.  A node plus edge represents a *complete edge* and viewing that substring in our answer.

Any connected directed graph where all nodes have equal in-degree and out-degree has an Euler circuit (an Euler path ending where it started.)  Because our graph is highly connected and symmetric, we should expect intuitively that taking any path greedily in some order will probably result in an Euler path.  

This intuition is called Hierholzer's algorithm: whenever there is an Euler cycle, we can construct it greedily.  The algorithm goes as follows:

* Starting from a vertex `u`, we walk through (unwalked) edges until we get stuck.  Because the in-degrees and out-degrees of each node are equal, we can only get stuck at `u`, which forms a cycle.

* Now, for any node `v` we had visited that has unwalked edges, we start a new cycle from `v` with the same procedure as above, and then merge the cycles together to form a new cycle $$u \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow u$$.


**Algorithm**

We will modify our standard depth-first search: instead of keeping track of nodes, we keep track of (complete) edges: `seen` records if an edge has been visited.

Also, we'll need to visit in a sort of "post-order", recording the answer after visiting the edge.  This is to prevent getting stuck.  For example, with `k = 2, n = 2`, we have the nodes `'0', '1'`.  If we greedily visit complete edges `'00', '01', '10'`, we will be stuck at the node `'0'` prematurely.  However, if we visit in post-order, we'll end up visiting `'00', '01', '11', '10'` correctly.

In general, during our Hierholzer walk, we will record the results of other subcycles first, before recording the main cycle we started from, just as in our first description of the algorithm.  Technically, we are recording backwards, as we exit the nodes.

For example, we will walk (in the "original cycle") until we get stuck, then record the node as we exit.  (Every edge walked is always marked immediately so that it can no longer be used.)  Then in the penultimate node of our original cycle, we will do a Hierholzer walk and then record this node; then in the third-last node of our original cycle we will do a Hierholzer walk and then record this node, and so on.


<iframe src="https://leetcode.com/playground/6FQhQc9V/shared" frameBorder="0" width="100%" height="500" name="6FQhQc9V"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(n * k^n)$$.  We visit every edge once in our depth-first search, and nodes take $$O(n)$$ space.

* Space Complexity: $$O(n * k^n)$$, the size of `seen`.

---
#### Approach #2: Inverse Burrows-Wheeler Transform [Accepted]

**Explanation**

If we are familiar with the theory of combinatorics on words, recall that a *Lyndon Word* `L` is a word that is the unique minimum of it's rotations.

One important mathematical result (due to [Fredericksen and Maiorana](http://www-igm.univ-mlv.fr/~perrin/Recherche/Publications/Articles/debruijnRevised3.pdf)), is that the concatenation in lexicographic order of Lyndon words with length dividing `n`, forms a *de Bruijin* sequence: a sequence where every every word (from the $$k^n$$ available) appears as a substring of length `n` (where we are allowed to wrap around.)

For example, when `n = 6, k = 2`, all the Lyndon words with length dividing `n` in lexicographic order are (spaces for convenience):
`0 000001 000011 000101 000111 001 001011 001101 001111 01
010111 011 011111 1`.  It turns out this is the smallest de Bruijin sequence.

We can use the *Inverse Burrows-Wheeler Transform* (IBWT) to generate these Lyndon words.  Consider two sequences: `S` is the alphabet repeated $$k^{n-1}$$ times: `S = 0123...0123...0123....`, and `S'` is the alphabet repeated $$k^{n-1}$$ times for each letter: `S' = 00...0011...1122....`  We can think of `S'` and `S` as defining a permutation, where the `j`-th occurrence of each letter of the alphabet in `S'` maps to the corresponding `j`-th occurrence in `S`.  The cycles of this permutation turn out to be the corresponding smallest de Bruijin sequence ([link](http://www.macs.hw.ac.uk/~markl/Higgins.pdf)).

Under this view, the permutation $$S' \rightarrow S$$ [mapping permutation indices $$(i * k^{n-1} + q) \rightarrow (q * k + i)$$] form the desired Lyndon words.

<iframe src="https://leetcode.com/playground/Xcx7eTBD/shared" frameBorder="0" width="100%" height="463" name="Xcx7eTBD"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(k^n)$$.  We loop through every possible substring.

* Space Complexity: $$O(k^n)$$, the size of `P` and `ans`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
