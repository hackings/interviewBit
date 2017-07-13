# add character
# { - add everything before {, add next string increase tabs
# } - add everything before }, add next string decrease tabs
# , - add string, set string to same num tabs
class Solution:
	# @param A : string
	# @return a list of strings
	def prettyJSON(self, A):
		res = []
		if len(A) == 0:
			return res
		tab = "\t"
		num_tabs = 0;
		string = ""
		for c in A:
			if c != " ":
				string += c

			if c == "{" or c == "[":
				if len(string) > 2 and string[-2] != "\t":
					res.append(string[:-1])				# exclude last index = "{"
				string = (tab * num_tabs) + c;
				res.append(string)
				num_tabs += 1
				string = tab * num_tabs

			elif c == "}" or c == "]":
				num_tabs -= 1
				if len(string) > 2 and string[-2] != "\t":
					res.append(string[:-1])
				string = (tab * num_tabs) + c

			elif c == ",":
				res.append(string)
				string = tab * num_tabs
			
		if len(string) > 0 and string[-1] != "\t":
			res.append(string)
		return res


			
"""
Pretty print a json object using proper indentation.

Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Example 1:

Input : {A:"B",C:{D:"E",F:{G:"H",I:"J"}}}
Output : 
{ 
	A:"B",
	C: 
	{ 
		D:"E",
		F: 
		{ 
			G:"H",
			I:"J"
		} 
	}     
}

{				0 tab
	A:"B",		1
	C:			1
	{			1 tab
		D:"E",	2
		F:		2
		{		2
			G:"H",		3
			I:"J"		3
		}		2
	}			1
}				0

Example 2:

Input : ["foo", {"bar":["baz",null,1.0,2]}]
Output : 
[
	"foo", 
	{
		"bar":
		[
			"baz", 
			null, 
			1.0, 
			2
		]
	}
]
"""
