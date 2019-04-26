# 0675 - Cut Off Trees for Golf Event

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Breadth-first Search | [Leetcode](https://leetcode.com/problems/cut-off-trees-for-golf-event) | [solution](https://leetcode.com/problems/cut-off-trees-for-golf-event/solution/)


-----------

<p>You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:</p>

<ol>
	<li><code>0</code> represents the <code>obstacle</code> can&#39;t be reached.</li>
	<li><code>1</code> represents the <code>ground</code> can be walked through.</li>
	<li><code>The place with number bigger than 1</code> represents a <code>tree</code> can be walked through, and this positive number represents the tree&#39;s height.</li>
</ol>

<p>&nbsp;</p>

<p>You are asked to cut off <b>all</b> the trees in this forest in the order of tree&#39;s height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).</p>

<p>You will start from the point (0, 0) and you should output the minimum steps <b>you need to walk</b> to cut off all the trees. If you can&#39;t cut off all the trees, output -1 in that situation.</p>

<p>You are guaranteed that no two <code>trees</code> have the same height and there is at least one tree needs to be cut off.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
<b>Output:</b> 6
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
<b>Output:</b> -1
</pre>

<p>&nbsp;</p>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
<b>Output:</b> 6
<b>Explanation:</b> You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
</pre>

<p>&nbsp;</p>

<p><b>Hint</b>: size of the given matrix will not exceed 50x50.</p>


-----------


## Similar Problems




## Solution:

[TOC]


#### Approach Framework

**Explanation**

Starting from `(0, 0)`, for each tree in height order, we will calculate the distance from where we are to the next tree (and move there), adding that distance to the answer.

We frame the problem as providing some distance function `dist(forest, sr, sc, tr, tc)` that calculates the path distance from source `(sr, sc)` to target `(tr, tc)` through obstacles `dist[i][j] == 0`.  (This distance function will return `-1` if the path is impossible.)

What follows is code and complexity analysis that is common to all three approaches.  After, the algorithms presented in our approaches will focus on only providing our `dist` function.


**Python**
```python
class Solution(object):
    def cutOffTree(self, forest):
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = dist(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans
```

**Java**
```java
class Solution {
    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};

    public int cutOffTree(List<List<Integer>> forest) {
        List<int[]> trees = new ArrayList();
        for (int r = 0; r < forest.size(); ++r) {
            for (int c = 0; c < forest.get(0).size(); ++c) {
                int v = forest.get(r).get(c);
                if (v > 1) trees.add(new int[]{v, r, c});
            }
        }

        Collections.sort(trees, (a, b) -> Integer.compare(a[0], b[0]));

        int ans = 0, sr = 0, sc = 0;
        for (int[] tree: trees) {
            int d = dist(forest, sr, sc, tree[1], tree[2]);
            if (d < 0) return -1;
            ans += d;
            sr = tree[1]; sc = tree[2];
        }
        return ans;
    }
}
```

**Complexity Analysis**

All three algorithms have similar worst case complexities, but in practice each successive algorithm presented performs faster on random data.

* Time Complexity: $$O((RC)^2)$$ where there are $$R$$ rows and $$C$$ columns in the given `forest`.  We walk to $$R*C$$ trees, and each walk could spend $$O(R*C)$$ time searching for the tree.

* Space Complexity: $$O(R*C)$$, the maximum size of the data structures used.

---
#### Approach #1: BFS [Accepted]

**Intuition and Algorithm**

We perform a breadth-first-search, processing nodes (grid positions) in a queue.  `seen` keeps track of nodes that have already been added to the queue at some point - those nodes will be already processed or are in the queue awaiting processing.

For each node that is next to be processed, we look at it's neighbors.  If they are in the forest (grid), they haven't been enqueued, and they aren't an obstacle, we will enqueue that neighbor.

We also keep a side count of the distance travelled for each node.  If the node we are processing is our destination 'target' `(tr, tc)`, we'll return the answer.

**Python**
```python
def bfs(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    queue = collections.deque([(sr, sc, 0)])
    seen = {(sr, sc)}
    while queue:
        r, c, d = queue.popleft()
        if r == tr and c == tc:
            return d
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if (0 <= nr < R and 0 <= nc < C and
                    (nr, nc) not in seen and forest[nr][nc]):
                seen.add((nr, nc))
                queue.append((nr, nc, d+1))
    return -1
```

**Java**
```java
public int bfs(List<List<Integer>> forest, int sr, int sc, int tr, int tc) {
    int R = forest.size(), C = forest.get(0).size();
    Queue<int[]> queue = new LinkedList();
    queue.add(new int[]{sr, sc, 0});
    boolean[][] seen = new boolean[R][C];
    seen[sr][sc] = true;
    while (!queue.isEmpty()) {
        int[] cur = queue.poll();
        if (cur[0] == tr && cur[1] == tc) return cur[2];
        for (int di = 0; di < 4; ++di) {
            int r = cur[0] + dr[di];
            int c = cur[1] + dc[di];
            if (0 <= r && r < R && 0 <= c && c < C &&
                    !seen[r][c] && forest.get(r).get(c) > 0) {
                seen[r][c] = true;
                queue.add(new int[]{r, c, cur[2]+1});
            }
        }
    }
    return -1;
}
```

---

#### Approach #2: A* Search [Accepted]

**Intuition and Algorithm**

The A* star algorithm is another path-finding algorithm.  For every node at position `(r, c)`, we have some estimated cost `node.f = node.g + node.h`, where `node.g` is the actual distance from `(sr, sc)` to `(r, c)`, and `node.h` is our *heuristic* (guess) of the distance from `(r, c)` to `(tr, tc)`.  In this case, our guess will be the taxicab distance, `node.h = abs(r-tr) + abs(c-tc)`.

We keep a priority queue to decide what node to search in (*expand*) next.  We can prove that if we find the target node, we must have travelled the lowest possible distance `node.g`.  By considering the last time where two backwards paths are the same, without loss of generality we could suppose the penultimate square of the two paths are different, and then in this case `node.f = node.g + 1`, showing the path with less actual distance travelled is expanded first as desired.

It might be useful for solvers familiar with *Dijkstra's Algorithm* to know that *A\* Search* is a special case of *Dijkstra's* with `node.h = 0` always.

**Python**
```python
def astar(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    heap = [(0, 0, sr, sc)]
    cost = {(sr, sc): 0}
    while heap:
        f, g, r, c = heapq.heappop(heap)
        if r == tr and c == tc: return g
        for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
            if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                if ncost < cost.get((nr, nc), 9999):
                    cost[nr, nc] = ncost
                    heapq.heappush(heap, (ncost, g+1, nr, nc))
    return -1
```

**Java**
```java
public int cutOffTree(List<List<Integer>> forest, int sr, int sc, int tr, int tc) {
    int R = forest.size(), C = forest.get(0).size();
    PriorityQueue<int[]> heap = new PriorityQueue<int[]>(
        (a, b) -> Integer.compare(a[0], b[0]));
    heap.offer(new int[]{0, 0, sr, sc});

    HashMap<Integer, Integer> cost = new HashMap();
    cost.put(sr * C + sc, 0);

    while (!heap.isEmpty()) {
        int[] cur = heap.poll();
        int g = cur[1], r = cur[2], c = cur[3];
        if (r == tr && c == tc) return g;
        for (int di = 0; di < 4; ++di) {
            int nr = r + dr[di], nc = c + dc[di];
            if (0 <= nr && nr < R && 0 <= nc && nc < C && forest.get(nr).get(nc) > 0) {
                int ncost = g + 1 + Math.abs(nr-tr) + Math.abs(nc-tr);
                if (ncost < cost.getOrDefault(nr * C + nc, 9999)) {
                    cost.put(nr * C + nc, ncost);
                    heap.offer(new int[]{ncost, g+1, nr, nc});
                }
            }
        }
    }
    return -1;
}
```

---
#### Approach #3: Hadlock's Algorithm [Accepted]

**Intuition**

Without any obstacles, the distance from `source = (sr, sc)` to `target = (tr, tc)` is simply `taxi(source, target) = abs(sr-tr) + abs(sc-tc)`.  This represents a sort of minimum distance that must be travelled.  Whenever we walk "away" from the target, we increase this minimum by 2, as we stepped 1 move, plus the taxicab distance from our new location has increased by one.

Let's call such a move that walks away from the target a *detour*.  It can be proven that the distance from source to target is simply `taxi(source, target) + 2 * detours`, where `detours` is the smallest number of detours in any path from `source` to `target`.

**Algorithm**

With respect to a `source` and `target`, call the *detour number* of a square to be the lowest number of detours possible in any path from `source` to that square.  (Here, detours are defined with respect to `target` - the number of away steps from that target.)

We will perform a priority-first-search in order of detour number.  If the target is found, it was found with the lowest detour number and therefore the lowest corresponding distance.  This motivates using `processed`, keeping track of when nodes are expanded, not visited - nodes could potentially be visited twice.

As each neighboring node can only have the same detour number or a detour number one higher, we will only consider at most 2 priority classes at a time.  Thus, we can use a deque (double ended queue) to perform this implementation.  We will place nodes with the same detour number to be expanded first, and nodes with a detour number one higher to be expanded after all nodes with the current number are done.

**Python**
```python
def hadlocks(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    processed = set()
    deque = collections.deque([(0, sr, sc)])
    while deque:
        detours, r, c = deque.popleft()
        if (r, c) not in processed:
            processed.add((r, c))
            if r == tr and c == tc:
                return abs(sr-tr) + abs(sc-tc) + 2*detours
            for nr, nc, closer in ((r-1, c, r > tr), (r+1, c, r < tr),
                                   (r, c-1, c > tc), (r, c+1, c < tc)):
                if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                    if closer:
                        deque.appendleft((detours, nr, nc))
                    else:
                        deque.append((detours+1, nr, nc))
    return -1
```

**Java**
```java
public int hadlocks(List<List<Integer>> forest, int sr, int sc, int tr, int tc) {
    int R = forest.size(), C = forest.get(0).size();
    Set<Integer> processed = new HashSet();
    Deque<int[]> deque = new ArrayDeque();
    deque.offerFirst(new int[]{0, sr, sc});
    while (!deque.isEmpty()) {
        int[] cur = deque.pollFirst();
        int detours = cur[0], r = cur[1], c = cur[2];
        if (!processed.contains(r*C + c)) {
            processed.add(r*C + c);
            if (r == tr && c == tc) {
                return Math.abs(sr-tr) + Math.abs(sc-tc) + 2 * detours;
            }
            for (int di = 0; di < 4; ++di) {
                int nr = r + dr[di];
                int nc = c + dc[di];
                boolean closer;
                if (di <= 1) closer = di == 0 ? r > tr : r < tr;
                else closer = di == 2 ? c > tc : c < tc;
                if (0 <= nr && nr < R && 0 <= nc && nc < C && forest.get(nr).get(nc) > 0) {
                    if (closer) deque.offerFirst(new int[]{detours, nr, nc});
                    else deque.offerLast(new int[]{detours+1, nr, nc});
                }
            }
        }
    }
    return -1;
}
```
---

Analysis written by: [@awice](https://leetcode.com/awice).
