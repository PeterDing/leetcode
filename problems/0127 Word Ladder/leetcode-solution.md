# 0127 - Word Ladder

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Breadth-first Search | [Leetcode](https://leetcode.com/problems/word-ladder) | [solution](https://leetcode.com/problems/word-ladder/solution/)


-----------

<p>Given two words (<em>beginWord</em> and <em>endWord</em>), and a dictionary&#39;s word list, find the length of shortest transformation sequence from <em>beginWord</em> to <em>endWord</em>, such that:</p>

<ol>
	<li>Only one letter can be changed at a time.</li>
	<li>Each transformed word must exist in the word list. Note that <em>beginWord</em> is <em>not</em> a transformed word.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
	<li>Return 0 if there is no such transformation sequence.</li>
	<li>All words have the same length.</li>
	<li>All words contain only lowercase alphabetic characters.</li>
	<li>You may assume no duplicates in the word list.</li>
	<li>You may assume <em>beginWord</em> and <em>endWord</em> are non-empty and are not the same.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

<strong>Output: </strong>5

<strong>Explanation:</strong> As one shortest transformation is &quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; &quot;cog&quot;,
return its length 5.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

<strong>Output:</strong>&nbsp;0

<strong>Explanation:</strong>&nbsp;The endWord &quot;cog&quot; is not in wordList, therefore no possible<strong>&nbsp;</strong>transformation.
</pre>

<ul>
</ul>


-----------


## Similar Problems

- [Hard] [Word Ladder II](word-ladder-ii)

- [Medium] [Minimum Genetic Mutation](minimum-genetic-mutation)




## Solution:

[TOC]

## Solution

We are given a `beginWord` and an `endWord`. Let these two represent `start node` and `end node` of a graph. We have to reach from the start node to the end node using some intermediate nodes/words. The intermediate nodes are determined by the `wordList` given to us. The only condition for every step we take on this ladder of words is the current word should change by just `one letter`.

<center>
<img src="../Figures/127/Word_Ladder_1.png" width="400"/>
</center>

We will essentially be working with an undirected and unweighted graph with words as nodes and edges between words which differ by just one letter. The problem boils down to finding the shortest path from a start node to a destination node, if there exists one. Hence it can be solved using `Breadth First Search` approach.

One of the most important step here is to figure out how to find adjacent nodes i.e. words which differ by one letter. To efficiently find the neighboring nodes for any given word we do some pre-processing on the words of the given `wordList`. The pre-processing involves replacing the letter of a word by a non-alphabet say, `*`.

<center>
<img src="../Figures/127/Word_Ladder_2.png" width="400"/>
</center>

This pre-processing helps to form generic states to represent a single letter change.

For e.g. `Dog ----> D*g <---- Dig`

Both `Dog` and `Dig` map to the same intermediate or generic state `D*g`.

The preprocessing step helps us find out the generic one letter away nodes for any word of the word list and hence making it easier and quicker to get the adjacent nodes. Otherwise, for every word we will have to iterate over the entire word list and find words that differ by one letter. That would take a lot of time. This preprocessing step essentially builds the adjacency list first before beginning the breadth first search algorithm.

For eg. While doing BFS if we have to find the adjacent nodes for `Dug` we can first find all the generic states for `Dug`.

1. `Dug => *ug`
2. `Dug => D*g`
3. `Dug => Du*`

The second transformation `D*g` could then be mapped to `Dog` or `Dig`, since all of them share the same generic state. Having a common generic transformation means two words are connected and differ by one letter.

#### Approach 1: Breadth First Search

**Intuition**

Start from `beginWord` and search the `endWord` using BFS.

**Algorithm**

1. Do the pre-processing on the given `wordList` and find all the possible generic/intermediate states. Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.
2. Push a tuple containing the `beginWord` and `1` in a queue. The `1` represents the level number of a node. We have to return the level of the `endNode` as that would represent the shortest sequence/distance from the `beginWord`.
3. To prevent cycles, use a visited dictionary.
4. While the queue has elements, get the front element of the queue. Let's call this word as `current_word`.
5. Find all the generic transformations of the `current_word` and find out if any of these transformations is also a transformation of other words in the word list. This is achieved by checking the `all_combo_dict`.
6. The list of words we get from `all_combo_dict` are all the words which have a common intermediate state with the `current_word`. These new set of words will be the adjacent nodes/words to `current_word` and hence added to the queue.
6. Hence, for each word in this list of intermediate words, append `(word, level + 1)` into the queue where `level` is the level for the `current_word`.
7. Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.

    >Termination condition for standard BFS is finding the end word.

<iframe src="https://leetcode.com/playground/iU5FRmPH/shared" frameBorder="0" width="100%" height="500" name="iU5FRmPH"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(M \times N)$$, where $$M$$ is the length of words and $$N$$ is the total number of words in the input word list. Finding out all the transformations takes $$M$$ iterations for each of the $$N$$ words. Also, breadth first search in the worst case might go to each of the $$N$$ words.

* Space Complexity: $$O(M \times N)$$, to store all $$M$$ transformations for each of the $$N$$ words, in the `all_combo_dict` dictionary. Visited dictionary is of $$N$$ size. Queue for BFS in worst case would need space for all $$N$$ words.  
<br/>
<br/>

---

#### Approach 2: Bidirectional Breadth First Search

**Intuition**

The graph formed from the nodes in the dictionary might be too big. The search space considered by the breadth first search algorithm depends upon the branching factor of the nodes at each level. If the branching factor remains the same for all the nodes, the search space increases exponentially along with the number of levels. Consider a simple example of a binary tree. With each passing level in a complete binary tree, the number of nodes increase in powers of `2`.

We can considerably cut down the search space of the standard breadth first search algorithm if we launch two simultaneous BFS. One from the `beginWord` and one from the `endWord`. We progress one node at a time from both sides and at any point in time if we find a common node in both the searches, we stop the search. This is known as `bidirectional BFS` and it considerably cuts down on the search space and hence reduces the time and space complexity.

<center>
<img src="../Figures/127/Word_Ladder_3.png" width="600"/>
</center>

**Algorithm**

1. The algorithm is very similar to the standard BFS based approach we saw earlier.
2. The only difference is we now do BFS starting two nodes instead of one. This also changes the termination condition of our search.
3. We now have two visited dictionaries to keep track of nodes visited from the search starting at the respective ends.
4. If we ever find a node/word which is in the visited dictionary of the parallel search we terminate our search, since we have found the meet point of this bidirectional search. It's more like meeting in the middle instead of going all the way through.

    >Termination condition for bidirectional search is finding a word which is already been seen by the parallel search.

5. The shortest transformation sequence is the sum of levels of the meet point node from both the ends. Thus, for every visited node we save its level as value in the visited dictionary.

<center>
<img src="../Figures/127/Word_Ladder_4.png" width="600"/>
</center>


<iframe src="https://leetcode.com/playground/ZR8C4roL/shared" frameBorder="0" width="100%" height="500" name="ZR8C4roL"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(M \times N)$$, where $$M$$ is the length of words and $$N$$ is the total number of words in the input word list. Similar to one directional, bidirectional also takes $$M*N$$ for finding out all the transformations. But the search time reduces to half, since the two parallel searches meet somewhere in the middle.

* Space Complexity: $$O(M \times N)$$, to store all $$M$$ transformations for each of the $$N$$ words, in the `all_combo_dict` dictionary, same as one directional. But bidirectional reduces the search space. It narrows down because of meeting in the middle.  
<br/>

---
Analysis written by: [@godayaldivya](https://leetcode.com/godayaldivya/).
