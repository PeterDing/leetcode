# 0073 - Set Matrix Zeroes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/set-matrix-zeroes) | [solution](https://leetcode.com/problems/set-matrix-zeroes/solution/)


-----------

<p>Given a <em>m</em> x <em>n</em> matrix, if an element is 0, set its entire row and column to 0. Do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
[
&nbsp; [1,1,1],
&nbsp; [1,0,1],
&nbsp; [1,1,1]
]
<strong>Output:</strong> 
[
&nbsp; [1,0,1],
&nbsp; [0,0,0],
&nbsp; [1,0,1]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
[
&nbsp; [0,1,2,0],
&nbsp; [3,4,5,2],
&nbsp; [1,3,1,5]
]
<strong>Output:</strong> 
[
&nbsp; [0,0,0,0],
&nbsp; [0,4,5,0],
&nbsp; [0,3,1,0]
]
</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>A straight forward solution using O(<em>m</em><em>n</em>) space is probably a bad idea.</li>
	<li>A simple improvement uses O(<em>m</em> + <em>n</em>) space, but still not the best solution.</li>
	<li>Could you devise a constant space solution?</li>
</ul>


-----------


## Similar Problems

- [Medium] [Game of Life](game-of-life)




## Solution:

[TOC]

## Solution
---

The question seems to be pretty simple but the trick here is that we need to modify the given matrix in place i.e. our space complexity needs to $$O(1)$$.

We will go through three different approaches to the question. The first approach makes use of additional memory while the other two don't.
<br/>
<br/>

---

#### Approach 1: Additional Memory Approach

**Intuition**

If any cell of the matrix has a zero we can record its row and column number. All the cells of this recorded row and column can be marked zero in the next iteration.

**Algorithm**

1. We make a pass over our original array and look for zero entries.
2. If we find that an entry at `[i, j]` is 0, then we need to record somewhere the row `i` and column `j`.
3. So, we use two `sets`, one for the rows and one for the columns.
    <pre>
    if cell[i][j] == 0 {
        row_set.add(i)
        column_set.add(j)
    }</pre>

4. Finally, we iterate over the original matrix. For every cell we check if the row `r` or column `c` had been marked earlier. If any of them was marked, we set the value in the cell to 0.
    <pre>
    if r in row_set or c in column_set {
        cell[r][c] = 0
    }</pre>

<iframe src="https://leetcode.com/playground/kPV6bYHr/shared" frameBorder="0" width="100%" height="500" name="kPV6bYHr"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(M \times N)$$ where M and N are the number of rows and columns respectively.

* Space Complexity: $$O(M + N)$$.
<br/>
<br/>

---

#### Approach 2: Brute O(1) space.

**Intuition**

In the above approach we use additional memory to keep a track of rows and columns which need to be set to zero. This additional use of space can be avoided by manipulating the original array instead.  

**Algorithm**

1. Iterate over the original array and if we find an entry, say `cell[i][j]` to be 0, then we iterate over row `i` and column `j` separately and set all the **non zero** elements to some high negative dummy value (say `-1000000`). Note, choosing the right dummy value for your solution is dependent on the constraints of the problem. Any value outside the range of permissible values in the matrix will work as a dummy value. 
2. Finally, we iterate over the original matrix and if we find an entry to be equal to the high negative value (constant defined initially in the code as `MODIFIED`), then we set the value in the cell to 0.

<iframe src="https://leetcode.com/playground/3qUZbzut/shared" frameBorder="0" width="100%" height="500" name="3qUZbzut"></iframe>

**Complexity Analysis**

* Time Complexity : $$O((M \times N) \times (M + N))$$ where M and N are the number of rows and columns respectively. Even though this solution avoids using space, but is very inefficient since in worst case for every cell we might have to zero out its corresponding row and column. Thus for all $$(M \times N)$$ cells zeroing out $$(M +  N)$$ cells.  
* Space Complexity : $$O(1)$$
<br/>
<br/>

---

#### Approach 3: O(1) Space, Efficient Solution

**Intuition**

The inefficiency in the second approach is that we might be repeatedly setting a row or column even if it was set to zero already. We can avoid this by postponing the step of setting a row or a column to zeroes.

> We can rather use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero. This means for every cell instead of going to $$M+N$$ cells and setting it to zero we just set the flag in two cells.

<pre>
if cell[i][j] == 0 {
    cell[i][0] = 0
    cell[0][j] = 0
}
</pre>

 These flags are used later to update the matrix. If the first cell of a row is set to zero this means the row should be marked zero. If the first cell of a column is set to zero this means the column should be marked zero.

**Algorithm**

1. We iterate over the matrix and we mark the first cell of a row `i` and first cell of a column `j`, if the condition in the pseudo code above is satisfied. i.e. if `cell[i][j] == 0`.

2. The first cell of row and column for the first row and first column is the same i.e. `cell[0][0]`. Hence, we use an additional variable to tell us if the first column had been marked or not and the `cell[0][0]` would be used to tell the same for the first row.

3. Now, we iterate over the original matrix starting from second row and second column i.e. `matrix[1][1]` onwards. For every cell we check if the row `r` or column `c` had been marked earlier by checking the respective first row cell or first column cell. If any of them was marked, we set the value in the cell to 0. Note the first row and first column serve as the `row_set` and `column_set` that we used in the first approach.

5. We then check if `cell[0][0] == 0`, if this is the case, we mark the first row as zero.

6. And finally, we check if the first column was marked, we make all entries in it as zeros.

!?!../Documents/73_Matrix_Zeroes.json:1000,400!?!

In the above animation we iterate all the cells and mark the corresponding first row/column cell incase of a cell with zero value.

<center>
<img src="../Figures/73/MatrixZeros_18_1.png" width="400"/>
</center>

We iterate the matrix we got from the above steps and mark respective cells zeroes.

<center>
<img src="../Figures/73/MatrixZeros_18_2.png" width="400"/>
</center>

<br>

<iframe src="https://leetcode.com/playground/2tGE5XF8/shared" frameBorder="0" width="100%" height="500" name="2tGE5XF8"></iframe>

**Complexity Analysis**

* Time Complexity : $$O(M \times N)$$
* Space Complexity : $$O(1)$$

<br/><br/>

---
Analysis written by: [@godayaldivya](https://leetcode.com/godayaldivya/).
