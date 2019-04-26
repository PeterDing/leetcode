# 0699 - Falling Squares

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Segment Tree, Ordered Map | [Leetcode](https://leetcode.com/problems/falling-squares) | [solution](https://leetcode.com/problems/falling-squares/solution/)


-----------

<p>On an infinite number line (x-axis), we drop given squares in the order they are given.</p>
<p>The <code>i</code>-th square dropped (<code>positions[i] = (left, side_length)</code>) is a square with the left-most point being <code>positions[i][0]</code> and sidelength <code>positions[i][1]</code>.</p>
<p>The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares.  We wait for each square to stick before dropping the next.</p>
<p>The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square).  Squares dropped adjacent to each other will not stick together prematurely.</p>

<br>
<p>Return a list <code>ans</code> of heights.  Each height <code>ans[i]</code> represents the current highest height of any square we have dropped, after dropping squares represented by <code>positions[0], positions[1], ..., positions[i]</code>.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1, 2], [2, 3], [6, 1]]
<b>Output:</b> [2, 5, 5]
<b>Explanation:</b>
<p>
After the first drop of <code>positions[0] = [1, 2]:
_aa
_aa
-------
</code>The maximum height of any square is 2.
</p><p>
After the second drop of <code>positions[1] = [2, 3]:
__aaa
__aaa
__aaa
_aa__
_aa__
--------------
</code>The maximum height of any square is 5.  
The larger square stays on top of the smaller square despite where its center
of gravity is, because squares are infinitely sticky on their bottom edge.
</p><p>
After the third drop of <code>positions[1] = [6, 1]:
__aaa
__aaa
__aaa
_aa
_aa___a
--------------
</code>The maximum height of any square is still 5.

Thus, we return an answer of <code>[2, 5, 5]</code>.
</pre>
</p>

<br>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [[100, 100], [200, 100]]
<b>Output:</b> [100, 100]
<b>Explanation:</b> Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.
</pre>
</p>

<p><b>Note:</b>
<li><code>1 <= positions.length <= 1000</code>.</li>
<li><code>1 <= positions[i][0] <= 10^8</code>.</li>
<li><code>1 <= positions[i][1] <= 10^6</code>.</li>
</p>

-----------


## Similar Problems

- [Hard] [The Skyline Problem](the-skyline-problem)




## Solution:

[TOC]

#### Approach Framework

**Intuition**

Intuitively, there are two operations: `update`, which updates our notion of the board (number line) after dropping a square; and `query`, which finds the largest height in the current board on some interval.  We will work on implementing these operations.

**Coordinate Compression**

In the below approaches, since there are only up to `2 * len(positions)` critical points, namely the left and right edges of each square, we can use a technique called *coordinate compression* to map these critical points to adjacent integers, as shown in the code snippets below.  

For brevity, these snippets are omitted from the remaining solutions.

**Python**
```python
coords = set()
for left, size in positions:
    coords.add(left)
    coords.add(left + size - 1)
index = {x: i for i, x in enumerate(sorted(coords))}
```

**Java**
```java
Set<Integer> coords = new HashSet();
for (int[] pos: positions) {
    coords.add(pos[0]);
    coords.add(pos[0] + pos[1] - 1);
}
List<Integer> sortedCoords = new ArrayList(coords);
Collections.sort(sortedCoords);

Map<Integer, Integer> index = new HashMap();
int t = 0;
for (int coord: sortedCoords) index.put(coord, t++);
```

---
#### Approach #1: Offline Propagation [Accepted]

**Intuition**

Instead of asking the question "what squares affect this query?", lets ask the question "what queries are affected by this square?"

**Algorithm**

Let `qans[i]` be the maximum height of the interval specified by `positions[i]`.  At the end, we'll return a running max of `qans`.

For each square `positions[i]`, the maximum height will get higher by the size of the square we drop.  Then, for any future squares that intersect the interval `[left, right)` (where `left = positions[i][0], right = positions[i][0] + positions[i][1]`), we'll update the maximum height of that interval.

**Python**
```python
class Solution(object):
    def fallingSquares(self, positions):
        qans = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in xrange(i+1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2: #intersect
                    qans[j] = max(qans[j], qans[i])

        ans = []
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans
```

**Java**
```java
class Solution {
    public List<Integer> fallingSquares(int[][] positions) {
        int[] qans = new int[positions.length];
        for (int i = 0; i < positions.length; i++) {
            int left = positions[i][0];
            int size = positions[i][1];
            int right = left + size;
            qans[i] += size;

            for (int j = i+1; j < positions.length; j++) {
                int left2 = positions[j][0];
                int size2 = positions[j][1];
                int right2 = left2 + size2;
                if (left2 < right && left < right2) { //intersect
                    qans[j] = Math.max(qans[j], qans[i]);
                }
            }
        }

        List<Integer> ans = new ArrayList();
        int cur = -1;
        for (int x: qans) {
            cur = Math.max(cur, x);
            ans.add(cur);
        }
        return ans;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the length of `positions`.  We use two for-loops, each of complexity $$O(N)$$.

* Space Complexity: $$O(N)$$, the space used by `qans` and `ans`.

---
#### Approach #2: Brute Force with Coordinate Compression [Accepted]

**Intuition and Algorithm**

Let `N = len(positions)`.  After mapping the board to a board of length at most $$2* N \leq 2000$$, we can brute force the answer by simulating each square's drop directly.

Our answer is either the current answer or the height of the square that was just dropped, and we'll update it appropriately.

**Python**
```python
class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate Compression
        #index = ...

        heights = [0] * len(index)
        def query(L, R):
            return max(heights[i] for i in xrange(L, R+1))

        def update(L, R, h):
            for i in xrange(L, R+1):
                heights[i] = max(heights[i], h)

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Java**
```java
class Solution {
    int[] heights;

    public int query(int L, int R) {
        int ans = 0;
        for (int i = L; i <= R; i++) {
            ans = Math.max(ans, heights[i]);
        }
        return ans;
    }

    public void update(int L, int R, int h) {
        for (int i = L; i <= R; i++) {
            heights[i] = Math.max(heights[i], h);
        }
    }

    public List<Integer> fallingSquares(int[][] positions) {
        //Coordinate Compression
        //HashMap<Integer, Integer> index = ...;
        //int t = ...;

        heights = new int[t];
        int best = 0;
        List<Integer> ans = new ArrayList();

        for (int[] pos: positions) {
            int L = index.get(pos[0]);
            int R = index.get(pos[0] + pos[1] - 1);
            int h = query(L, R) + pos[1];
            update(L, R, h);
            best = Math.max(best, h);
            ans.add(best);
        }
        return ans;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the length of `positions`.  We use two for-loops, each of complexity $$O(N)$$ (because of coordinate compression.)

* Space Complexity: $$O(N)$$, the space used by `heights`.

---
#### Approach #3: Block (Square Root) Decomposition [Accepted]

**Intuition**

Whenever we perform operations (like `update` and `query`) on some interval in a domain, we could segment that domain with size $$W$$ into blocks of size $$\sqrt{W}$$.  

Then, instead of a typical brute force where we update our array `heights` representing the board, we will also hold another array `blocks`, where `blocks[i]` represents the $$B = \lfloor \sqrt{W} \rfloor$$ elements `heights[B*i], heights[B*i + 1], ..., heights[B*i + B-1]`.  This allows us to write to the array in $$O(B)$$ operations.

**Algorithm**

Let's get into the details.  We actually need another array, `blocks_read`.  When we update some element `i` in block `b = i / B`, we'll also update `blocks_read[b]`.  If later we want to read the entire block, we can read from here (and stuff written to the whole block in `blocks[b]`.)

When we write to a block, we'll write in `blocks[b]`.  Later, when we want to read from an element `i` in block `b = i / B`, we'll read from `heights[i]` and `blocks[b]`.

Our process for managing `query` and `update` will be similar.  While `left` isn't a multiple of `B`, we'll proceed with a brute-force-like approach, and similarly for `right`.  At the end, `[left, right+1)` will represent a series of contiguous blocks: the interval will have length which is a multiple of `B`, and `left` will also be a multiple of `B`.

**Python**
```python
class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate compression
        #index = ...

        W = len(index)
        B = int(W**.5)
        heights = [0] * W
        blocks = [0] * (B+2)
        blocks_read = [0] * (B+2)

        def query(left, right):
            ans = 0
            while left % B and left <= right:
                ans = max(ans, heights[left], blocks[left / B])
                left += 1
            while right % B != B-1 and left <= right:
                ans = max(ans, heights[right], blocks[right / B])
                right -= 1
            while left <= right:
                ans = max(ans, blocks[left / B], blocks_read[left / B])
                left += B
            return ans

        def update(left, right, h):
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                blocks_read[left / B] = max(blocks_read[left / B], h)
                left += 1
            while right % B != B-1 and left <= right:
                heights[right] = max(heights[right], h)
                blocks_read[right / B] = max(blocks_read[right / B], h)
                right -= 1
            while left <= right:
                blocks[left / B] = max(blocks[left / B], h)
                left += B

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Java**
```java
class Solution {
    int[] heights;
    int[] blocks;
    int[] blocks_read;
    int B;

    public int query(int left, int right) {
        int ans = 0;
        while (left % B > 0 && left <= right) {
            ans = Math.max(ans, heights[left]);
            ans = Math.max(ans, blocks[left / B]);
            left++;
        }
        while (right % B != B - 1 && left <= right) {
            ans = Math.max(ans, heights[right]);
            ans = Math.max(ans, blocks[right / B]);
            right--;
        }
        while (left <= right) {
            ans = Math.max(ans, blocks[left / B]);
            ans = Math.max(ans, blocks_read[left / B]);
            left += B;
        }
        return ans;
    }

    public void update(int left, int right, int h) {
        while (left % B > 0 && left <= right) {
            heights[left] = Math.max(heights[left], h);
            blocks_read[left / B] = Math.max(blocks_read[left / B], h);
            left++;
        }
        while (right % B != B - 1 && left <= right) {
            heights[right] = Math.max(heights[right], h);
            blocks_read[right / B] = Math.max(blocks_read[right / B], h);
            right--;
        }
        while (left <= right) {
            blocks[left / B] = Math.max(blocks[left / B], h);
            left += B;
        }
    }

    public List<Integer> fallingSquares(int[][] positions) {
        //Coordinate Compression
        //HashMap<Integer, Integer> index = ...;
        //int t = ...;

        heights = new int[t];
        B = (int) Math.sqrt(t);
        blocks = new int[B+2];
        blocks_read = new int[B+2];

        int best = 0;
        List<Integer> ans = new ArrayList();

        for (int[] pos: positions) {
            int L = index.get(pos[0]);
            int R = index.get(pos[0] + pos[1] - 1);
            int h = query(L, R) + pos[1];
            update(L, R, h);
            best = Math.max(best, h);
            ans.add(best);
        }
        return ans;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N\sqrt{N})$$, where $$N$$ is the length of `positions`.  Each `query` and `update` has complexity $$O(\sqrt{N})$$.

* Space Complexity: $$O(N)$$, the space used by `heights`.

---
#### Approach #4: Segment Tree with Lazy Propagation [Accepted]

**Intuition**

If we were familiar with the idea of a segment tree (which supports queries and updates on intervals), we can immediately crack the problem.  

**Algorithm**

Segment trees work by breaking intervals into a disjoint sum of component intervals, whose number is at most `log(width)`.  The motivation is that when we change an element, we only need to change `log(width)` many intervals that aggregate on an interval containing that element.

When we want to update an interval all at once, we need to use *lazy propagation* to ensure good run-time complexity.  This topic is covered in more depth [here](https://leetcode.com/articles/recursive-approach-segment-trees-range-sum-queries-lazy-propagation/).

With such an implementation in hand, the problem falls out immediately.

**Python**
```python
class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def _pull(self, x):
        while x > 1:
            x /= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        for h in xrange(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2+ 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                self._apply(R, h)
                R -= 1
            L /= 2; R /= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):
        L += self.N
        R += self.N
        self._push(L); self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L /= 2; R /= 2
        return ans

class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate compression
        #index = ...

        tree = SegmentTree(len(index), max, max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left + size - 1]
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Java**

```java
class Solution {
    public List<Integer> fallingSquares(int[][] positions) {
        //Coordinate Compression
        //HashMap<Integer, Integer> index = ...;

        SegmentTree tree = new SegmentTree(sortedCoords.size());
        int best = 0;
        List<Integer> ans = new ArrayList();

        for (int[] pos: positions) {
            int L = index.get(pos[0]);
            int R = index.get(pos[0] + pos[1] - 1);
            int h = tree.query(L, R) + pos[1];
            tree.update(L, R, h);
            best = Math.max(best, h);
            ans.add(best);
        }
        return ans;
    }
}

class SegmentTree {
    int N, H;
    int[] tree, lazy;

    SegmentTree(int N) {
        this.N = N;
        H = 1;
        while ((1 << H) < N) H++;
        tree = new int[2 * N];
        lazy = new int[N];
    }

    private void apply(int x, int val) {
        tree[x] = Math.max(tree[x], val);
        if (x < N) lazy[x] = Math.max(lazy[x], val);
    }

    private void pull(int x) {
        while (x > 1) {
            x >>= 1;
            tree[x] = Math.max(tree[x * 2], tree[x * 2 + 1]);
            tree[x] = Math.max(tree[x], lazy[x]);
        }
    }

    private void push(int x) {
        for (int h = H; h > 0; h--) {
            int y = x >> h;
            if (lazy[y] > 0) {
                apply(y * 2, lazy[y]);
                apply(y * 2 + 1, lazy[y]);
                lazy[y] = 0;
            }
        }
    }

    public void update(int L, int R, int h) {
        L += N; R += N;
        int L0 = L, R0 = R, ans = 0;
        while (L <= R) {
            if ((L & 1) == 1) apply(L++, h);
            if ((R & 1) == 0) apply(R--, h);
            L >>= 1; R >>= 1;
        }
        pull(L0); pull(R0);
    }

    public int query(int L, int R) {
        L += N; R += N;
        int ans = 0;
        push(L); push(R);
        while (L <= R) {
            if ((L & 1) == 1) ans = Math.max(ans, tree[L++]);
            if ((R & 1) == 0) ans = Math.max(ans, tree[R--]);
            L >>= 1; R >>= 1;
        }
        return ans;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N \log N)$$, where $$N$$ is the length of `positions`.  This is the run-time complexity of using a segment tree.

* Space Complexity: $$O(N)$$, the space used by our tree.

---

Analysis written by: [@awice](https://leetcode.com/awice).
