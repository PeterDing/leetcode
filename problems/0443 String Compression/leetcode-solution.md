# 0443 - String Compression

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/string-compression) | [solution](https://leetcode.com/problems/string-compression/solution/)


-----------

<p>Given an array of characters, compress it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><b>in-place</b></a>.</p>

<p>The length after compression must always be smaller than or equal to the original array.</p>

<p>Every element of the array should be a <b>character</b> (not int) of length 1.</p>

<p>After you are done <b>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></b>, return the new length of the array.</p>
&nbsp;

<p><b>Follow up:</b><br />
Could you solve it using only O(1) extra space?</p>
&nbsp;

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b>
[&quot;a&quot;,&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]

<b>Output:</b>
Return 6, and the first 6 characters of the input array should be: [&quot;a&quot;,&quot;2&quot;,&quot;b&quot;,&quot;2&quot;,&quot;c&quot;,&quot;3&quot;]

<b>Explanation:</b>
&quot;aa&quot; is replaced by &quot;a2&quot;. &quot;bb&quot; is replaced by &quot;b2&quot;. &quot;ccc&quot; is replaced by &quot;c3&quot;.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b>
[&quot;a&quot;]

<b>Output:</b>
Return 1, and the first 1 characters of the input array should be: [&quot;a&quot;]

<b>Explanation:</b>
Nothing is replaced.
</pre>

<p>&nbsp;</p>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b>
[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;]

<b>Output:</b>
Return 4, and the first 4 characters of the input array should be: [&quot;a&quot;,&quot;b&quot;,&quot;1&quot;,&quot;2&quot;].

<b>Explanation:</b>
Since the character &quot;a&quot; does not repeat, it is not compressed. &quot;bbbbbbbbbbbb&quot; is replaced by &quot;b12&quot;.
Notice each digit has it&#39;s own entry in the array.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>All characters have an ASCII value in <code>[35, 126]</code>.</li>
	<li><code>1 &lt;= len(chars) &lt;= 1000</code>.</li>
</ol>


-----------


## Similar Problems

- [Easy] [Count and Say](count-and-say)

- [Medium] [Encode and Decode Strings](encode-and-decode-strings)

- [Easy] [Design Compressed String Iterator](design-compressed-string-iterator)




## Solution:

[TOC]


#### Approach #1: Read and Write Heads [Accepted]

**Intuition**

We will use separate pointers `read` and `write` to mark where we are reading and writing from.  Both operations will be done left to right alternately:  we will read a contiguous group of characters, then write the compressed version to the array.  At the end, the position of the `write` head will be the length of the answer that was written.

**Algorithm**

Let's maintain `anchor`, the start position of the contiguous group of characters we are currently reading.

Now, let's read from left to right.  We know that we must be at the end of the block when we are at the last character, or when the next character is different from the current character.

When we are at the end of a group, we will write the result of that group down using our `write` head.  `chars[anchor]` will be the correct character, and the length (if greater than 1) will be `read - anchor + 1`.  We will write the digits of that number to the array.

**Python**
```python
class Solution(object):
    def compress(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
```

**Java**
```java
class Solution {
    public int compress(char[] chars) {
        int anchor = 0, write = 0;
        for (int read = 0; read < chars.length; read++) {
            if (read + 1 == chars.length || chars[read + 1] != chars[read]) {
                chars[write++] = chars[anchor];
                if (read > anchor) {
                    for (char c: ("" + (read - anchor + 1)).toCharArray()) {
                        chars[write++] = c;
                    }
                }
                anchor = read + 1;
            }
        }
        return write;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `chars`.

* Space Complexity: $$O(1)$$, the space used by `read`, `write`, and `anchor`.

---

Analysis written by: [@awice](https://leetcode.com/awice).