# 0811 - Subdomain Visit Count

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table | [Leetcode](https://leetcode.com/problems/subdomain-visit-count) | [solution](https://leetcode.com/problems/subdomain-visit-count/solution/)


-----------

<p>A website domain like &quot;discuss.leetcode.com&quot; consists of various subdomains. At the top level, we have &quot;com&quot;, at the next level, we have &quot;leetcode.com&quot;, and at the lowest level, &quot;discuss.leetcode.com&quot;. When we visit a domain like &quot;discuss.leetcode.com&quot;, we will also visit the parent domains &quot;leetcode.com&quot; and &quot;com&quot; implicitly.</p>

<p>Now, call a &quot;count-paired domain&quot; to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be &quot;9001 discuss.leetcode.com&quot;.</p>

<p>We are given a list <code>cpdomains</code> of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> 
[&quot;9001 discuss.leetcode.com&quot;]
<strong>Output:</strong> 
[&quot;9001 discuss.leetcode.com&quot;, &quot;9001 leetcode.com&quot;, &quot;9001 com&quot;]
<strong>Explanation:</strong> 
We only have one website domain: &quot;discuss.leetcode.com&quot;. As discussed above, the subdomain &quot;leetcode.com&quot; and &quot;com&quot; will also be visited. So they will all be visited 9001 times.

</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> 
[&quot;900 google.mail.com&quot;, &quot;50 yahoo.com&quot;, &quot;1 intel.mail.com&quot;, &quot;5 wiki.org&quot;]
<strong>Output:</strong> 
[&quot;901 mail.com&quot;,&quot;50 yahoo.com&quot;,&quot;900 google.mail.com&quot;,&quot;5 wiki.org&quot;,&quot;5 org&quot;,&quot;1 intel.mail.com&quot;,&quot;951 com&quot;]
<strong>Explanation:</strong> 
We will visit &quot;google.mail.com&quot; 900 times, &quot;yahoo.com&quot; 50 times, &quot;intel.mail.com&quot; once and &quot;wiki.org&quot; 5 times. For the subdomains, we will visit &quot;mail.com&quot; 900 + 1 = 901 times, &quot;com&quot; 900 + 50 + 1 = 951 times, and &quot;org&quot; 5 times.

</pre>

<p><strong>Notes: </strong></p>

<ul>
	<li>The length of <code>cpdomains</code> will not exceed&nbsp;<code>100</code>.&nbsp;</li>
	<li>The length of each domain name will not exceed <code>100</code>.</li>
	<li>Each address will have either 1 or 2 &quot;.&quot; characters.</li>
	<li>The input count&nbsp;in any count-paired domain will not exceed <code>10000</code>.</li>
	<li>The answer output can be returned in any order.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Hash Map [Accepted]

**Intuition and Algorithm**

The algorithm is straightforward: we just do what the problem statement tells us to do.

For an address like `a.b.c`, we will count `a.b.c`, `b.c`, and `c`.  For an address like `x.y`, we will count `x.y` and `y`.

To count these strings, we will use a hash map.  To split the strings into the required pieces, we will use library `split` functions.

<iframe src="https://leetcode.com/playground/tMRWeTNX/shared" frameBorder="0" width="100%" height="395" name="tMRWeTNX"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `cpdomains`, and assuming the length of `cpdomains[i]` is fixed.

* Space Complexity: $$O(N)$$, the space used in our count.

---

Analysis written by: [@awice](https://leetcode.com/awice).
