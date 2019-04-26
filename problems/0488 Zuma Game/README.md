# 0488 - Zuma Game

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Depth-first Search | [Leetcode](https://leetcode.com/problems/zuma-game) | [solution](https://leetcode.com/problems/zuma-game/solution/)


-----------

<p>Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.</p>
<p>
Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.</p>
<p>
Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.
</p>
<pre>
<p><b>Examples:</b><br />
<b>Input:</b> "WRRBBW", "RB"
<b>Output:</b> -1
<b>Explanation:</b> WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

<b>Input:</b> "WWRRBBWW", "WRBRW"
<b>Output:</b> 2
<b>Explanation:</b> WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

<b>Input:</b>"G", "GGGGG"
<b>Output:</b> 2
<b>Explanation:</b> G -> G[G] -> GG[G] -> empty 

<b>Input:</b> "RBYYBBRRB", "YRBGB"
<b>Output:</b> 3
<b>Explanation:</b> RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.</li>
<li>The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.</li>
<li>The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.</li>
<li>Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.</li>
</ol>
</p>

-----------


## Similar Problems




## Thought:
