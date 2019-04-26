# 0649 - Dota2 Senate

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Greedy | [Leetcode](https://leetcode.com/problems/dota2-senate) | [solution](https://leetcode.com/problems/dota2-senate/solution/)


-----------

<p>In the world of Dota2, there are two parties: the <code>Radiant</code> and the <code>Dire</code>.</p>

<p>The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise <code>one</code> of the two rights:</p>

<ol>
	<li><code>Ban one senator&#39;s right</code>:<br />
	A senator can make another senator lose <b>all his rights</b> in this and all the following rounds.</li>
	<li><code>Announce the victory</code>:<br />
	If this senator found the senators who still have rights to vote are all from <b>the same party</b>, he can announce the victory and make the decision about the change in the game.</li>
</ol>

<p>&nbsp;</p>

<p>Given a string representing each senator&#39;s party belonging. The character &#39;R&#39; and &#39;D&#39; represent the <code>Radiant</code> party and the <code>Dire</code> party respectively. Then if there are <code>n</code> senators, the size of the given string will be <code>n</code>.</p>

<p>The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.</p>

<p>Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be <code>Radiant</code> or <code>Dire</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;RD&quot;
<b>Output:</b> &quot;Radiant&quot;
<b>Explanation:</b> The first senator comes from Radiant and he can just ban the next senator&#39;s right in the round 1. 
And the second senator can&#39;t exercise any rights any more since his right has been banned. 
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;RDD&quot;
<b>Output:</b> &quot;Dire&quot;
<b>Explanation:</b> 
The first senator comes from Radiant and he can just ban the next senator&#39;s right in the round 1. 
And the second senator can&#39;t exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator&#39;s right in the round 1. 
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The length of the given string will in the range [1, 10,000].</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Teemo Attacking](teemo-attacking)




## Solution:

[TOC]

---
#### Approach #1: Simulation [Accepted]

**Intuition**

A senator performing a ban doesn't need to use it on another senator immediately.  We can wait to see when another team's senator will vote, then use that ban retroactively.

**Algorithm**

Put the senators in an integer queue: `1` for `'Radiant'` and `0` for `'Dire'`.

Now process the queue: if there is a floating ban for that senator, exercise it and continue.  Otherwise, add a floating ban against the other team, and enqueue this senator again.

<iframe src="https://leetcode.com/playground/zdvGbwLN/shared" frameBorder="0" width="100%" height="497" name="zdvGbwLN"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the size of the senate.  Every vote removes one senator from the other team.

* Space Complexity: $$O(N)$$, the space used by our queue.

---

Analysis written by: [@awice](https://leetcode.com/awice).
