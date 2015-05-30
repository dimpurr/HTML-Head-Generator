#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HTML Head Generator Builder
Author 	Dimpurr Cheny
Site 	http://dimpurr.com
Version 0.1"""
__author__ = 'Dimpurr Cheny'

html_head = """<!DOCTYPE html>
<html lang="zh-cmn-Hans">
<head>
	<meta charset="utf-8">
	<title>&lt;head&gt; Generator by Dimpurr</title>

	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="HandheldFriendly" content="true">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

	<meta name="application-name" content="&lt;head&gt; Generator" />
	<meta name="description" content="A HTML Head Tag Generator by Dimpurr Cheny">
	<meta name="author" content="dimpurr, dimpurr@live.com">

	<link rel="stylesheet" type="text/css" href="style.css">"""

html_main = """</head>
<body>
	<div class="ctn"><div class="content">
		<header class="header">
			<h1>HTML &lt;head&gt; Generator</h1>
			<p>
				Author by <a href="http://dimpurr.com/" title="Dimpurr Cheny">Dimpurr</a> - 
				<a href="http://find.moe/headgen" title="HTML &lt;head&gt; Generator by Dimpurr">Drag to Add Favourite</a><br />
				Hover the button for Tips
			</p>
		</header>"""

html_foot = """\n	</div></div>
</body>
</html>\n"""

data = [
	{ "doc": [
		{ "__name__": "HTML Doctype" },
		{ "doctype": [
			{ "html5": [
				"HTML 5 and Newer",
				"""<!DOCTYPE html>""",
				"HTML5 Doctype Tag",
				"checked",
			]},
			{ "html4-strict": [
				"HTML 4.01 Strict",
				"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">""",
				"HTML 4.01 Strict Doctype Tag",
			]},
			{ "html4-transitional": [
				"HTML 4.01 Transitional",
				"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">""",
				"HTML 4.01 Transitional Doctype Tag",
			]},
			{ "html4-frameset": [
				"HTML 4.01 Frameset",
				"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">""",
				"HTML 4.01 Frameset Doctype Tag",
			]},
			{ "xhtml1-0-strict": [
				"XHTML 1.0 Strict",
				"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">""",
				"XHTML 1.0 Strict Doctype Tag",
			]},
			{ "xhtml1-0-transitional": [
				"XHTML 1.0 Transitional",
				"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">""",
				"XHTML 1.0 Transitional Doctype Tag",
			]},
			{ "xhtml1-0-frameset": [
				"XHTML 1.0 Frameset",
				"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">""",
				"XHTML 1.0 Frameset Doctype Tag",
			]},
			{ "xhtml1-1": [
				"XHTML 1.1 (Strict)",
				"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">""",
				"XHTML 1.1 (Strict) Doctype Tag",
			]},
		]},
	]},
	{ "base": [
		{ "__name__": "Document Base Meta" },
		{ "html-lang": [
			{ "html-lang-zh-cmn-hans": [
				"Simplified Chinese",
				"""<html lang="zh-cmn-Hans">{{br}}<head>{{br}}{{br}}""",
				"Set Language to Simplified Chinese",
				"checked"
			]},
			{ "html-lang-zh-cmn-hant": [
				"Traditional Chinese",
				"""<html lang="zh-cmn-Hant">{{br}}<head>{{br}}{{br}}""",
				"Set Language to Traditional Chinese"
			]},
			{ "html-lang-en-us": [
				"American English",
				"""<html lang="en-us">{{br}}<head>{{br}}{{br}}""",
				"Set Language to American English"
			]},
			{ "html-lang-other": [
				"Other Language",
				"""<html lang="{{value}}">{{br}}<head>{{br}}{{br}}""",
				"Set Language to Other Language Code"
			]},
		]},
		{ "charset--new": [
			"Charset",
			"""<meta charset="{{utf-8}}">""",
			"Charset of Web Page",
			"checked",
		]},
		{ "charset--old": [
			"Charset",
			"""<meta http-equiv="Content-Type" content="text/html; charset={{utf-8}}">""",
			"Charset of Web Page",
			"checked",
		]},
		{ "title": [
			"Title",
			"""<title>{{value}}</title>""",
			"Title of Web Page",
			"checked",
		]},
	]},
	{ "seo": [
		{ "__name__": "SEO Meta" },

		{ "application-name": [
			"Application Name",
			"""<meta name="application-name" content="{{value}}" />""",
			"Application Name for Search Engines"
		]},
		{ "keywords": [
			"Keywords",
			"""<meta name="keywords" content="{{value}}" />""",
			"Keywords for Search Engines"
		]},
		{ "description": [
			"Description",
			"""<meta name="description" content="{{value}}">""",
			"Description for Search Engines"
		]},
		{ "author": [
			"Author",
			"""<meta name="author" content="{{value}}">""",
			"Author for Search Engines"
		]},
		{ "robots": [
			"Robots Nofollow",
			"""<meta name="robots" content="{{noindex,nofollow}}">""",
			"Rule for Search Engines Robots"
		]},
		{ "disable-baidu-siteapp": [
			"Disable Baidu Siteapp",
			"""<meta http-equiv="Cache-Control" content="no-siteapp" />""",
			"Disable Baidu Siteapp Mode, or Baidu will change to read mode and add their Ads"
		]},
		{ "disable-google-auto-translate": [
			"Disable Google Translate",
			"""<meta name="google" value="notranslate">""",
			"Disable Google Auto Translate Notice for Chrome"
		]},
	]},
	{ "link": [
		{ "__name__": "Link" },
		{ "rss": [
			"RSS Feed",
			"""<link rel="alternate" type="application/rss+xml" title="RSS" href="{{uri}}" />""",
			"Application Name for Search Engines"
		]},
		{ "favicon": [
			"Favicon",
			"""<link rel="shortcut icon" type="image/ico" href="{{uri}}" />""",
			"Application Name for Search Engines",
			"checked"
		]},
		{ "shortlink": [
			"Shortlink",
			"""<link rel="shortlink" href="{{uri}}"" />""",
			"Shrotlink for This Web Page"
		]},
		{ "index": [
			"Index",
			"""<link rel="index" title="{{value}}" href="{{uri}}" />""",
			"Index for This Web Site"
		]},
		{ "stylesheet": [
			"Stylesheet",
			"""<link rel="stylesheet" type="text/css" media="{{value}}" href="{{uri}}" />""",
			"Stylesheets for This Web Site"
		]},
	]},
	{ "platform": [
		{ "__name__": "Platform Compatibility Meta" },
		{ "cache-control": [
			"Cache Control",
			"""<meta http-equiv="Cache-Control" content="{{no-cache}}">""",
			"Enable Cache Control"
		]},
		{ "viewport": [
			"Responsible Viewport",
			"""<meta name="viewport" content="{{width=device-width, initial-scale=1.0}}">{{br}}<meta name="HandheldFriendly" content="true">""",
			"Responsible Set Viewport to Device Width\nUsing: width, height, initial-scale, maximum-scale, minimum-scale, user-scalable, minimal-ui (fullscreen in iOS 7 and newer)",
			"checked"
		]},
		{ "ie-edge-chrome": [
			"Prefer Newest Browser",
			"""<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />""",
			"Prefer Newest IE and Chrome",
			"checked"
		]},
		{ "chrome-frame": [
			"Prefer Chrome Frame",
			"""<meta name="renderer" content="webkit">""",
			"Prefer Chrome Webkit Mode (in 360 Browser)"
		]},
		{ "format-detection": [
			"Disable Number Dectect",
			"""<meta name="format-detection" content="telephone=no" />""",
			"Disable Telephone Number Dectect"
		]},
		{ "tap-highlight": [
			"Disable Tap Highlight",
			"""<meta name="msapplication-tap-highlight" content="no">""",
			"Disable Tap Highlight Effect (Windows Phone)"
		]},
	]},
	{ "webapp": [
		{ "__name__": "Web App Meta" },
		{ "ios-app-title": [
			"iOS App Title",
			"""<meta name="apple-mobile-web-app-title" content="{{value}}">""",
			"App Title for Homescreen (iOS 6 and newer)"
		]},
		{ "ios-app-fullscreen": [
			"iOS App Fullscreen",
			"""<meta name="apple-mobile-web-app-capable" content="yes" />""",
			"Enable Web App Capable Mode (iOS 6 and newer)"
		]},
		{ "ios-app-statusbar": [
			"iOS StatusBar Color",
			"""<meta name="apple-mobile-web-app-status-bar-style" content="{{black-translucent}}" />""",
			"Use: default, black, black-translucent (only take effect after enable fullscreen)"
		]},
		{ "windows-tile-color": [
			"Windows Tile Color",
			"""<meta name="msapplication-TileColor" content="{{value}}"/>""",
			"Windows Tile Color in Start Screen\nUse: hex color code"
		]},
		{ "windows-tile-image": [
			"Windows Tile Image",
			"""<meta name="msapplication-TileImage" content="{{uri}}"/>""",
			"Windows Tile Image in Start Screen"
		]},
		{ "android-theme-color": [
			"Android Theme Color",
			"""<meta name="theme-color" content="{{value}}">""",
			"Android Theme Color for Task Manager Tab\nUse: hex color code"
		]},
		{ "uc-app-mode": [
			"UC Browser App Mode",
			"""<meta name="browsermode" content="application">""",
			"Enable UC Browser App Mode"
		]},
		{ "uc-fullscreen-mode": [
			"UC Browser Fullsreen",
			"""<meta name="full-screen" content="yes">""",
			"Enable UC Browser Fullscreen Mode"
		]},
		{ "uc-orientation-mode": [
			{ "uc-portrait-mode": [
				"UC Browser Portrait",
				"""<meta name="screen-orientation" content="portrait">""",
				"Enable UC Browser Portrait Mode"
			]},
			{ "uc-landscape-mode": [
				"UC Browser Landscape",
				"""<meta name="screen-orientation" content="landscape">""",
				"Enable UC Browser Landscape Mode"
			]},
		]},
		{ "uc-fitscreen-mode": [
			"UC Browser Fitscreen",
			"""<meta name="layoutmode" content="fitscreen/standard" />""",
			"Enable UC Browser Fitscreen Mode"
		]},
		{ "uc-disable-night-mode": [
			"UC Disable Night Mode",
			"""	<meta name="nightmode" content="enable/disable"/>""",
			"Disable UC Browser Night Mode"
		]},
		{ "qq-app-mode": [
			"QQ Browser App Mode",
			"""<meta name="x5-page-mode" content="app">""",
			"Enable QQ Browser App Mode"
		]},
		{ "qq-fullscreen-mode": [
			"QQ Browser Fullscreen",
			"""<meta name="x5-fullscreen" content="true">""",
			"Enable QQ Browser Fullscreen Mode"
		]},
		{ "qq-orientation-mode": [
			{ "qq-portrait-mode": [
				"QQ Browser Portrait",
				"""<meta name="x5-orientation" content="portrait">""",
				"Enable QQ Browser Portrait Mode"
			]},
			{ "qq-landscape-mode": [
				"QQ Browser Landscape",
				"""<meta name="x5-orientation" content="landscape">""",
				"Enable QQ Browser Landscape Mode"
			]},
		]},

	]},
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
	}

.html5:checked ~ .fixed .ctn .code section[class$="--old"] {
	display: none;
}

.radio[class*="html4"]:checked ~ .fixed .ctn .code section[class$="--new"], .radio[class*="xhtml"]:checked ~ .fixed .ctn .code section[class$="--new"] {
	display: none;
}

.html5:checked ~ .check[name$="--old"], .html5:checked ~ .check[name$="--old"] + span {
	display: none;
}

.radio[class*="html4"]:checked ~ .check[name$="--new"], .radio[class*="html4"]:checked ~ .check[name$="--new"] + span, .radio[class*="xhtml"]:checked ~ .check[name$="--new"], .radio[class*="xhtml"]:checked ~ .check[name$="--new"] + span {
	display: none;
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
							html += """		<input type="radio" name="%s" class="check radio %s" %s title="%s">\n		<span>%s</span>\n""" % (module_key, radio_id, if_checked, radio[radio_id][2], radio[radio_id][0])
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
				if (module_key == "__name__") & ((section_key == "seo") | (section_key == "platform")):
					html+= "{{br}}"
				elif type(module[module_key][0]) == dict:
					for radio in module[module_key]:
						for radio_id in radio:
							html += "			<section class=\"" + radio_id + "\">" + cgi.escape(radio[radio_id][1]) + "</section>\n"
				else:
					for checkbox_id in module:
						html += "			<section class=\"" + checkbox_id + "\">" + cgi.escape(module[checkbox_id][1]) + "</section>\n"

html += """			<section style="display: block"><br />&lt;/head&gt;<br />&lt;/html&gt;</section>
		</div></div></div>\n"""
html += html_foot

html = html.replace('{{br}}','<br />')
replace = ['{{utf-8}}', '{{value}}', '{{uri}}', '{{noindex,nofollow}}', '{{width=device-width, initial-scale=1.0}}', '{{black-translucent}}', '{{no-cache}}']
for replace_char in replace:
	html = html.replace(replace_char,'<span class="value" contenteditable>' + replace_char[2:-2] + '</span>')

print html

with open(output, 'w') as file:
	file.write(html)