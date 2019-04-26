# 0303 - Range Sum Query - Immutable

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Dynamic Programming | [Leetcode](https://leetcode.com/problems/range-sum-query-immutable) | [solution](https://leetcode.com/problems/range-sum-query-immutable/solution/)


-----------

<p>Given an integer array <i>nums</i>, find the sum of the elements between indices <i>i</i> and <i>j</i> (<i>i</i> &le; <i>j</i>), inclusive.</p>

<p><b>Example:</b><br>
<pre>
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>You may assume that the array does not change.</li>
<li>There are many calls to <i>sumRange</i> function.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Range Sum Query 2D - Immutable](range-sum-query-2d-immutable)

- [Medium] [Range Sum Query - Mutable](range-sum-query-mutable)

- [Medium] [Maximum Size Subarray Sum Equals k](maximum-size-subarray-sum-equals-k)




## Solution:

[TOC]

## Solution
---
#### Approach #1 (Brute Force) [Time Limit Exceeded]

Each time *sumRange* is called, we use a for loop to sum each individual element from index $$i$$ to $$j$$.

```java
private int[] data;

public NumArray(int[] nums) {
    data = nums;
}

public int sumRange(int i, int j) {
    int sum = 0;
    for (int k = i; k <= j; k++) {
        sum += data[k];
    }
    return sum;
}
```

**Complexity analysis:**

* Time complexity : $$O(n)$$ time per query.
Each *sumRange* query takes $$O(n)$$ time.

* Space complexity : $$O(1)$$. Note that `data` is a *reference* to `nums` and is not a copy of it.

---
#### Approach #2 (Caching) [Accepted]

Imagine that *sumRange* is called one thousand times with the exact same arguments. How could we speed that up?

We could trade in extra space for speed. By pre-computing all range sum possibilities and store its results in a hash table, we can speed up the query to constant time.

```java
private Map<Pair<Integer, Integer>, Integer> map = new HashMap<>();

public NumArray(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        int sum = 0;
        for (int j = i; j < nums.length; j++) {
            sum += nums[j];
            map.put(Pair.create(i, j), sum);
        }
    }
}

public int sumRange(int i, int j) {
    return map.get(Pair.create(i, j));
}
```

**Complexity analysis**

* Time complexity : $$O(1)$$ time per query, $$O(n^2)$$ time pre-computation.
The pre-computation done in the constructor takes $$O(n^2)$$ time. Each *sumRange* query's time complexity is $$O(1)$$ as the hash table's look up operation is constant time.

* Space complexity : $$O(n^2)$$.
The extra space required is $$O(n^2)$$ as there are $$n$$ candidates for both $$i$$ and $$j$$.

---
#### Approach #3 (Caching) [Accepted]

The above approach takes a lot of space, could we optimize it?

Imagine that we pre-compute the cummulative sum from index $$0$$ to $$k$$. Could we use this information to derive $$Sum(i, j)$$?

Let us define $$sum[k]$$ as the cumulative sum for $$nums[0 \cdots k-1]$$ (inclusive):

$$
sum[k] = \left\{ \begin{array}{rl} \sum_{i=0}^{k-1}nums[i] & , k > 0 \\ 0 &, k = 0 \end{array} \right.
$$

Now, we can calculate *sumRange* as following:

$$
sumRange(i, j) = sum[j + 1] - sum[i]
$$

```java
private int[] sum;

public NumArray(int[] nums) {
    sum = new int[nums.length + 1];
    for (int i = 0; i < nums.length; i++) {
        sum[i + 1] = sum[i] + nums[i];
    }
}

public int sumRange(int i, int j) {
    return sum[j + 1] - sum[i];
}
```

Notice in the code above we inserted a dummy 0 as the first element in the *sum* array. This trick saves us from an extra conditional check in *sumRange* function.

**Complexity analysis**

* Time complexity : $$O(1)$$ time per query, $$O(n)$$ time pre-computation.
Since the cumulative sum is cached, each *sumRange* query can be calculated in $$O(1)$$ time.

* Space complexity : $$O(n)$$.
