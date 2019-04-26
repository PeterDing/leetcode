# 0542 - 01 Matrix

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Depth-first Search, Breadth-first Search | [Leetcode](https://leetcode.com/problems/01-matrix) | [solution](https://leetcode.com/problems/01-matrix/solution/)


-----------

<p>Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.</p>

<p>The distance between two adjacent cells is 1.</p>

<p>&nbsp;</p>

<p><b>Example 1: </b></p>

<pre>
<strong>Input:</strong>
[[0,0,0],
 [0,1,0],
 [0,0,0]]

<strong>Output:</strong>
[[0,0,0],
&nbsp;[0,1,0],
&nbsp;[0,0,0]]
</pre>

<p><b>Example 2: </b></p>

<pre>
<b>Input:</b>
[[0,0,0],
 [0,1,0],
 [1,1,1]]

<strong>Output:</strong>
[[0,0,0],
 [0,1,0],
 [1,2,1]]
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The number of elements of the given matrix will not exceed 10,000.</li>
	<li>There are at least one 0 in the given matrix.</li>
	<li>The cells are adjacent in only four directions: up, down, left and right.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach #1 Brute force [Time Limit Exceeded]

**Intuition**

Do what the question says.

**Algorithm**

* Initialize `dist[i][j]=INT_MAX` for all `{i,j}` cells.
* Iterate over the matrix.
  + If cell is `0`, `dist[i][j]=0`,
  + Else, for each `1` cell,
    - Iterate over the entire matrix
    - If the cell is `0`, calculate its distance from current cell as `abs(k-i)+abs(l-j)`.
    - If the distance is smaller than the current distance, update it.


<iframe src="https://leetcode.com/playground/WrxDXrW3/shared" frameBorder="0" name="WrxDXrW3" width="100%" height="445"></iframe>

**Complexity Analysis**

* Time complexity: $$O((r \cdot c)^2)$$.
Iterating over the entire matrix for each `1` in the matrix.

* Space complexity: $$O(r \cdot c)$$.
No extra space required than the `vector<vector<int> > dist`

---
#### Approach #2 Using BFS [Accepted]

**Intuition**

*A better brute force*:
Looking over the entire matrix appears wasteful and hence, we can use Breadth First Search(BFS) to limit the search to the nearest `0` found for each `1`. As soon as a `0` appears during the BFS, we know that the `0` is nearest, and hence, we move to the next `1`.

*Think again*:
But, in this approach, we will only be able to update the distance of one `1` using one BFS, which could in fact, result in slightly higher complexity than the Approach #1 brute force.
But hey,this could be optimised if we start the BFS from `0`s and thereby, updating the distances of all the `1`s in the path.

**Algorithm**

* For our BFS routine, we keep a queue, `q` to maintain the queue of cells to be examined next.
* We start by adding all the cells with `0`s to `q`.
* Intially, distance for each `0` cell is `0` and distance for each `1` is `INT_MAX`, which is updated during the BFS.
* Pop the cell from queue, and examine its neighbours. If the new calculated distance for neighbour `{i,j}` is smaller, we add `{i,j}` to `q` and update `dist[i][j]`.


<iframe src="https://leetcode.com/playground/abTJGHUf/shared" frameBorder="0" name="abTJGHUf" width="100%" height="515"></iframe>

**Complexity analysis**

* Time complexity: $$O(r \cdot c)$$.
  + Since, the new cells are added to the queue only if their current distance is greater than the calculated distance, cells are not likely to be added multiple times.

* Space complexity: $$O(r \cdot c)$$. Additional $$O(r \cdot c)$$ for queue than in Approach #1

---
#### Approach #3 DP Approach [Accepted]

**Intuition**

The distance of a cell from `0` can be calculated if we know the nearest distance for all the neighbours, in which case the distance is minimum distance of any neightbour + 1. And, instantly, the word come to mind DP!!  
For each `1`, the minimum path to `0` can be in any direction. So, we need to check all the 4 direction. In one iteration from top to bottom, we can check left and top directions, and we need another iteration from bottom to top to check for right and bottom direction.

**Algorithm**

* Iterate the matrix from top to bottom-left to right:
  + Update
  $$\text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j-1],\text{dist}[i-1][j])+1)$$
  i.e., minimum of the current dist and distance from top or left neighbour +1, that would have been already calculated previously in the current iteration.
* Now, we need to do the back iteration in the similar manner: from bottom to top-right to left:
  + Update
  $$\text{dist}[i][j]=\min(\text{dist}[i][j],\min(\text{dist}[i][j+1],\text{dist}[i+1][j])+1)$$
  i.e. minimum of current dist and distances calculated from bottom and right neighbours, that would be already available in current iteration.


<iframe src="https://leetcode.com/playground/ZLQD7VF7/shared" frameBorder="0" name="ZLQD7VF7" width="100%" height="515"></iframe>

**Complexity analysis**

* Time complexity: $$O(r \cdot c)$$. 2 passes of $$r \cdot c$$ each
* Space complexity: $$O(r \cdot c)$$. No additional space required than `dist vector<vector<int> >`

---
Analysis written by [@abhinavbansal0](https://leetcode.com/abhinavbansal0).
