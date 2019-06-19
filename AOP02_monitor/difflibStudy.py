#!usr/bin/python
# -*- coding: UTF-8 -*-
import difflib
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""
text1_lines = text1.splitlines()
text2 = """text2L:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
"""
text2_lines = text2.splitlines()

def test1():
	d = difflib.Differ()
	diff = d.compare(text1_lines,text2_lines)
	print '\n'.join(list(diff))

def testHtml():
	d = difflib.HtmlDiff()
	print d.make_file(text1_lines, text2_lines)

if __name__ == "__main__":
	testHtml()


