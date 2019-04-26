# 0133 - Clone Graph

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Depth-first Search, Breadth-first Search, Graph | [Leetcode](https://leetcode.com/problems/clone-graph) | [solution](https://leetcode.com/problems/clone-graph/solution/)


-----------

<p>Given&nbsp;a reference of a node in a&nbsp;<strong><a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a></strong>&nbsp;undirected graph, return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> (clone) of the graph. Each node in the graph contains a val (<code>int</code>) and a list (<code>List[Node]</code>) of its neighbors.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/02/19/113_sample.png" style="width: 200px; height: 149px;" /></p>

<pre>
<strong>Input:
</strong>{&quot;$id&quot;:&quot;1&quot;,&quot;neighbors&quot;:[{&quot;$id&quot;:&quot;2&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;1&quot;},{&quot;$id&quot;:&quot;3&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;2&quot;},{&quot;$id&quot;:&quot;4&quot;,&quot;neighbors&quot;:[{&quot;$ref&quot;:&quot;3&quot;},{&quot;$ref&quot;:&quot;1&quot;}],&quot;val&quot;:4}],&quot;val&quot;:3}],&quot;val&quot;:2},{&quot;$ref&quot;:&quot;4&quot;}],&quot;val&quot;:1}

<strong>Explanation:</strong>
Node 1&#39;s value is 1, and it has two neighbors: Node 2 and 4.
Node 2&#39;s value is 2, and it has two neighbors: Node 1 and 3.
Node 3&#39;s value is 3, and it has two neighbors: Node 2 and 4.
Node 4&#39;s value is 4, and it has two neighbors: Node 1 and 3.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes will be between 1 and 100.</li>
	<li>The undirected&nbsp;graph is a <a href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Simple_graph" target="_blank">simple graph</a>,&nbsp;which means no repeated edges and no self-loops in the graph.</li>
	<li>Since the graph is undirected, if node <em>p</em>&nbsp;has node <em>q</em>&nbsp;as&nbsp;neighbor, then node <em>q</em>&nbsp;must have node <em>p</em>&nbsp;as neighbor too.</li>
	<li>You must return the <strong>copy of the given node</strong> as a reference to the cloned graph.</li>
</ol>


-----------


## Similar Problems

- [Medium] [Copy List with Random Pointer](copy-list-with-random-pointer)




## Thought:
