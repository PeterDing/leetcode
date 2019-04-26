# 0722 - Remove Comments

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String | [Leetcode](https://leetcode.com/problems/remove-comments) | [solution](https://leetcode.com/problems/remove-comments/solution/)


-----------

<p>Given a C++ program, remove comments from it. The program <code>source</code> is an array where <code>source[i]</code> is the <code>i</code>-th line of the source code.  This represents the result of splitting the original source code string by the newline character <code>\n</code>.</p>

<p>In C++, there are two types of comments, line comments, and block comments.</p>
<p>
The string <code>//</code> denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.
</p><p>
The string <code>/*</code> denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of <code>*/</code> should be ignored.  (Here, occurrences happen in reading order: line by line from left to right.)  To be clear, the string <code>/*/</code> does not yet end the block comment, as the ending would be overlapping the beginning.
</p><p>
The first effective comment takes precedence over others: if the string <code>//</code> occurs in a block comment, it is ignored. Similarly, if the string <code>/*</code> occurs in a line or block comment, it is also ignored.
</p><p>
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.
</p><p>
There will be no control characters, single quote, or double quote characters.  For example, <code>source = "string s = "/* Not a comment. */";"</code> will not be a test case.  (Also, nothing else such as defines or macros will interfere with the comments.)
</p><p>
It is guaranteed that every open block comment will eventually be closed, so <code>/*</code> outside of a line or block comment always starts a new comment.
</p><p>
Finally, implicit newline characters can be deleted by block comments.  Please see the examples below for details.
</p>

<p>After removing the comments from the source code, return the source code in the same format.</p>

<p><b>Example 1:</b><br />
<pre style="white-space: pre-wrap">
<b>Input:</b> 
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}

<b>Output:</b> ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{ 
  
int a, b, c;
a = b + c;
}

<b>Explanation:</b> 
The string <code>/*</code> denotes a block comment, including line 1 and lines 6-9. The string <code>//</code> denotes line 4 as comments.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre style="white-space: pre-wrap">
<b>Input:</b> 
source = ["a/*comment", "line", "more_comment*/b"]
<b>Output:</b> ["ab"]
<b>Explanation:</b> The original source string is "a/*comment<b>\n</b>line<b>\n</b>more_comment*/b", where we have bolded the newline characters.  After deletion, the <i>implicit</i> newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>source</code> is in the range <code>[1, 100]</code>.</li>
<li>The length of <code>source[i]</code> is in the range <code>[0, 80]</code>.</li>
<li>Every open block comment is eventually closed.</li>
<li>There are no single-quote, double-quote, or control characters in the source code.</li>
</p>

-----------


## Similar Problems

- [Medium] [Mini Parser](mini-parser)

- [Medium] [Ternary Expression Parser](ternary-expression-parser)




## Solution:

[TOC]

#### Approach #1: Parsing [Accepted]

**Intuition and Algorithm**

We need to parse the `source` line by line.  Our state is that we either are in a block comment or not.

* If we start a block comment and we aren't in a block, then we will skip over the next two characters and change our state to be in a block.

* If we end a block comment and we are in a block, then we will skip over the next two characters and change our state to be *not* in a block.

* If we start a line comment and we aren't in a block, then we will ignore the rest of the line.

* If we aren't in a block comment (and it wasn't the start of a comment), we will record the character we are at.

* At the end of each line, if we aren't in a block, we will record the line.

**Python**
```python
class Solution(object):
    def removeComments(self, source):
        in_block = False
        ans = []
        for line in source:
            i = 0
            if not in_block:
                newline = []
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 1
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == '//':
                    break
                elif not in_block:
                    newline.append(line[i])
                i += 1
            if newline and not in_block:
                ans.append("".join(newline))

        return ans
```

**Java**
```java
class Solution {
    public List<String> removeComments(String[] source) {
        boolean inBlock = false;
        StringBuilder newline = new StringBuilder();
        List<String> ans = new ArrayList();
        for (String line: source) {
            int i = 0;
            char[] chars = line.toCharArray();
            if (!inBlock) newline = new StringBuilder();
            while (i < line.length()) {
                if (!inBlock && i+1 < line.length() && chars[i] == '/' && chars[i+1] == '*') {
                    inBlock = true;
                    i++;
                } else if (inBlock && i+1 < line.length() && chars[i] == '*' && chars[i+1] == '/') {
                    inBlock = false;
                    i++;
                } else if (!inBlock && i+1 < line.length() && chars[i] == '/' && chars[i+1] == '/') {
                    break;
                } else if (!inBlock) {
                    newline.append(chars[i]);
                }
                i++;
            }
            if (!inBlock && newline.length() > 0) {
                ans.add(new String(newline));
            }
        }
        return ans;
    }
}
```

**Complexity Analysis**

* Time Complexity: $$O(S)$$, where $$S$$ is the total length of the source code.

* Space Complexity: $$O(S)$$, the space used by recording the source code into `ans`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
