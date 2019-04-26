# 0692 - Top K Frequent Words

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table, Heap, Trie | [Leetcode](https://leetcode.com/problems/top-k-frequent-words) | [solution](https://leetcode.com/problems/top-k-frequent-words/solution/)


-----------

<p>Given a non-empty list of words, return the <i>k</i> most frequent elements.</p>
<p>Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> ["i", "love", "leetcode", "i", "love", "coding"], k = 2
<b>Output:</b> ["i", "love"]
<b>Explanation:</b> "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
<b>Output:</b> ["the", "is", "sunny", "day"]
<b>Explanation:</b> "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>You may assume <i>k</i> is always valid, 1 &le; <i>k</i> &le; number of unique elements.</li>
<li>Input words contain only lowercase letters.</li>
</ol>
</p>

<p><b>Follow up:</b><br />
<ol>
<li>Try to solve it in <i>O</i>(<i>n</i> log <i>k</i>) time and <i>O</i>(<i>n</i>) extra space.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Top K Frequent Elements](top-k-frequent-elements)

- [Medium] [K Closest Points to Origin](k-closest-points-to-origin)




## Solution:

[TOC]


#### Approach #1: Sorting [Accepted]

**Intuition and Algorithm**

Count the frequency of each word, and sort the words with a custom ordering relation that uses these frequencies.  Then take the best `k` of them.

**Python**
```python
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]
```

**Java**
```java
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap();
        for (String word: words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        List<String> candidates = new ArrayList(count.keySet());
        Collections.sort(candidates, (w1, w2) -> count.get(w1).equals(count.get(w2)) ?
                w1.compareTo(w2) : count.get(w2) - count.get(w1));

        return candidates.subList(0, k);
```

**Complexity Analysis**

* Time Complexity: $$O(N \log{N})$$, where $$N$$ is the length of `words`.  We count the frequency of each word in $$O(N)$$ time, then we sort the given words in $$O(N \log{N})$$ time.

* Space Complexity: $$O(N)$$, the space used to store our `candidates`.

---

#### Approach #2: Heap [Accepted]

**Intuition and Algorithm**

Count the frequency of each word, then add it to heap that stores the best `k` candidates.  Here, "best" is defined with our custom ordering relation, which puts the worst candidates at the top of the heap.  At the end, we pop off the heap up to `k` times and reverse the result so that the best candidates are first.

In Python, we instead use `heapq.heapify`, which can turn a list into a heap in linear time, simplifying our work.

**Java**
```java
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap();
        for (String word: words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        PriorityQueue<String> heap = new PriorityQueue<String>(
                (w1, w2) -> count.get(w1).equals(count.get(w2)) ?
                w2.compareTo(w1) : count.get(w1) - count.get(w2) );

        for (String word: count.keySet()) {
            heap.offer(word);
            if (heap.size() > k) heap.poll();
        }

        List<String> ans = new ArrayList();
        while (!heap.isEmpty()) ans.add(heap.poll());
        Collections.reverse(ans);
        return ans;
    }
}
```

```python
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]
```

**Complexity Analysis**

* Time Complexity: $$O(N \log{k})$$, where $$N$$ is the length of `words`.  We count the frequency of each word in $$O(N)$$ time, then we add $$N$$ words to the heap, each in $$O(\log {k})$$ time.  Finally, we pop from the heap up to $$k$$ times.  As $$k \leq N$$, this is $$O(N \log{k})$$ in total.

  In Python, we improve this to $$O(N + k \log {N})$$: our `heapq.heapify` operation and counting operations are $$O(N)$$, and each of $$k$$ `heapq.heappop` operations are $$O(\log {N})$$.

* Space Complexity: $$O(N)$$, the space used to store our `count`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
