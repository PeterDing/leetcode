# 0818 - Race Car

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming, Heap | [Leetcode](https://leetcode.com/problems/race-car) | [solution](https://leetcode.com/problems/race-car/solution/)


-----------

<p>Your car starts at position 0 and speed +1 on an infinite number line.&nbsp; (Your car can go into negative positions.)</p>

<p>Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).</p>

<p>When you get an instruction &quot;A&quot;, your car does the following:&nbsp;<code>position += speed, speed *= 2</code>.</p>

<p>When you get an instruction &quot;R&quot;, your car does the following: if your speed is positive then&nbsp;<code>speed = -1</code>&nbsp;, otherwise&nbsp;<code>speed = 1</code>.&nbsp; (Your position stays the same.)</p>

<p>For example, after commands &quot;AAR&quot;, your car goes to positions 0-&gt;1-&gt;3-&gt;3, and your speed goes to 1-&gt;2-&gt;4-&gt;-1.</p>

<p>Now for some target position, say the <strong>length</strong> of the shortest sequence of instructions to get there.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> 
target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The shortest instruction sequence is &quot;AA&quot;.
Your position goes from 0-&gt;1-&gt;3.
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> 
target = 6
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
The shortest instruction sequence is &quot;AAARA&quot;.
Your position goes from 0-&gt;1-&gt;3-&gt;7-&gt;7-&gt;6.
</pre>

<p>&nbsp;</p>

<p><strong>Note: </strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10000</code>.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---

#### Approach Framework

**Explanation**

Let $$A^k$$ denote the command $$A A A \cdots A$$ (k times).

Starting with an `"R"` command doesn't help, and as the final sequence does not end on an `"R"`, so we have some sequence like $$R A^{k_1} R A^{k_2} \cdots R A^{k_n}$$ which could be instead $$A^{k_2} R A^{k_3} R \cdots A^{k_n} R R A^{k_1}$$ for the same final position of the car.  (Here, $$k_i \geq 0$$, where $$A^0$$ means no command.)

So let's suppose our command is always of the form $$A^{k_1} R A^{k_2} R \cdots A^{k_n}$$.  Note that under such a command, the car will move to final position $$(2^{k_1} - 1) - (2^{k_2} - 1) + (2^{k_3} - 1) - \cdots $$.

Without loss of generality, we can say that ($$k_i$$, $$i$$ odd) is monotone decreasing, and ($$k_i$$, $$i$$ even) is also monotone decreasing.

Also because terms will cancel out, we can also ignore the possibility that $$k_i = k_j$$ (for $$i, j$$ with different parity).

A key claim is that $$k_i$$ is bounded by $$a+1$$, where $$a$$ is the smallest integer such that $$2^a \geq \text{target}$$ - basically, if you drive past the target, you don't need to keep driving.  This is because it adds another power of two (as $$2^{k_i} - 1 = \sum_{j < k_i} 2^j$$) to the position that must get erased by one or more negative terms later (in whole or in part), as it is not part of the target.

---

#### Approach #1: Dijkstra's [Accepted]

**Intuition**

With some `target`, we have different moves we can perform (such as $$k_1 = 0, 1, 2, \cdots$$, using the notation from our *Approach Framework*), with different costs.

This is an ideal setup for Dijkstra's algorithm, which can help us find the shortest cost path in a weighted graph.  

**Algorithm**

Dijkstra's algorithm uses a priority queue to continually searches the path with the lowest cost to destination, so that when we reach the target, we know it must have been through the lowest cost path.  Refer to [this link](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) for more detail.

Back to the problem, as described above, we have some `barrier` where we are guaranteed to never cross.  We will also handle negative targets; in total we will have `2 * barrier + 1` nodes.

After, we could move `walk = 2**k - 1` steps for a cost of `k + 1` (the `1` is to reverse).  If we reach our destination exactly, we don't need the `R`, so it is just `k` steps.

<iframe src="https://leetcode.com/playground/qNruc33Y/shared" frameBorder="0" width="100%" height="500" name="qNruc33Y"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(T \log T)$$.  There are $$O(T)$$ nodes, we process each one using $$O(\log T)$$ work (both popping from the heap and adding the edges).

* Space Complexity: $$O(T)$$.

---

#### Approach #2: Dynamic Programming [Accepted]

**Intuition and Algorithm**

As in our *Approach Framework*, we've framed the problem as a series of moves $$k_i$$.

Now say we have some target `2**(k-1) <= t < 2**k` and we want to know the cost to go there, if we know all the other costs `dp[u]` (for `u < t`).

If `t == 2**k - 1`, the cost is just `k`: we use the command $$A^k$$, and clearly we can't do better.

Otherwise, we might drive without crossing the target for a position change of $$2^{k-1} - 2**j$$, by the command $$A^{k-1} R A^{j} R$$, for a total cost of $$k - 1 + j + 2$$.

Finally, we might drive $$2^k - 1$$ which crosses the target, by the command $$A^k R$$, for a total cost of $$k + 1$$.

We can use dynamic programming together with the above recurrence to implement the code below.

<iframe src="https://leetcode.com/playground/ZF65uxfa/shared" frameBorder="0" width="100%" height="412" name="ZF65uxfa"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(T \log T)$$.  Each node `i` does $$\log i$$ work.

* Space Complexity: $$O(T)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
