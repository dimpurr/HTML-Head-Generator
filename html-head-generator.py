#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HTML Head Generator Builder
Author 	Dimpurr Cheny
Site 	http://dimpurr.com
Version 0.1"""
__author__ = 'Dimpurr Cheny'

html_head = """<!DOCTYPE html>
<html>
<head>
	<title>&lt;head&gt; Generator by Dimpurr</title>
	<link rel="stylesheet" type="text/css" href="style.css">"""

html_main = """</head>
<body>
	<div class="ctn"><div class="content">
		<header class="header">
			<h1>HTML &lt;head&gt; Generator</h1>
			<p>
				Socure at Github by <a href="http://dimpurr.com/" alt="Dimpurr Cheny">Dimpurr</a>
				<br/>
				<a href="http://to.find.moe/head" title="HTML &lt;head&gt; Generator by Dimpurr">Drag to Add Favourite</a>
			</p>
		</header>"""

html_foot = """\n	</div></div>
</body>
</html>\n"""

data = [
	{ "base": [
		{ "__name__": "Document Base Meta" },
		{ "doctype": [
			{ "html5": [
				"HTML5 Doctype",
				"""<!DOCTYPE html>{{br}}<head>""",
				"HTML5 Doctype Tag",
				"checked",
			]},
			{ "html4": [
				"HTML4 Doctype",
				"<!DOCTYPE html4>{{br}}<head>",
				"HTML4 Doctype Tag",
			]}
		]},
		{ "title": [
			"Title",
			"<title>{{value}}</title>",
			"Title of Web Page",
			"checked",
		]},
	]},
	{ "seo": [
		{ "__name__": "SEO Meta" },
		{ "keywords": [
			"Keywords",
			"<meta name=\"keywords\" content=\"{{value}}\" />",
			"Keywords for Search Tools"
		]}
	]}
]

import sys, getopt, cgi

output = "index.html"
opts, args = getopt.getopt(sys.argv[1:], "ho:")
for o, value in opts:
	if o == "-o":
		output = value
	elif o == "-h":
		print __doc__
		sys.exit()

html = "";
html += html_head

html += "\n	<style>"

for section_dict in data:
	for section_key in section_dict:
		section = section_dict[section_key]
		for module in section:
			for module_key in module:
				if module_key == "__name__":
					continue;
				elif type(module[module_key][0]) == dict:
					for radio in module[module_key]:
						for radio_id in radio:
							html += ".%s:checked ~ .fixed .ctn .code .%s, " % (radio_id, radio_id)
				else:
					for checkbox_id in module:
						html += ".%s:checked ~ .fixed .ctn .code .%s, " % (checkbox_id, checkbox_id)
html += """block {
		display: block;
	}</style>\n"""

html += html_main

for section_dict in data:
	for section_key in section_dict:
		section = section_dict[section_key]
		for module in section:
			for module_key in module:
				if module_key == "__name__":
					html+= "\n		<h2 class=\"sectionh\">" + module[module_key] + "</h2>\n\n"
				elif type(module[module_key][0]) == dict:
					for radio in module[module_key]:
						for radio_id in radio:
							if len(radio[radio_id]) == 4:
								if_checked = "checked"
							else:
								if_checked = ""
							html += """		<input type="radio" name="%s" class="check radio %s" %s title="%s">
		<span>%s</span>\n""" % (module_key, radio_id, if_checked, radio[radio_id][2], radio[radio_id][0])
				else:
					for checkbox_id in module:
						if len(module[checkbox_id]) == 4:
							if_checked = "checked"
						else:
							if_checked = ""
					html += """		<input type="checkbox" name="%s" class="check checkbox %s" %s title="%s">
		<span>%s</span>\n""" % (checkbox_id, checkbox_id, if_checked, module[checkbox_id][2], module[checkbox_id][0])

html += """\n		<div class="fixed"><div class="ctn"><div class="code">\n"""

for section_dict in data:
	for section_key in section_dict:
		section = section_dict[section_key]
		for module in section:
			for module_key in module:
				if module_key == "__name__":
					continue;
				elif type(module[module_key][0]) == dict:
					for radio in module[module_key]:
						for radio_id in radio:
							html += "			<section class=\"" + radio_id + "\">" + cgi.escape(radio[radio_id][1]) + "</section>\n"
				else:
					for checkbox_id in module:
						html += "			<section class=\"" + checkbox_id + "\">" + cgi.escape(module[checkbox_id][1]) + "</section>\n"

html += """			<section style="display: block">&lt;/head&gt;</section>
		</div></div></div>\n"""
html += html_foot

html = html.replace('{{br}}','<br />')
html = html.replace('{{value}}','<span class="value" contenteditable>{{value}}</span>')
html = html.replace('{{uri}}','<span class="uri" contenteditable>{{uri}}</span>')

print html

with open(output, 'w') as file:
	file.write(html)