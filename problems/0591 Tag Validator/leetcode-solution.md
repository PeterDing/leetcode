# 0591 - Tag Validator

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | String, Stack | [Leetcode](https://leetcode.com/problems/tag-validator) | [solution](https://leetcode.com/problems/tag-validator/solution/)


-----------

<p>Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:<p>
<ol>
<li>The code must be wrapped in a <b>valid closed tag</b>. Otherwise, the code is invalid.</li>
<li>A <b>closed tag</b> (not necessarily valid) has exactly the following format : <code>&lt;TAG_NAME&gt;TAG_CONTENT&lt;/TAG_NAME&gt;</code>. Among them, <code>&lt;TAG_NAME&gt;</code> is the start tag, and <code>&lt;/TAG_NAME&gt;</code> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is <b>valid</b> if and only if the TAG_NAME and TAG_CONTENT are valid.</li>
<li>A <b>valid</b> <code>TAG_NAME</code> only contain <b>upper-case letters</b>, and has length in range [1,9]. Otherwise, the <code>TAG_NAME</code> is <b>invalid</b>.</li>
<li>A <b>valid</b> <code>TAG_CONTENT</code> may contain other <b>valid closed tags</b>, <b>cdata</b> and any characters (see note1) <b>EXCEPT</b> unmatched <code>&lt;</code>, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the <code>TAG_CONTENT</code> is <b>invalid</b>.</li>
<li>A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.</li>
<li>A <code>&lt;</code> is unmatched if you cannot find a subsequent <code>></code>. And when you find a <code>&lt;</code> or <code>&lt;/</code>, all the subsequent characters until the next <code>></code> should be parsed as TAG_NAME  (not necessarily valid).</li>
<li>The cdata has the following format : <code>&lt;![CDATA[CDATA_CONTENT]]&gt;</code>. The range of <code>CDATA_CONTENT</code> is defined as the characters between <code>&lt;![CDATA[</code> and the <b>first subsequent</b> <code>]]></code>. </li>
<li><code>CDATA_CONTENT</code> may contain <b>any characters</b>. The function of cdata is to forbid the validator to parse <code>CDATA_CONTENT</code>, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as <b>regular characters</b>. </li>
</ol>

<p><b>Valid Code Examples:</b><br />
<pre>
<b>Input:</b> "&lt;DIV&gt;This is the first line &lt;![CDATA[&lt;div&gt;]]&gt;&lt;/DIV&gt;"<br />
<b>Output:</b> True<br />
<b>Explanation:</b> <br>
The code is wrapped in a closed tag : &lt;DIV> and &lt;/DIV>. <br>
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. <br>
Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.<br>
So TAG_CONTENT is valid, and then the code is valid. Thus return true.<br />

<b>Input:</b> "&lt;DIV>>>  ![cdata[]] &lt;![CDATA[&lt;div>]>]]>]]>>]&lt;/DIV>"<br />
<b>Output:</b> True<br />
<b>Explanation:</b><br />
We first separate the code into : start_tag|tag_content|end_tag.<br />
start_tag -> <b>"&lt;DIV&gt;"</b><br />
end_tag -> <b>"&lt;/DIV>"</b><br />
tag_content could also be separated into : text1|cdata|text2.<br />
text1 -> <b>">>  ![cdata[]] "</b><br />
cdata -> <b>"&lt;![CDATA[&lt;div>]>]]>"</b>, where the CDATA_CONTENT is <b>"&lt;div>]>"</b><br />
text2 -> <b>"]]>>]"</b><br />

The reason why start_tag is NOT <b>"&lt;DIV>>>"</b> is because of the rule 6.
The reason why cdata is NOT <b>"&lt;![CDATA[&lt;div>]>]]>]]>"</b> is because of the rule 7.
</pre>
</p>

<p><b>Invalid Code Examples:</b><br />
<pre>
<b>Input:</b> "&lt;A>  &lt;B> &lt;/A>   &lt;/B>"
<b>Output:</b> False
<b>Explanation:</b> Unbalanced. If "&lt;A>" is closed, then "&lt;B>" must be unmatched, and vice versa.

<b>Input:</b> "&lt;DIV&gt;  div tag is not closed  &lt;DIV&gt;"
<b>Output:</b> False

<b>Input:</b> "&lt;DIV&gt;  unmatched &lt  &lt;/DIV&gt;"
<b>Output:</b> False

<b>Input:</b> "&lt;DIV&gt; closed tags with invalid tag name  &lt;b>123&lt;/b> &lt;/DIV&gt;"
<b>Output:</b> False

<b>Input:</b> "&lt;DIV&gt; unmatched tags with invalid tag name  &lt;/1234567890> and &lt;CDATA[[]]>  &lt;/DIV&gt;"
<b>Output:</b> False

<b>Input:</b> "&lt;DIV&gt;  unmatched start tag &lt;B>  and unmatched end tag &lt;/C>  &lt;/DIV&gt;"
<b>Output:</b> False
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>For simplicity, you could assume the input code (including the <b>any characters</b> mentioned above) only contain <code>letters</code>, <code>digits</code>, <code>'&lt;'</code>,<code>'>'</code>,<code>'/'</code>,<code>'!'</code>,<code>'['</code>,<code>']'</code> and <code>' '</code>.</li>
</ol>
</p>

-----------


## Similar Problems

- [Medium] [Add Bold Tag in String](add-bold-tag-in-string)




## Solution:

[TOC]

## Solution

---
#### Approach 1: Stack

Summarizing the given problem, we can say that we need to determine whether a tag is valid or not, by checking the following properties.

1. The code should be wrapped in valid closed tag.

2. The `TAG_NAME` should be valid.

3. The `TAG_CONTENT` should be valid.

4. The **cdata** should be valid.

5. All the tags should be closed. i.e. each start-tag should have a corresponding end-tag and vice-versa and the order of the tags should be correct as well.

In order to check the validity of all these, firstly, we need to identify which parts of the given $$code$$ string act as which part from the above mentioned categories. To understand how it's done, we'll go through the implementation and the reasoning behind it step by step.

We iterate over the given $$code$$ string. Whenever a `<` is encountered(unless we are currently inside `<![CDATA[...]]>`), it indicates the beginning of either a `TAG_NAME`(start tag or end tag) or the beginning of cdata as per the conditions given in the problem statement. 

If the character immediately following this `<` is an `!`, the characters following this `<` can't be a part of a valid `TAG_NAME`, since only upper-case letters(in case of a start tag) or `/` followed by upper-case letters(in the case of an end tag). Thus, the choice now narrows down to only **cdata**. Thus, we need to check if the current bunch of characters following `<!`(including it) constitute a valid **cdata**. For doing this, firstly we find out the first matching `]]>` following the current `<!` to mark the ending of **cdata**. If no such matching `]]>` exists, the $$code$$ string is considered as invalid. Apart from this, the `<!` should also be immediately followed by `CDATA[` for the **cdata** to be valid. The characters lying inside the  `<![CDATA[` and `]]>` do not have any constraints on them.

If the character immediately following the `<` encountered isn't an `!`, this `<` can only mark the beginnning of `TAG_NAME`. Now, since a valid start tag can't contain anything except upper-case letters, if a `/` is found after `<`, the `</` pair indicates the beginning of an end tag. Now, when a `<` refers to the beginning of a `TAG_NAME`(either start-tag or end-tag), we find out the first closing `>` following the `<` to find out the substring(say $$s$$), that constitutes the `TAG_NAME`. This $$s$$ should satisfy all the criterion to constitute a valid `TAG_NAME`. Thus, for every such $$s$$, we check if it contains all upper-case letters and also check its length(It should be between 1 to 9). If any of the criteria isn't fulfilled, $$s$$ doesn't constitue a valid `TAG_NAME`. Hence, the $$code$$ string turns out to be invalid as well.

Apart from checking the validity of the `TAG_NAME`, we also need to ensure that the tags always exist in pairs. i.e. for every start-tag, a corresponding end-tag should always exist. Further, we can note that in case of multiple `TAG_NAME`'s, the `TAG_NAME` whose start-tag comes later than the other ones, should have its end-tag appearing before the end-tags of those other `TAG_NAME`'s. i.e. the tag which starts later should end first. 

From this, we get the intuition that we can make use of a $$stack$$ to check the existence of matching start and end-tags. Thus, whenever we find out a valid start-tag, as mentioned above, we push its `TAG_NAME` string onto a $$stack$$. Now, whenever an end-tag is found, we compare its `TAG_NAME` with the `TAG_NAME` at the top the $$stack$$ and remove this element from the $$stack$$. If the two don't match, this implies that either the current end-tag has no corresponding start-tag or there is a problem with the ordering of the tags. The two need to match for the tag-pair to be valid, since there can't exist an end-tag without a corresponding start-tag and vice-versa. Thus, if a match isn't found, we can conclude that the given $$code$$ string is invalid.

Now, after the complete $$code$$ string has been traversed, the $$stack$$ should be empty if all the start-tags have their corresponding end-tags as well. If the $$stack$$ isn't empty, this implies that some start-tag doesn't have the corresponding end-tag, violating the closed-tag's validity condition.

Further, we also need to ensure that the given $$code$$ is completely enclosed within closed tags. For this, we need to ensure that the first **cdata** found is also inside the closed tags. Thus, when we find a possibility of the presence of **cdata**, we proceed further only if we've already found a start tag, indicated by a non-empty stack. Further, to ensure that no data lies after the last end-tag, we need to ensure that the $$stack$$ doesn't become empty before we reach the end of the given $$code$$ string, since an empty $$stack$$ indicates that the last end-tag has been encountered.

The following animation depicts the process.

!?!../Documents/Tag_Validator_Stack.json:1000,563!?!


<iframe src="https://leetcode.com/playground/MSiS7Hb8/shared" frameBorder="0" width="100%" height="500" name="MSiS7Hb8"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$. We traverse over the given $$code$$ string of length $$n$$.

* Space complexity : $$O(n)$$. The stack can grow upto a size of $$n/3$$ in the worst case. e.g. In case of `<A><B><C><D>`, $$n$$=12 and number of tags = 12/3 = 4.
<br>
<br>

---
#### Approach 2: Regex

Instead of manually checking the given $$code$$ string for checking the validity of `TAG_NAME`, `TAG_CONTENT` and **cdata**, we can make use of an inbuilt java fuunctionality known as regular expressions.

A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. They can be used to search, edit, or manipulate text and data. The most common quantifiers used in regular expressions are listed below. A quantifier after a token (such as a character) or group specifies how often that preceding element is allowed to occur.

`?`	The question mark indicates zero or one occurrences of the preceding element. For example, colou?r matches both "color" and "colour".

`*`	The asterisk indicates zero or more occurrences of the preceding element. For example, ab*c matches "ac", "abc", "abbc", "abbbc", and so on.

`+`	The plus sign indicates one or more occurrences of the preceding element. For example, ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac".

`{n}` The preceding item is matched exactly **n** times.

`{min,}` The preceding item is matched **min** or more times.

`{min,max}`	The preceding item is matched at least **min** times, but not more than **max** times.

`|` A vertical bar separates alternatives. For example, gray|grey can match "gray" or "grey".

`()` Parentheses are used to define the scope and precedence of the operators (among other uses). For example, gray|grey and gr(a|e)y are equivalent patterns which both describe the set of "gray" or "grey".

`[...]`	Matches any single character in brackets.

`[^...]`	Matches any single character not in brackets.

Thus, by making use of regex, we can directly check the validity of the $$code$$ string directly(except the nesting of the inner tags) by using the regex expression below:

`<([A-Z]{1,9})>([^<]*((<\/?[A-Z]{1,9}>)|(<!\[CDATA\[(.*?)]]>))?[^<]*)*<\/\1>`

The image below shows the portion of the string that each part of the expression helps to match:

![Regex](../Figures/591/591_Tag_Validator.PNG)
{:align="center"}


But, if we make use of back-referencing as mentioned above, the matching process takes a very large amount of CPU time. Thus, we use the regex only to check the validity of the `TAG_CONTENT`, `TAG_NAME` and the **cdata**. We check the presence of the outermost closed tags by making use of a $$stack$$ as done in the last approach.

The rest of the process remains the same as in the last approach, except that we need not manually check the validity of `TAG_CONTENT`, `TAG_NAME` and the **cdata**, since it is already done by the regex expression. We only need to check the presence of inner closed tags.

Check [this](http://regexr.com/) link for testing any regular expression on a sample text.

<iframe src="https://leetcode.com/playground/tkdtPJcE/shared" frameBorder="0" width="100%" height="500" name="tkdtPJcE"></iframe>

**Complexity Analysis**

* Time complexity : Regular Expressions are/can be implemented in the form of Finite State Machines. Thus, the time complexity is dependent on the internal representation. In case of any suggestions, please comment below.

* Space complexity : $$O(n)$$. The stack can grow upto a size of $$n/3$$ in the worst case. e.g. In case of `<A><B><C><D>`, $$n$$=12 and number of tags = 12/3 = 4.
<br>
<br>

---
Analysis written by: [@vinod23](https://leetcode.com/vinod23)
