# 0609 - Find Duplicate File in System

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table, String | [Leetcode](https://leetcode.com/problems/find-duplicate-file-in-system) | [solution](https://leetcode.com/problems/find-duplicate-file-in-system/solution/)


-----------

<p>Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.</p>

<p>A group of duplicate files consists of at least <b>two</b> files that have exactly the same content.</p>

<p>A single directory info string in the <b>input</b> list has the following format:</p>

<p><code>&quot;root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)&quot;</code></p>

<p>It means there are <b>n</b> files (<code>f1.txt</code>, <code>f2.txt</code> ... <code>fn.txt</code> with content <code>f1_content</code>, <code>f2_content</code> ... <code>fn_content</code>, respectively) in directory <code>root/d1/d2/.../dm</code>. Note that n &gt;= 1 and m &gt;= 0. If m = 0, it means the directory is just the root directory.</p>

<p>The <b>output</b> is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:</p>

<p><code>&quot;directory_path/file_name.txt&quot;</code></p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b>
[&quot;root/a 1.txt(abcd) 2.txt(efgh)&quot;, &quot;root/c 3.txt(abcd)&quot;, &quot;root/c/d 4.txt(efgh)&quot;, &quot;root 4.txt(efgh)&quot;]
<b>Output:</b>  
[[&quot;root/a/2.txt&quot;,&quot;root/c/d/4.txt&quot;,&quot;root/4.txt&quot;],[&quot;root/a/1.txt&quot;,&quot;root/c/3.txt&quot;]]
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>No order is required for the final output.</li>
	<li>You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].</li>
	<li>The number of files given is in the range of [1,20000].</li>
	<li>You may assume no files or directories share the same name in the same directory.</li>
	<li>You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.</li>
</ol>

<p>&nbsp;</p>
<b>Follow-up beyond contest:</b>

<ol>
	<li>Imagine you are given a real file system, how will you search files? DFS or BFS?</li>
	<li>If the file content is very large (GB level), how will you modify your solution?</li>
	<li>If you can only read the file by 1kb each time, how will you modify your solution?</li>
	<li>What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?</li>
	<li>How to make sure the duplicated files you find are not false positive?</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution

---
#### Approach #1 Brute Force [Time Limit Exceeded]

**Algorithm**

For the brute force solution, firstly we obtain the directory paths, the filenames and file contents separately by appropriately splitting the elements of the $$paths$$ list. While doing so, we keep on creating a $$list$$ which contains the full path of every file along with the contents of the file. The $$list$$ contains data in the form $$[ [file_1\_full\_path, file_1\_contents], [file_2\_full\_path, file_2\_contents]..., [file_n\_full\_path, file_n\_contents] ]$$.

Once this is done, we iterate over this $$list$$. For every element $$i$$ chosen from the list, we iterate over the whole $$list$$ to find another element $$j$$ whose file contents are the same as the $$i^{th}$$ element. For every such element found, we put the $$j^{th}$$ element's file path in a temporary list $$l$$ and we also mark the $$j^{th}$$ element as visited so that this element isn't considered again in the future. Thus, when we reach the end of the array for every $$i^{th}$$ element, we obtain a list of file paths in $$l$$, which have the same contents as the file corresponding to the $$i^{th}$$ element. If this list isn't empty, it indicates that there exists content duplicate to the $$i^{th}$$ element. Thus, we also need to put the $$i^{th}$$ element's file path in the $$l$$. 

At the end of each iteration, we put this list $$l$$ obtained in the resultant list $$res$$ and reset the list $$l$$ for finding the duplicates of the next element.

<iframe src="https://leetcode.com/playground/P5yYSqFy/shared" frameBorder="0" name="P5yYSqFy" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n*x + f^2*s)$$. Creation of $$list$$ will take $$O(n*x)$$, where n is the number of directories and x is the average string length. Every file is compared with every other file. Let $$f$$ files are there with average size of $$s$$, then files comparision will take $$O(f^2*s)$$, equals can take $$O(s)$$. Here, Worst case will be when all files are unique.

* Space complexity : $$O(n*x)$$. Size of lists $$res$$ and $$list$$ can grow upto $$n*x$$.

---
#### Approach #2 Using HashMap [Accepted]

In this approach, firstly we obtain the directory paths, the file names and their contents separately by appropriately splitting each string in the given $$paths$$ list. In order to find the files with duplicate contents, we make use of a HashMap $$map$$, which stores the data in the form $$(contents, list\_of\_file\_paths\_with\_this\_content)$$. Thus, for every file's contents, we check if the same content already exist in the hashmap. If so, we add the current file's path to the list of files corresponding to the current contents. Otherwise, we create a new entry in the $$map$$, with the current contents as the key and the value being a list with only one entry(the current file's path).

At the end, we find out the contents corresponding to which atleast two file paths exist. We obtain the resultant list $$res$$, which is a list of lists containing these file paths corresponding to the same contents.

The following animation illustrates the process for a clearer understanding.

!?!../Documents/609_Find_Duplicate.json:1000,563!?!

<iframe src="https://leetcode.com/playground/9pU24YeR/shared" frameBorder="0" name="9pU24YeR" width="100%" height="428"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n*x)$$. $$n$$ strings of average length $$x$$ is parsed.

* Space complexity : $$O(n*x)$$. $$map$$ and $$res$$ size grows upto $$n*x$$.

---

Analysis written by: [@vinod23](https://leetcode.com/vinod23)
