# 0819 - Most Common Word

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/most-common-word) | [solution](https://leetcode.com/problems/most-common-word/solution/)


-----------

<p>Given a paragraph&nbsp;and a list of banned words, return the most frequent word that is not in the list of banned words.&nbsp; It is guaranteed there is at least one word that isn&#39;t banned, and that the answer is unique.</p>

<p>Words in the list of banned words are given in lowercase, and free of punctuation.&nbsp; Words in the paragraph are not case sensitive.&nbsp; The answer is in lowercase.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 
paragraph = &quot;Bob hit a ball, the hit BALL flew far after it was hit.&quot;
banned = [&quot;hit&quot;]
<strong>Output:</strong> &quot;ball&quot;
<strong>Explanation:</strong> 
&quot;hit&quot; occurs 3 times, but it is a banned word.
&quot;ball&quot; occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as &quot;ball,&quot;), 
and that &quot;hit&quot; isn&#39;t the answer even though it occurs more because it is banned.
</pre>

<p>&nbsp;</p>

<p><strong>Note: </strong></p>

<ul>
	<li><code>1 &lt;= paragraph.length &lt;= 1000</code>.</li>
	<li><code>0 &lt;= banned.length &lt;= 100</code>.</li>
	<li><code>1 &lt;= banned[i].length &lt;= 10</code>.</li>
	<li>The answer is unique, and written in lowercase (even if its occurrences in <code>paragraph</code>&nbsp;may have&nbsp;uppercase symbols, and even if it is a proper noun.)</li>
	<li><code>paragraph</code> only consists of letters, spaces, or the punctuation symbols <code>!?&#39;,;.</code></li>
	<li>There are no hyphens or hyphenated words.</li>
	<li>Words only consist of letters, never apostrophes or other punctuation symbols.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Counting [Accepted]

**Intuition**

This problem is about the implementation, as the question tells us how to solve the problem.  We'll count each word separately, ignoring punctuation and converting each word to lowercase.  The word with the highest frequency that isn't in the banned list is the answer.

**Algorithm**

We'll need some `count` of words (converted to lowercase) that we have seen in the paragraph.  As we iterate through the paragraph, we will collect these words (with punctuation removed and converted to lowercase).

There are two ways we could try to collect these words: we could try to split the paragraph (delimited by spaces) and then clean up the fragment like `"Bob!"` to be `"bob"`.  Or, we could add characters one by one to build the next word, stopping when we reach a character that isn't a letter.

For each word (lowercase, and free of punctuation), we'll update our count and update the answer if the count of that word is highest (and the word is not banned.)

<iframe src="https://leetcode.com/playground/aAhpvopR/shared" frameBorder="0" width="100%" height="500" name="aAhpvopR"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(P + B)$$, where $$P$$ is the size of `paragraph` and $$B$$ is the size of `banned`.

* Space Complexity: $$O(P + B)$$, to store the `count` and the banned set.

---

Analysis written by: [@awice](https://leetcode.com/awice).
