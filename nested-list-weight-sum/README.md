<h2>339. Nested List Weight Sum</h2><h3>Easy</h3><hr><div><p>You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists.</p>

<p>Return <em>the sum of all integers in the list weighted by their depth</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Four 1's at depth 2, one 2 at depth 1.</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> 27
<strong>Explanation:</strong> One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nestedList = [0]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 50</code></li>
	<li>The values of the integers in the nested list is in the range <code>[-100, 100]</code>.</li>
	<li>The maximum depth of any integer is less than or equal to <code>50</code>.</li>
</ul>
</div>